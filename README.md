# Projeto FastAPI com Docker Compose

Este é um projeto básico FastAPI com suporte a Docker Compose, incluindo contêineres para o aplicativo FastAPI e um banco de dados PostgreSQL. O projeto consiste em uma API para gerenciar times, jogadores e jogos, além de um script interativo (`cmd.py`) para listar times, jogos e jogadores.

## Estrutura do Projeto

```plaintext
projetoAV2Docker/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── cmd.py
│   ├── crud.py
│   ├── models.py
│   └── database.py  
│   
├── data/
│
├── docker/
│   ├── db/
│   │   ├── Dockerfile
│   │   └── create_tables.sql
│   │
│   └── app/
│       └── Dockerfile
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

- **app/**: Contém os arquivos principais do seu aplicativo.
  - **main.py**: O ponto de entrada principal para o aplicativo FastAPI.
  - **cmd.py**: Script interativo.
  - **crud.py**: Funções de acesso ao banco de dados.
  - **database.py**: Configuração do banco de dados.
  - **models.py**: Definição das classes de modelo SQLAlchemy.

- **data/**: Diretório para armazenar dados do aplicativo.

- **docker/**: Diretório que contém os arquivos relacionados ao Docker.
  - **db/**: Configurações para o contêiner do banco de dados.
    - **Dockerfile**: Configurações para construir a imagem do contêiner do banco de dados.
    - **create_tables.sql**: Script SQL para criar tabelas.
  - **app/**: Configurações para o contêiner do aplicativo.
    - **Dockerfile**: Configurações para construir a imagem do contêiner do aplicativo.

- **docker-compose.yml**: Arquivo de configuração do Docker Compose.

## Como Executar o Projeto

### Pré-requisitos

- Docker
- Docker Compose

### Passos

1. Execute o aplicativo e o banco de dados:

   ```bash
   docker-compose up --build
   ```

   Isso criará e iniciará os contêineres conforme especificado no arquivo `docker-compose.yml`.

2. Abra o navegador e acesse a documentação da API:

   [http://localhost:8000/docs](http://localhost:8000/docs)

3. Execute o script interativo:

   ```
   docker-compose exec app bash
   
   python cmd.py
   ```

   Siga as instruções no script interativo para listar times, jogos e jogadores.

## Acesso ao Banco de Dados

Para acessar o banco de dados diretamente, você pode usar o seguinte comando:

```
docker-compose exec app bash
psql -h db -U user -d db
```

Isso abrirá um shell interativo do PostgreSQL onde você pode executar comandos SQL. Caso queira consultar os dados da tabela de times.

```
\dt
SELECT * FROM teams;
```

Lembre-se de que é necessário ter o cliente PostgreSQL instalado localmente para usar o comando `psql`.


## Observações

- Certifique-se de que as portas 8000 (aplicativo FastAPI) e 5432 (PostgreSQL) não estejam sendo utilizadas por outros serviços em sua máquina.

- Este projeto utiliza o Docker Compose para facilitar a execução do aplicativo e do banco de dados. Certifique-se de ter o Docker Compose instalado.

- Os dados do banco de dados PostgreSQL são persistentes e são armazenados no diretório `data/db`. Isso significa que você pode parar e reiniciar os contêineres sem perder os dados.

