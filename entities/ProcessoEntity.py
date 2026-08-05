from dataclasses import dataclass

@dataclass
class Processo:
    contratante_processo: str
    nome_posicao_processo: str
    posicao_processo: str
    numero_cpf_processo: str
    numero_cnpj_processo: str
    valor_contrato_processo: str
    nome_banco_processo: str
    endereco_banco_processo: str
    tipo_acao_processo: str
