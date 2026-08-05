from contextbridge.models.message import Message


def parse_message(raw_message: dict) -> Message:
    """
    Convert one Claude message into the universal Message model.
    """

    role = raw_message.get("sender", "")

    if role == "human":
        role = "user"

    return Message(
        id=raw_message["uuid"],
        role=role,
        text=raw_message.get("text", ""),
        created_at=raw_message.get("created_at"),
        metadata={
            "updated_at": raw_message.get("updated_at"),
            "content": raw_message.get("content", []),
            "attachments": raw_message.get("attachments", []),
            "files": raw_message.get("files", []),
            "parent_message_uuid": raw_message.get("parent_message_uuid"),
        },
    )