from abc import ABC, abstractmethod

class ISheetRepository(ABC):
    @abstractmethod
    def find(self, line: int):
        pass