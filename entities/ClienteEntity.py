from dataclasses import dataclass

@dataclass
class Cliente:
    contratante_cliente: str
    tipo_pessoa_cliente: str
    num_cpf_cliente: str
    num_cnpj_cliente: str
    telefone_cliente: str
    email_cliente: str
    num_rg_cliente: str
    genero_cliente: str
    nacionalidade_cliente: str
    estado_civil_cliente: str
    profissao_cliente: str
    logradouro_cliente: str
    numero_cliente: int
    complemento_cliente: str
    bairro_cliente: str
    cidade_cliente: str
    uf_cliente: str
    cep_cliente: str