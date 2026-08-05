from dataclasses import dataclass

@dataclass
class Advogado:
    nome_advogado: str
    numero_oab: str
    estado_oab: str
    endereco_escritorio: str