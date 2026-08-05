from entities.ClienteEntity import Cliente
from infrastructure.wrappers.DocumentoWrapper import IDocumentoWrapper
from entities.AdvogadoEntity import Advogado
from entities.ProcessoEntity import Processo
from dataclasses import asdict

import locale
from datetime import datetime

class DocumentoService:
    def __init__(self, documento: IDocumentoWrapper):
        self.documento = documento

    def gerarDocumento(self, cliente: Cliente,
                             advogado: Advogado,
                             processo: Processo,
                             pathOutputArquivo: str) -> None:
        
        contexto = self._montaContexto(cliente, advogado, processo)
        self.documento.preencheDocumento(contexto)
        self.documento.salvar(f"{pathOutputArquivo}.docx")

    def _montaContexto(self, cliente: Cliente, advogado: Advogado, processo: Processo) -> dict:
        dataAtual = datetime.now()

        locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

        dictDataAtual = {"dia_atual": f"{dataAtual.day:02d}",
                         "mes_atual": dataAtual.strftime("%B").capitalize(),
                         "ano_atual": dataAtual.year}
        
        contexto = asdict(cliente) | asdict(advogado) | asdict(processo) | dictDataAtual
        return contexto