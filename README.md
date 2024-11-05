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
![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
```
- Python 3.12+
- Flask e SQLAlchemy (instaladas via `requirements.txt`)
```
## Instalação

1. Clone este repositório:
```
   git clone https://github.com/Alexandre17araujo/magpy.git
   cd magpy
```

## Crie e ative um ambiente virtual (opcional, mas recomendado):
```
	python -m venv venv
	source venv/bin/activate  # Linux
	venv\Scripts\activate     # Windows
```

## Instale as dependencias
```
	pip install -r requirements.txt
```

## Execute a aplicação 
![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

```	
    python3.12 main.py 
```


## Uso das Endpoints

### 1. Criar um Projeto com "POST"
```
Endpoint: https://link_da_sua_api/projects
Método: POST
Exemplo de Request

{
  "name": "meu_projeto",
  "packages": [
    {"name": "requests", "version": "2.26.0"},
    {"name": "flask"}
  ]
}

```
#### Resposta de Sucesso (201):

```
	{
  	"message": "Project created successfully"
	}
```

### 2. Listando Projetos, com "GET".

```
https://link_da_sua_api/projects/nome_projeto
Método: GET
Exemplo de Request:

	GET /projects/nome_projeto
```

#### Resposta de Sucesso (200):
```
{
  	"name": "nome_projeto",
	"packages": [
    {"name": "requests", "version": "2.26.0"},
    {"name": "flask", "version": "2.0.2"}
]
}
```

### 3. Excluir um Projeto
```
Endpoint: https://link_da_sua_api/projects/nome_projeto
Método: DELETE

Exemplo de Request:

DELETE /projects/nome_projeto
```

#### Resposta de Sucesso (200):
```
{
  "message": "Project deleted"
}
```

### Tratamento de Erros
	400: Parâmetros inválidos ou projeto/pacote inexistente no PyPI.
	404: Projeto não encontrado.
	500: Erro interno do servidor.


### Testando com o Postman
	Abra o Postman.
	Configure as requisições conforme os endpoints e exemplos acima.
	Verifique o banco de dados para confirmar que as informações estão sendo armazenadas e deletadas corretamente.

### Documentação

- [Python](https://docs.python.org/pt-br/3.12/library/index.html)
- [Flask](https://flask-ptbr.readthedocs.io/en/latest/)
- [flask Restful](https://flask-restful.readthedocs.io/en/latest/)
- [Requests](https://requests.readthedocs.io/projects/pt/pt-br/latest/user/quickstart.html)
- [OS](https://docs.python.org/pt-br/3/library/os.html)
- [SQlAchemy](https://docs.sqlalchemy.org/en/20/)