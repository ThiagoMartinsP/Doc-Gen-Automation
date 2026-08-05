from docxtpl import DocxTemplate
from infrastructure.wrappers.DocumentoWrapper import IDocumentoWrapper

class DocxWrapper(IDocumentoWrapper):
    def __init__(self, nomeArquivo: str):
        self.nomeArquivo = nomeArquivo
        self.documento = DocxTemplate(nomeArquivo)

    def preencheDocumento(self, contexto: dict) -> None:
        self.documento.render(contexto)

    def salvar(self, outputPath: str) -> None:
        self.documento.save(outputPath)

    def getVariaveisDocumento(self):
        return self.documento.get_undeclared_template_variables()