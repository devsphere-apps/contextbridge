from pathlib import Path


REQUIRED_FILES = [
    "conversations.json",
]


class ClaudeLoader:
    """
    Detects and validates a Claude export directory.
    """

    def __init__(self, export_path: str | Path):
        self.export_path = Path(export_path)

    def exists(self) -> bool:
        return self.export_path.exists()

    def is_valid_export(self) -> bool:
        if not self.exists():
            return False

        for item in REQUIRED_FILES:
            if not (self.export_path / item).exists():
                return False

        return True