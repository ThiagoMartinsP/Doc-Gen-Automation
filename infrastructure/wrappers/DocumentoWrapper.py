from abc import ABC, abstractmethod

class IDocumentoWrapper(ABC):
    @abstractmethod
    def preencheDocumento(self, contexto: dict) -> None:
        pass
    
    @abstractmethod
    def salvar(self, outputPath: str) -> None:
        pass

    @abstractmethod
    def getVariaveisDocumento(self) -> list:
        pass