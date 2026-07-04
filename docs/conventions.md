# Convenções

# Jornada New Job

---

## Nomeação

Arquivos

snake_case.py

Funções

snake_case()

Classes

PascalCase

Constantes

UPPER_CASE

---

## Organização

Uma responsabilidade por função.

Uma responsabilidade por arquivo quando possível.

---

## Componentes

Todo componente Streamlit deve iniciar com:

show_

Exemplo

show_process_form()

show_process_card()

---

## Services

Toda regra de negócio fica nesta camada.

Nunca acessar Streamlit.

---

## Repository

Toda consulta ao banco.

Nunca validar dados.

---

## Comentários

Evitar comentários desnecessários.

Preferir código autoexplicativo.

---

## Tipagem

Sempre utilizar type hints.

Exemplo

company: str

process_id: int

---

## Imports

Bibliotecas padrão

↓

Bibliotecas externas

↓

Projeto

Separados por linha em branco.

---

## Git

Commits curtos.

Formato

feat:

fix:

docs:

refactor:

test:

chore:

Exemplos

feat: implementa edição de processos

fix: corrige atualização de status

docs: atualiza arquitetura

---

## Feature

Uma Feature somente termina quando possuir

Código

Teste

Commit

Push

Documentação atualizada

---

## Código

Preferir:

Legibilidade

Ao invés de:

Criatividade.
