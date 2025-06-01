# TaskFlow

Um sistema de gerenciamento de tarefas e projetos desenvolvido com Django e Bootstrap.

## Configuração

1. Instale o Python e o PostgreSQL.
2. Clone o repo: `git clone <repo-url>`
3. Crie um ambiente virtual: `python -m venv venv`
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure o banco de dados: `createdb taskflow_db`
6. Execute as migrações: `python manage.py migrate`
7. Inicie o servidor: `python manage.py runserver`

## Features

- CRUD para projetos e tarefas.
- Autenticação e autorização de usuários.
- Interface responsiva com Bootstrap.
- Filtros e paginação para as tarefas.

## Team

- @Phoenix7290 : Frontend (HTML, CSS, Bootstrap, JavaScript)
- Hishow: Backend (Django, PostgreSQL)
