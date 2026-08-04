from docxtpl import DocxTemplate

class DocxEntity:
    def __init__(self, nomeArquivo: str):
        self.nomeArquivo = nomeArquivo
        self.documento = DocxTemplate(nomeArquivo)
        self.variaveisDocumento = self.documento.get_undeclared_template_variables()

    def geraModelo(self, contexto) -> None:
        self.documento.render(contexto)
        self.documento.save(contexto.contratante)