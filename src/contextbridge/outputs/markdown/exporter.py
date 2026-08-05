from pathlib import Path
import re

from contextbridge.models.project_context import ProjectContext
from contextbridge.outputs.base import Exporter


class MarkdownExporter(Exporter):
    """
    Export a ProjectContext into Markdown files.

    Each conversation becomes its own .md file.
    """

    def export(
        self,
        context: ProjectContext,
        output_dir: str | Path,
    ) -> None:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        for conversation in context.conversations:
            filename = self._safe_filename(conversation.title)

            if not filename:
                filename = conversation.id

            filepath = output_dir / f"{filename}.md"

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(self._render_conversation(conversation))

    def _render_conversation(self, conversation) -> str:
        lines = []

        lines.append(f"# {conversation.title or conversation.id}")
        lines.append("")

        if conversation.summary:
            lines.append("## Summary")
            lines.append("")
            lines.append(conversation.summary)
            lines.append("")

        lines.append("---")
        lines.append("")

        for message in conversation.messages:
            role = message.role.capitalize()

            lines.append(f"## {role}")
            lines.append("")

            if message.text:
                lines.append(message.text)
            else:
                lines.append("_No text_")

            lines.append("")
            lines.append("---")
            lines.append("")

        return "\n".join(lines)

    def _safe_filename(self, name: str) -> str:
        if not name:
            return ""

        name = re.sub(r'[<>:"/\\|?*]', "", name)
        name = name.strip()
        name = re.sub(r"\s+", " ", name)

        return name[:120]