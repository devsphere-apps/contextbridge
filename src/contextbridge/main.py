import re

import typer
from rich import print

from contextbridge.core.context import build_context
from contextbridge.outputs.markdown.exporter import MarkdownExporter
from contextbridge.version import __version__

app = typer.Typer(
    help="ContextBridge - Universal AI project migration toolkit"
)


@app.command()
def version():
    """
    Show ContextBridge version.
    """
    print(f"ContextBridge v{__version__}")


@app.command()
def inspect(path: str):
    """
    Inspect a Claude export.
    """

    context = build_context(path)

    print("[green]✓ Claude export detected[/green]")
    print()
    print(f"Conversations: {len(context.conversations)}")

    total_messages = sum(
        len(c.messages)
        for c in context.conversations
    )

    print(f"Messages:      {total_messages}")


@app.command()
def export(
    path: str,
    format: str = typer.Option(
        "markdown",
        "--format",
        "-f",
        help="Export format.",
    ),
    output: str = typer.Option(
        "exports",
        "--output",
        "-o",
        help="Output directory.",
    ),
    conversation: str | None = typer.Option(
        None,
        "--conversation",
        "-c",
        help="Export a single conversation by UUID.",
    ),
    url: str | None = typer.Option(
        None,
        "--url",
        help="Claude conversation URL.",
    ),
):
    """
    Export a Claude project.
    """

    context = build_context(path)

    if url:
        match = re.search(
            r"/chat/([0-9a-fA-F-]+)",
            url,
        )

        if not match:
            raise typer.BadParameter(
                "Invalid Claude conversation URL."
            )

        conversation = match.group(1)

    if conversation:
        context = context.filter_conversations(
            [conversation]
        )

        if not context.conversations:
            raise typer.BadParameter(
                f"Conversation '{conversation}' not found."
            )

    if format.lower() == "markdown":
        MarkdownExporter().export(
            context,
            output,
        )

        if conversation:
            print(
                f"[green]✓ Exported 1 conversation to {output}[/green]"
            )
        else:
            print(
                f"[green]✓ Exported {len(context.conversations)} conversations to {output}[/green]"
            )

    else:
        raise typer.BadParameter(
            f"Unsupported format: {format}"
        )


if __name__ == "__main__":
    app()