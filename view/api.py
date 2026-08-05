from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/doc-gen")
def gerar():
    '''
        TODO: estruturar endpoint de post onde ele recebe um json no formato ↓
            {
                "cliente": 2
                "advogado": 1
                "processo": 3
                "modelo_id": idDocumentoTemplate
            }
        
            
        1. Instancia as planilhas em ClienteSheetRepository (BASE CLIENTES),
        ProcessoSheetRepository (BASE PROCESSOS).

        2. Nisso, a API faz a busca das linhas nas planilhas usando 'find', que
        retorna objetos Cliente, Advogado e Processo

        4. Ela baixa o arquivo modelo de 'modelo_id'
        
        5. Injeta as informacoes dos objetos instaciados na etapa 2.
        (usar DocumentoController aqui)

        6. Serializa para base64 o documento já gerado

        7. Apaga o arquivo do disco

        8. Envia o arquivo em base64 no response.body
    '''