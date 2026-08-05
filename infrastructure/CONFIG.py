
# *NOME DO CABEÇALHO DA PLANILHA* : *VARÍAVEL ATRIBUTO EM DATACLASS*

RELACAO_CABECALHO_CLIENTE = {
    "CONTRATANTE (PESSOA FÍSICA)": "contratante_cliente",
    "TIPO"                       : "tipo_pessoa_cliente",
    "CPF"                        : "num_cpf_cliente",
    "CNPJ"                       : "num_cnpj_cliente",
    "Telefone"                   : "telefone_cliente",
    "E-mail"                     : "email_cliente",
    "RG"                         : "num_rg_cliente",
    "Gênero"                     : "genero_cliente",
    "Nacionalidade"              : "nacionalidade_cliente",
    "Estado Civil"               : "estado_civil_cliente",
    "Profissão"                  : "profissao_cliente",  
    "Logradouro"                 : "logradouro_cliente", 
    "Número"                     : "numero_cliente",
    "Complem."                   : "complemento_cliente",
    "Bairro"                     : "bairro_cliente",
    "Cidade"                     : "cidade_cliente",
    "UF"                         : "uf_cliente",
    "CEP"                        : "cep_cliente"
}

RELACAO_CABECALHO_PROCESSO = {
    "CONTRATANTE (CLIENTE)": "contratante_processo",
    "Nome do autor/reu"    : "nome_posicao_processo",
    "Posição do autor/reu" : "posicao_processo",
    "CPF"                  : "numero_cpf_processo",
    "CNPJ"                 : "numero_cnpj_processo",
    "Valor do contrato"    : "valor_do_contrato_processo",
    "Banco"                : "nome_banco_processo",
    "Endereço do banco"    : "endereco_banco_processo",
    "Tipo de ação"         : "tipo_acao_processo"
}