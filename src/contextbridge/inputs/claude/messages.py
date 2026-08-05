from contextbridge.models.message import Message


def _extract_text(content: list) -> str:
    """
    Extract only the human-readable text from Claude content blocks.

    Tool calls, search results, thinking blocks, images, and other
    internal blocks are intentionally ignored because they create
    extremely noisy exports and are not useful for ChatGPT Projects.
    """

    if not content:
        return ""

    parts = []

    for block in content:
        if block.get("type") != "text":
            continue

        text = block.get("text", "").strip()

        if text:
            parts.append(text)

    return "\n\n".join(parts)


def parse_message(raw_message: dict) -> Message:
    """
    Convert one Claude message into the universal Message model.
    """

    role = raw_message.get("sender", "")

    if role == "human":
        role = "user"
    elif role == "assistant":
        role = "assistant"
    else:
        role = "system"

    text = _extract_text(raw_message.get("content", []))

    if not text:
        text = raw_message.get("text", "").strip()

    return Message(
        id=raw_message["uuid"],
        role=role,
        text=text,
        created_at=raw_message.get("created_at"),
        metadata={
            "updated_at": raw_message.get("updated_at"),
            "attachments": raw_message.get("attachments", []),
            "files": raw_message.get("files", []),
            "parent_message_uuid": raw_message.get("parent_message_uuid"),
        },
    )