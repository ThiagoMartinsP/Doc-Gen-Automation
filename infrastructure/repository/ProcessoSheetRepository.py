from ISheetRepository import ISheetRepository
from entities.ProcessoEntity import Processo
from infrastructure.CONFIG import RELACAO_CABECALHO_PROCESSO
from utils.mergeDictionaries import mergeDictionaries

class ProcessoSheetRepository(ISheetRepository):
    def __init__(self, googleClientAuth, sheetId: str):
        self.sheet = googleClientAuth.open_by_key(sheetId).sheet1

    def find(self, line: int) -> Processo:
        keys = self.sheet.row_values(self.sheet.find("CONTRATANTE (CLIENTE)", in_column=1).row)
        values = self.sheet.row_values(line)

        # Nome coluna : valor coluna
        dictProcesso = dict(zip(keys, values))
        # Nome var : valor coluna
        objectProcessDict = swapDictionaries(RELACAO_CABECALHO_PROCESSO, dictProcesso)

        return Processo(**objectProcessDict)