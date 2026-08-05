from entities.ClienteEntity import Cliente
from entities.DocumentoEntity import Documento
from entities.AdvogadoEntity import Advogado
from entities.ProcessoEntity import Processo
from dataclasses import asdict

class DocumentoService:
    def __init__(self, templatePath: str):
        self.documento = Documento(templatePath)

    def gerarDocumento(self, cliente: Cliente,
                             advogado: Advogado,
                             processo: Processo,
                             pathArquivo: str) -> None:
        
        contexto = self._montaContexto(cliente, advogado, processo)
        self.documento.render(contexto)
        self.documento.save(f"{pathArquivo}.docx")

    def _montaContexto(self, cliente: Cliente, advogado: Advogado, processo: Processo) -> dict:
        contexto = asdict(cliente) | asdict(advogado) | asdict(processo)
        contexto["nome"] = cliente.contratante
        contexto["numero_rg"] = cliente.rg
        contexto["endereco"] = self._montaEndereco(cliente)
        return contexto

    def _montaEndereco(self, cliente: Cliente) -> str:
        endereco = f"{cliente.logradouro}, {cliente.numero}"
        if cliente.complemento:
            endereco += f", {cliente.complemento}"
        return endereco