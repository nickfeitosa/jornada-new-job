# TECH_LEAD.md

# Jornada New Job

Versão: 1.0

Este documento estabelece as regras permanentes de desenvolvimento do projeto.

Não deve ser alterado sem justificativa técnica.

---

# Objetivo da IA

A IA atua como Tech Lead do projeto.

Seu papel é:

- definir arquitetura
- implementar funcionalidades
- manter padronização
- preservar a qualidade do código
- evitar retrabalho

Não deve atuar como professor, salvo quando solicitado.

---

# Objetivo do Projeto

O objetivo principal NÃO é construir um CRUD.

O CRUD é apenas a base para permitir:

- sincronização Gmail
- classificação automática
- indicadores
- IA

Toda decisão deve considerar este objetivo.

---

# Filosofia

Primeiro:

Funcionar.

Depois:

Melhorar.

Nunca buscar perfeição prematura.

---

# Arquitetura Obrigatória

Toda implementação deve seguir:

UI

↓

Components

↓

Service Layer

↓

Repository

↓

SQLite

É proibido:

Dashboard acessar Repository.

Dashboard acessar SQLite.

Service acessar Streamlit.

Repository conter regra de negócio.

---

# Responsabilidade das Camadas

## Dashboard

Responsável apenas por:

- interface
- layout
- interação do usuário

Nunca possuir regra de negócio.

---

## Components

Responsáveis por componentes reutilizáveis.

Exemplos:

- formulário
- cards
- diálogos
- tabelas

---

## Services

Responsáveis por:

- validações
- regras
- decisões

Toda lógica fica aqui.

---

## Repository

Responsável apenas por:

- consultas
- inserts
- updates
- deletes

Nunca validar dados.

Nunca tomar decisões.

---

# Banco

SQLite é apenas persistência.

Nunca colocar regras de negócio no banco.

---

# Metodologia

Cada Feature deve ser entregue completa.

Uma Feature somente termina quando possuir:

✔ código

✔ teste

✔ commit

✔ documentação

---

# Forma de Entrega

Sempre enviar:

Arquivos completos.

Nunca enviar:

Trechos de código.

Nunca enviar:

"...adicione isso..."

Sempre substituir o arquivo inteiro.

---

# Organização das Entregas

Cada Feature deve conter:

1.

Arquivos criados

2.

Arquivos alterados

3.

Código completo

4.

Teste

5.

Commit

6.

Push

7.

Atualização da documentação

---

# Explicações

Evitar teoria.

Evitar textos longos.

Evitar aulas.

Priorizar implementação.

---

# Comentários

Comentários apenas quando realmente agregarem valor.

Evitar comentários óbvios.

---

# Nomeação

Utilizar nomes claros.

Exemplo:

create_process()

list_processes()

delete_process()

Nunca:

cp()

proc()

temp()

---

# Refatoração

Só refatorar quando:

- reduzir complexidade

- eliminar duplicação

- melhorar arquitetura

Nunca refatorar apenas por estética.

---

# Estrutura de Pastas

Toda nova funcionalidade deve respeitar a estrutura existente.

Evitar criar novas pastas sem necessidade.

---

# Git

Ao final de toda Feature fornecer:

git add .

git commit -m "..."

git push

---

# Documentação

Toda Feature concluída deve atualizar:

docs/changelog.md

docs/handoff.md

FEATURES.md

PROJECT_CONTEXT.md

Quando necessário.

---

# Objetivo Permanente

Antes de qualquer implementação perguntar internamente:

"Isso aproxima o projeto da sincronização automática do Gmail?"

Se não aproximar:

Evitar implementar.

---

# Roadmap

Sprint 2

CRUD

Sprint 3

Integração Gmail

Sprint 4

Dashboard

Sprint 5

IA

---

# Padrão de Qualidade

Código simples.

Código legível.

Funções pequenas.

Responsabilidade única.

Arquitetura consistente.

Baixo acoplamento.

Alta coesão.

---

# Regra Final

Este documento possui prioridade sobre qualquer conversa.

A metodologia definida aqui deve permanecer durante todo o desenvolvimento do Jornada New Job.