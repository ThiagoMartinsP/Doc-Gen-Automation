from docxtpl import DocxTemplate

class Documento:
    def __init__(self, nomeArquivo: str):
        self.nomeArquivo = nomeArquivo
        self.documento = DocxTemplate(nomeArquivo)
        self.variaveisDocumento = self.documento.get_undeclared_template_variables()

    def render(self, contexto: dict) -> None:
        self.documento.render(contexto)

    def save(self, caminho: str) -> None:
        self.documento.save(caminho)