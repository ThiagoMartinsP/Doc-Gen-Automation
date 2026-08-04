from dataclasses import dataclass

@dataclass
class Cliente:
    contratante: str
    tipo_pessoa: str
    cpf: str
    cnpj: str
    telefone: str
    email: str
    rg: str
    genero: str
    nacionalidade: str
    estado_civil: str
    profissao: str
    logradouro: str
    numero: int
    complemento: str
    bairro: str
    cidade: str
    uf: str
    cep: str