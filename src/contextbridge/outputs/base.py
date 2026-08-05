from abc import ABC, abstractmethod
from pathlib import Path

from contextbridge.models.project_context import ProjectContext


class Exporter(ABC):
    @abstractmethod
    def export(
        self,
        context: ProjectContext,
        output_dir: str | Path,
    ) -> None:
        pass