from datetime import datetime

from pydantic import BaseModel, Field


class Message(BaseModel):
    """
    Universal message model used internally by ContextBridge.

    All AI providers (Claude, ChatGPT, Gemini, Cursor, etc.)
    should map their message formats into this model.
    """

    id: str = Field(description="Unique message identifier")

    role: str = Field(
        description="Message role (user, assistant, system)"
    )

    text: str = Field(
        default="",
        description="Plain text content",
    )

    created_at: datetime | None = Field(
        default=None,
        description="Creation timestamp",
    )

    metadata: dict = Field(
        default_factory=dict,
        description="Provider-specific metadata",
    )