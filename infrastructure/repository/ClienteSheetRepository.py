from infrastructure.repository.ISheetRepository import ISheetRepository
from entities.ClienteEntity import Cliente
from utils.mergeDictionaries import mergeDictionaries
from infrastructure.CONFIG import RELACAO_CABECALHO_CLIENTE

class ClienteSheetRepository(ISheetRepository):
    def __init__(self, googleClientAuth, sheetId: str):
        self.sheet = googleClientAuth.open_by_key(sheetId).sheet1

    def find(self, line: int) -> Cliente:
        keys = self.sheet.row_values(self.sheet.find("CONTRATANTE (PESSOA FÍSICA)", in_column=1).row)
        values = self.sheet.row_values(line)

        # gspread omite as células vazias no fim da linha
        values += [""] * (len(keys) - len(values))

        # Nome coluna : valor coluna
        dictProcesso = dict(zip(keys, values))
        # Nome var : valor coluna
        objectProcessDict = mergeDictionaries(RELACAO_CABECALHO_CLIENTE, dictProcesso)

        return Cliente(**objectProcessDict)