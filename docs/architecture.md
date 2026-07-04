# Arquitetura

# Jornada New Job

---

## Objetivo

O sistema segue arquitetura em camadas para garantir organização, baixo acoplamento e facilidade de manutenção.

Todo fluxo obrigatoriamente deve seguir esta ordem.

```
Usuário

↓

Dashboard (UI)

↓

Components

↓

Services

↓

Repositories

↓

SQLite
```

---

# Dashboard

Responsável apenas por:

- interface
- navegação
- interação

Nunca acessar banco.

Nunca possuir regra de negócio.

---

# Components

São elementos reutilizáveis da interface.

Exemplos:

- Formulários
- Cards
- Dialogs
- Tabelas

Componentes podem receber funções da camada Service.

Nunca acessar Repository.

---

# Services

Camada responsável por:

- validações
- regras
- decisões
- tratamento de dados

Toda lógica deve existir aqui.

---

# Repository

Responsável apenas pela persistência.

Exemplos:

Create

Read

Update

Delete

Nunca validar informações.

Nunca acessar Streamlit.

Nunca possuir lógica de negócio.

---

# Database

Persistência utilizando SQLite.

Toda comunicação ocorre através do SQLAlchemy.

---

# Fluxo Atual

Cadastro

```
Dashboard

↓

Form

↓

Service

↓

Repository

↓

SQLite
```

---

Listagem

```
Dashboard

↓

Service

↓

Repository

↓

SQLite
```

---

Exclusão

```
Dashboard

↓

Confirmação

↓

Service

↓

Repository

↓

SQLite
```

---

Edição (Feature 002)

```
Dashboard

↓

Form preenchido

↓

Service

↓

Repository

↓

SQLite
```

---

Sincronização Gmail (Sprint futura)

```
Dashboard

↓

Gmail Sync

↓

OAuth

↓

Reader

↓

Filters

↓

Extractor

↓

Service

↓

Repository

↓

SQLite
```

---

# Estrutura

```
dashboard/

components/

services/

repositories/

database/

gmail/

config/

utils/

tests/

docs/
```

---

# Princípios

Baixo acoplamento.

Alta coesão.

Responsabilidade única.

Reutilização.

Código simples.
