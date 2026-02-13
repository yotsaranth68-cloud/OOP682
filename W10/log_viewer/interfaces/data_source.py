
# interface ILogSource(ABC):
from abc import ABC, abstractmethod
from typing import List


class ILogSource(ABC):
    @abstractmethod
    def get_logs(self) -> List[str]:
        """Retrieve logs from the source."""
        pass