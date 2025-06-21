
# 📌 Task App API - Flask + PostgreSQL
# Andamento

Este projeto foi desenvolvido como objeto de estudo backend.

Uma API simples de gerenciamento de tarefas desenvolvida em Flask, usando SQLAlchemy para integração com PostgreSQL.

---

## ✅ Tecnologias usadas:

- **Python 3.x**
- **Flask**
- **Flask SQLAlchemy**
- **PostgreSQL**
- **dotenv**

---

## ✅ Estrutura do Projeto:

```
task_app/
├── app.py               # Arquivo principal da aplicação Flask
├── db.py                # Conexão com o banco de dados
├── models.py            # Modelos de dados (SQLAlchemy)
├── config.py            # Configurações de ambiente (variáveis do banco)
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente (não versionar)
└── venv/                # Ambiente virtual Python
```

---

## ✅ Configuração do ambiente

### 1. Clone o projeto:

```bash
git clone https://github.com/seu-usuario/task_app.git
cd task_app
```

### 2. Crie o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`:

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=task_app
```

---

## ✅ Model da Tabela `tarefas`

| Campo | Tipo | Descrição |
|--|--|--|
| cod_id | Integer | ID único da tarefa (Primary Key) |
| titulo | String(30) | Título da tarefa |
| descricao | Text | Descrição detalhada |
| status | Boolean | Status da tarefa (True/False) |
| data_criacao | DateTime | Data/hora de criação (auto gerado) |

---

## ✅ Endpoints da API:

### 🔎 GET `/tarefas`
**Descrição:** Lista todas as tarefas existentes.

**Exemplo de resposta:**

```json
{
  "message": "Lista de tarefas obtida com sucesso",
  "tarefas": [
    {
      "cod_id": 1,
      "titulo": "Estudar Flask",
      "descricao": "Fazer um projeto usando Flask e PostgreSQL",
      "status": false,
      "data_criacao": "2025-06-20 14:33:00"
    }
  ]
}
```

---

### ➕ POST `/tarefas`
**Descrição:** Adiciona uma nova tarefa.

**Exemplo de requisição JSON:**

```json
{
  "titulo": "Nova tarefa",
  "descricao": "Descrição da tarefa",
  "status": false
}
```

**Exemplo de resposta:**

```json
{
  "message": "Tarefa adicionada com sucesso",
  "tarefa": {
    "cod_id": 2,
    "titulo": "Nova tarefa",
    "descricao": "Descrição da tarefa",
    "status": false,
    "data_criacao": "2025-06-20 14:40:00"
  }
}
```

---

### 🗑️ DELETE `/tarefas`
**Descrição:** Remove uma tarefa pelo ID.

**Exemplo de requisição JSON:**

```json
{
  "cod_id": 1
}
```

**Exemplo de resposta:**

```json
{
  "message": "Tarefa removida com sucesso",
  "cod_id": 1
}
```

---

## ✅ Como rodar o projeto:

```bash
python3 app.py
```

A API vai rodar em:

```
http://localhost:5000
```

---

## ✅ Próximos passos (sugestões):

- ✅ Adicionar rota PUT para atualizar tarefas  
- ✅ Criar autenticação de usuário  
- ✅ Fazer deploy no Railway / Render  
- ✅ Adicionar testes automatizados  

---