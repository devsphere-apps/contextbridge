from __future__ import annotations

import json
from pathlib import Path

from contextbridge.inputs.claude.messages import parse_message
from contextbridge.models.conversation import Conversation


class ConversationParser:
    """
    Parses Claude conversations.json into Conversation models.
    """

    def __init__(self, export_path: str | Path):
        self.export_path = Path(export_path)

    def load(self) -> list[Conversation]:
        file_path = self.export_path / "conversations.json"

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        conversations: list[Conversation] = []

        for raw_conversation in data:
            messages = [
                parse_message(message)
                for message in raw_conversation.get("chat_messages", [])
            ]

            conversations.append(
                Conversation(
                    id=raw_conversation["uuid"],
                    title=raw_conversation.get("name", ""),
                    summary=raw_conversation.get("summary", ""),
                    created_at=raw_conversation.get("created_at"),
                    updated_at=raw_conversation.get("updated_at"),
                    messages=messages,
                )
            )

        return conversations