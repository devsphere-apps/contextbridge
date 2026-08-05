from datetime import datetime

from pydantic import BaseModel, Field

from contextbridge.models.message import Message


class Conversation(BaseModel):
    """
    Universal conversation model.
    """

    id: str = Field(
        description="Unique conversation identifier"
    )

    title: str = Field(
        default="",
        description="Conversation title",
    )

    summary: str = Field(
        default="",
        description="Conversation summary",
    )

    created_at: datetime | None = Field(
        default=None,
        description="Creation timestamp",
    )

    updated_at: datetime | None = Field(
        default=None,
        description="Last updated timestamp",
    )

    messages: list[Message] = Field(
        default_factory=list,
        description="Messages in this conversation",
    )

    metadata: dict = Field(
        default_factory=dict,
        description="Provider-specific metadata",
    )