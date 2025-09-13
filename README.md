# Projeto de Estudos Django: DVD Rental

Este é um projeto desenvolvido como parte dos estudos em desenvolvimento web com o framework Django. A aplicação se conecta a um banco de dados PostgreSQL (baseado no famoso banco de exemplo `dvdrental`) para realizar operações de visualização, criação, edição e busca de dados.

## Funcionalidades

* **Listagem de Clientes:** Exibição de todos os clientes em uma tabela estilizada com CSS, incluindo status de ativo/inativo.
* **Busca de Clientes:** Funcionalidade de busca dinâmica para filtrar clientes pelo nome.
* **Listagem e Adição de Filmes:** Página para visualizar todos os filmes e um formulário para adicionar novos títulos ao banco.
* **Busca de Atores por Filme:** Uma ferramenta de busca para listar todos os atores que participaram de um determinado filme.
* **Listagem de Categorias:** Visualização de todas as categorias de filmes.
* E outras funcionalidades de visualização e edição de dados.

## Tecnologias Utilizadas

* **Backend:** Python, Django
* **Banco de Dados:** PostgreSQL
* **Frontend:** HTML, CSS

## Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar o projeto no seu ambiente.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/pabloaugussto/seu-novo-nome.git](https://github.com/pabloaugussto/seu-novo-nome.git)
    cd seu-novo-nome
    ```

2.  **Crie e Ative um Ambiente Virtual:**
    ```bash
    python -m venv env
    # No Windows
    env\Scripts\activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Banco de Dados:**
    * Certifique-se de ter o PostgreSQL instalado.
    * Restaure o backup do banco de dados `dvdrental`.
    * Renomeie o arquivo `.env.example` para `.env` e preencha com suas credenciais do banco de dados. (Esta é uma melhoria que podemos fazer depois, por enquanto, edite o `settings.py`).
    * No arquivo `my_ads/settings.py`, configure a seção `DATABASES` com seu usuário e senha do PostgreSQL.

5.  **Execute as Migrações:**
    ```bash
    python manage.py migrate
    ```

6.  **Inicie o Servidor:**
    ```bash
    python manage.py runserver
    ```

A aplicação estará disponível em `http://127.0.0.1:8000/`.
