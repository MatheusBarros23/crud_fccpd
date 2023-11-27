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

**1. Parando e Reiniciando o Container:**

Após a execução do primeiro cenário, vamos parar o contêiner e reiniciar só o DB para simular um segundo cenário de execução. 
Dê o STOP nos containers no Docker Desktop e utilize o seguinte comando:

```bash
# Reinicie o contêiner do banco de dados
docker-compose restart db
```

**2. Abra o Conectando-se ao Banco de Dados:**

```bash
docker-compose exec db bash

# Conecte-se ao banco de dados PostgreSQL usando psql
psql -U user -d db
```

Insira a senha quando solicitado.
```bash
password
```

**3. Realizando Operações CRUD:**

Agora, dentro do ambiente interativo do PostgreSQL, realize as operações CRUD:

**3.1. Inserir Dados:**

```sql
INSERT INTO players (name, team_id) VALUES ('novoJogador', 2);
```

**3.2. Atualizar Dados:**

```sql
UPDATE players SET name = 'nomeAlterado' WHERE name = 'Xena Souza';
```

**4. Verificando as Alterações:**

Para verificar as alterações, você pode realizar uma consulta simples:

```sql
SELECT * FROM players;
```

Isso mostrará os dados atualizados na tabela de jogadores.

**5. Encerrando o Contêiner:**

Quando terminar, você pode sair do ambiente interativo do PostgreSQL e parar o contêiner:

```bash
# Sair do shell interativo do contêiner
exit

# Parar o contêiner do banco de dados
docker-compose down
```

Esses comandos encerrarão o contêiner e encerrarão a simulação do segundo cenário de execução. Certifique-se de que suas operações CRUD foram concluídas antes de encerrar o contêiner.

## Observações

- Certifique-se de que as portas 8000 (aplicativo FastAPI) e 5432 (PostgreSQL) não estejam sendo utilizadas por outros serviços em sua máquina.

- Este projeto utiliza o Docker Compose para facilitar a execução do aplicativo e do banco de dados. Certifique-se de ter o Docker Compose instalado.

- Os dados do banco de dados PostgreSQL são persistentes e são armazenados no diretório `data/db`. Isso significa que você pode parar e reiniciar os contêineres sem perder os dados.

