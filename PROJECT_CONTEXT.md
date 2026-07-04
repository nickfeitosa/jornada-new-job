# Jornada New Job

Versão: 1.0
Status: Em Desenvolvimento

---

# Objetivo

O Jornada New Job é um sistema desenvolvido em Python para gerenciamento de processos seletivos.

Seu principal diferencial será a sincronização automática de e-mails do Gmail, permitindo atualizar candidaturas automaticamente através da leitura e interpretação de mensagens.

O projeto possui dois objetivos:

- Portfólio profissional
- Produto funcional

O CRUD existe apenas como base para suportar as funcionalidades futuras.

---

# Stack

Backend

- Python 3.13+
- SQLAlchemy
- SQLite

Frontend

- Streamlit

Versionamento

- Git
- GitHub

Integrações futuras

- Gmail API
- Google OAuth
- IA para classificação automática

---

# Arquitetura

Todo acesso ao banco obrigatoriamente segue a arquitetura abaixo.

```

UI (Dashboard)

↓

Components

↓

Service Layer

↓

Repository

↓

SQLite

```

É proibido acessar o banco diretamente pela UI.

Toda regra de negócio deve permanecer na camada Service.

Toda persistência deve permanecer na camada Repository.

---

# Estrutura

```

Jornada-New-Job/

dashboard/

components/

database/

repositories/

services/

gmail/

config/

utils/

logs/

tests/

docs/

PROJECT_CONTEXT.md

TECH_LEAD.md

README.md

```

---

# Convenções

Sempre utilizar:

Service

↓

Repository

↓

Database

Nunca:

Dashboard

↓

SQLite

---

# Feature Status

## Sprint 1

✔ Estrutura inicial

✔ Banco SQLite

✔ Cadastro

✔ Listagem

---

Sprint 2

✔ Componentização

✔ Exclusão

✔ Edição

Sprint concluída.

---

## Sprint 3

Planejado

Integração Gmail

---

## Sprint 4

Dashboard

KPIs

Indicadores

Gráficos

---

## Sprint 5

Inteligência Artificial

Extração automática

Classificação

Insights

---

# Regras

Todo código deve possuir responsabilidade única.

Arquivos pequenos.

Funções pequenas.

Comentários apenas quando agregarem valor.

---

# Fluxo de Desenvolvimento

Feature

↓

Arquivos completos

↓

Copiar

↓

Executar

↓

Testar

↓

Commit

↓

Push

↓

Atualizar documentação

---

# Objetivo Permanente

Sempre avaliar:

"A alteração aproxima o projeto da sincronização automática do Gmail?"

Se sim:

Implementar.

Se não:

Adiar.

---

# GitHub Oficial

https://github.com/nickfeitosa/jornada-new-job

---

# Branch Principal

main

---

Sprint Atual

Sprint 3

Integração Gmail

# Tech Lead

Toda decisão técnica deve seguir o documento TECH_LEAD.md.
