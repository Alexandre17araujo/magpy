# MagPy API

MagPy é uma API RESTful desenvolvida em Python, utilizando Flask e SQLAlchemy, para gerenciar uma coleção de projetos e pacotes associados, com integração ao PyPI. Este projeto permite a criação, listagem e remoção de projetos e pacotes.

## Funcionalidades

- **Criar um Projeto**: Crie um projeto com uma lista de pacotes, validando cada pacote no PyPI.
- **Listar um Projeto**: Consulte um projeto específico e veja a lista de pacotes com nome e versão.
- **Excluir um Projeto**: Exclua um projeto e todos os pacotes associados a ele.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework para criação de APIs REST.
- **SQLAlchemy**: ORM para gerenciamento de banco de dados.
- **SQLite**: Banco de dados utilizado para armazenamento local.

## Estrutura do Projeto

- `main.py`: Contém a definição dos endpoints e a lógica principal da API.
- `models.py`: Define os modelos de banco de dados `Project` e `Package`.
- `README.md`: Documentação do projeto.
- `requirements.txt`: Lista de dependências do projeto.

## Pré-requisitos

- Python 3.7+
- Flask e SQLAlchemy (instaladas via `requirements.txt`)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/magpy-api.git
   cd magpy-api


Crie e ative um ambiente virtual (opcional, mas recomendado):
	python -m venv venv
	source venv/bin/activate  # Linux
	venv\Scripts\activate     # Windows

Instale as dependencias
	pip install -r requirements.txt

Execute a aplicação
	python3.11 main.py

Endpoints da API
1. Criar um Projeto
Endpoint: /projects
Método: POST

Exemplo de Request (JSON):

	{
  "name": "meu_projeto",
  "packages": [
    {"name": "requests", "version": "2.26.0"},
    {"name": "flask"}
  ]
}


Resposta de Sucesso (201):

	{
  	"message": "Project created successfully"
	}

2. Listar um Projeto
Endpoint: /projects/<project_name>
Método: GET
Exemplo de Request:

	GET /projects/meu_projeto



Resposta de Sucesso (200):

{
  	"name": "meu_projeto",
	"packages": [
    {"name": "requests", "version": "2.26.0"},
    {"name": "flask", "version": "2.0.2"}
]
}


3. Excluir um Projeto
Endpoint: /projects/<project_name>
Método: DELETE

Exemplo de Request:

DELETE /projects/meu_projeto


Resposta de Sucesso (200):

{
  "message": "Project deleted"
}


Tratamento de Erros
	400: Parâmetros inválidos ou projeto/pacote inexistente no PyPI.
	404: Projeto não encontrado.
	500: Erro interno do servidor.


Testando com o Postman
	Abra o Postman.
	Configure as requisições conforme os endpoints e exemplos acima.
	Verifique o banco de dados para confirmar que as informações estão sendo armazenadas corretamente.
