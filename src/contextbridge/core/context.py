from pathlib import Path

from contextbridge.inputs.claude.conversations import ConversationParser
from contextbridge.inputs.claude.loader import ClaudeLoader
from contextbridge.models.project_context import ProjectContext


def build_context(export_path: str | Path) -> ProjectContext:
    """
    Build a ProjectContext from a Claude export.
    """

    loader = ClaudeLoader(export_path)

    if not loader.is_valid_export():
        raise ValueError("Invalid Claude export.")

    conversations = ConversationParser(export_path).load()

    return ProjectContext(
        conversations=conversations,
        metadata={
            "provider": "claude",
        },
    )