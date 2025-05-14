# SGHSS – Sistema de Gestão Hospitalar e de Serviços de Saúde (Back-end)

Este projeto é o back-end de uma aplicação acadêmica que simula um sistema de gestão hospitalar. Ele foi desenvolvido como parte do Projeto Multidisciplinar do curso de Análise e Desenvolvimento de Sistemas – UNINTER (ênfase em Desenvolvimento Back-end).

---

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- Flask
- Flask-JWT-Extended
- SQLAlchemy
- SQLite
- Bcrypt
- Pytest (para testes)

---

## 🚀 Como Executar o Projeto Localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/OdimarDev/sghss-backend.git
cd sghss-backend
````

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
venv\Scripts\activate   # No Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**

```bash
python app.py
```

O servidor estará rodando em:
📍 `http://127.0.0.1:5000`

---

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Tokens)**. Para acessar rotas protegidas, é necessário:

1. Cadastrar um usuário (`/signup`)
2. Fazer login (`/login`) e receber o token
3. Enviar o token no cabeçalho de cada requisição protegida:

```
Authorization: Bearer SEU_TOKEN_JWT
```

---

## 📚 Documentação da API

### ✅ POST /signup

Cadastra um novo usuário.

```json
Requisição:
{
  "email": "usuario@teste.com",
  "senha": "123456"
}

Resposta (201 CREATED):
{
  "mensagem": "Usuario criado com sucesso"
}
```

---

### ✅ POST /login

Realiza o login e retorna um token JWT.

```json
Requisição:
{
  "email": "usuario@teste.com",
  "senha": "123456"
}

Resposta (200 OK):
{
  "token": "eyJhbGciOiJIUzI1NiIs..."
}
```

---

### ✅ POST /pacientes

Cadastra um novo paciente. (🔒 Token necessário)

```json
Requisição:
{
  "nome": "João da Silva",
  "cpf": "12345678900"
}

Resposta (200 OK):
{
  "mensagem": "Paciente cadastrado com sucesso"
}
```

---

### ✅ GET /pacientes

Lista todos os pacientes cadastrados. (🔒 Token necessário)

```json
Resposta:
[
  {
    "id": 1,
    "nome": "João da Silva",
    "cpf": "12345678900"
  }
]
```

---

### ✅ POST /medicos

Cadastra um novo médico. (🔒 Token necessário)

```json
Requisição:
{
  "nome": "Dra. Ana",
  "especialidade": "Cardiologia"
}

Resposta:
{
  "mensagem": "Médico cadastrado com sucesso"
}
```

---

### ✅ POST /consultas

Agenda uma nova consulta. (🔒 Token necessário)

```json
Requisição:
{
  "paciente_id": 1,
  "medico_id": 1,
  "data": "2025-05-13"
}

Resposta:
{
  "mensagem": "Consulta agendada com sucesso"
}
```

---

### ✅ GET /medicos

Lista todos os médicos cadastrados. (🔒 Token necessário)

```json
Requisição:
{
  "paciente_id": 1,
  "medico_id": 1,
  "data": "2025-05-13"
}

Resposta:
{
  "mensagem": "Consulta agendada com sucesso"
}

```

#### ✅ GET /medicos

Lista todos os médicos cadastrados. (🔒 Token necessário)

```json
Resposta:
[
  {
    "id": 1,
    "nome": "Dr. João",
    "especialidade": "Cardiologia"
  }
]

```

#### Observação:

Esta API, por se tratar de um projeto acadêmico com escopo limitado, implementa apenas operações de criação (POST) e consulta (GET). As operações de edição (PUT) e exclusão (DELETE) podem ser adicionadas em versões futuras, conforme evolução da proposta.

```

## ✅ Estrutura do Projeto

```

📦 sghss-backend
├── app.py
├── models.py
├── auth.py
├── requirements.txt
├── readme.md
├── test_app.py (opcional para pytest)
├── database.db (gerado automaticamente)
```

---

## 📄 Licença

Este projeto é de uso acadêmico e foi desenvolvido para fins educacionais como parte da disciplina Projeto Multidisciplinar da UNINTER.

```
