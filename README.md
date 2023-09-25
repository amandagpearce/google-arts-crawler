# Google Image Service

Projeto criado como componente D do MVP da disciplina de Back-end avançado do curso de pós-graduação em Desenvolvimento Full Stack da PUC-Rio. 

## O que é?
API Rest que utiliza a Google's Programmable Search Engine da API Custom Search para buscar uma imagem da obra de arte referenciada pelo filme ou série, de acordo com o cadastro realizado no [front-end](https://github.com/amandagpearce/got-that-ref#send-a-reference).

## Arquivo .env 
Primeiramente é necessário gerar uma API Key como descrito na [documentação](https://developers.google.com/custom-search/v1/introduction?hl=pt-br). Com a API Key e a search engine ID criadas, crie um arquivo `.env` que irá conter essas informações, como no exemplo abaixo:

`
PROGRAMMABLE_SEARCH_ENGINE_API_KEY="suakey"
SEARCH_ENGINE_ID="suaid"
`
- Substitua `suakey` e `suaid` pelos seus dados. Após a criação da API Key, os dados podem ser conferidos e obtidos no [painel da Google](https://programmablesearchengine.google.com/controlpanel/all).

### Instalação com Docker
1. Clone o projeto
2. Cole na raiz do projeto o arquivo `.env` preenchido, como descrito na seção anterior 
3. Na raiz do projeto, rode o seguinte comando para criar a imagem:
```bash
  docker build -t g-arts-service .
```
4. Rode a imagem criada:
```bash
  docker run -p 9000:9000 g-arts-service
```
5. Acesse a documentação no Swagger em `http://localhost:9000/doc`

### Instalação sem Docker
1. Clone o projeto
2. Cole na raiz do projeto o arquivo `.env` preenchido, como descrito na seção anterior 
3. Na raiz do projeto, rode o seguinte comando:
```bash
  flask run --host 0.0.0.0 --port 9000
```
4. Acesse a documentação no Swagger em `http://localhost:9000/doc`

## Banco de dados 
A aplicação gerencia um banco de dados sqlite com a seguinte tabela:

| Field Name    | Data Type  | Description                  |
| ------------- | ---------- | ---------------------------- |
| id            | Integer    | Primary Key                   |
| artworkTitle  | String     | Título da Obra de Arte       |
| imageUrl      | String     | URL da Imagem da Obra de Arte |
| artist        | String     | Nome do Artista              |

- imageUrl é o que é retornado da pesquisa no Google Images.

## Licensa e critérios de busca de imagem 
A busca de imagens utiliza a licensa Creative Commons como definido nos argumentos de busca do script:
`
    search_params = {
        "q": query,
        "num": 1,  # Number of images to fetch
        "safe": "high",  # Safety level (options: high, medium, off)
        "fileType": "jpg|png",  # Limit search to JPEG and PNG files
        "size": "large",  # Filter for large images
        "rights": (  # Creative Commons licenses
            "cc_publicdomain|"
            "cc_attribute|"
            "cc_sharealike|"
            "cc_noncommercial|"
            "cc_nonderived"
        ),
    }
`
