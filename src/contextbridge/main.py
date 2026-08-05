from pathlib import Path

import typer

from contextbridge.inputs.claude.conversations import ConversationParser
from contextbridge.inputs.claude.loader import ClaudeLoader
from contextbridge.version import __version__

app = typer.Typer(
    help="ContextBridge - Universal AI project migration toolkit."
)


@app.callback()
def main():
    """ContextBridge CLI."""
    pass


@app.command()
def version():
    """Show the current version."""
    typer.echo(f"ContextBridge v{__version__}")


@app.command()
def inspect(path: str):
    """
    Inspect a Claude export.
    """

    export_path = Path(path)

    loader = ClaudeLoader(export_path)

    if not loader.is_valid_export():
        typer.secho("❌ Invalid Claude export.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    parser = ConversationParser(export_path)
    conversations = parser.load()

    message_count = sum(len(c.messages) for c in conversations)

    typer.secho("✓ Claude export detected", fg=typer.colors.GREEN)
    typer.echo()

    typer.echo(f"Conversations: {len(conversations)}")
    typer.echo(f"Messages:      {message_count}")


if __name__ == "__main__":
    app()