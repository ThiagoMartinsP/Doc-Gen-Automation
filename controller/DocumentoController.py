from infrastructure.repository.ClienteSheetRepository import ClienteSheetRepository
from infrastructure.repository.ProcessoSheetRepository import ProcessoSheetRepository
from services.DocumentoService import DocumentoService

from entities.AdvogadoEntity import Advogado

class DocumentoController:
    def __init__(self,
                 clienteRepository: ClienteSheetRepository,
                 processoRepository: ProcessoSheetRepository,
                 documentoService: DocumentoService):
        
        self.clienteRepository = clienteRepository
        self.processoRepository = processoRepository
        self.documentoService = documentoService

    def gerarDocumento(self, linhaCliente: int, linhaProcesso: int) -> str:
        advogado = Advogado("Yuri Henrique Bernardes Campagnolli",
                            "270727",
                            "RJ",
                            "*endereço do escritorio*")
        
        cliente = self.clienteRepository.find(linhaCliente)
        processo = self.processoRepository.find(linhaProcesso)

        outputPath = cliente.num_cpf_cliente
        self.documentoService.gerarDocumento(cliente,
                                             advogado,
                                             processo,
                                             outputPath)

        return outputPath