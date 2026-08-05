from pydantic import BaseModel, Field

from contextbridge.models.conversation import Conversation


class ProjectContext(BaseModel):
    """
    Universal project representation.

    Every importer builds this.
    Every exporter consumes this.
    """

    conversations: list[Conversation] = Field(default_factory=list)

    metadata: dict = Field(default_factory=dict)

    def filter_conversations(self, conversation_ids: list[str]) -> "ProjectContext":
        """
        Return a new ProjectContext containing only the selected conversations.
        """

        return ProjectContext(
            conversations=[
                conversation
                for conversation in self.conversations
                if conversation.id in conversation_ids
            ],
            metadata=self.metadata.copy(),
        )