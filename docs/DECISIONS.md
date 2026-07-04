# DECISIONS

Registro permanente das decisões arquiteturais.

---

## DEC-001

Arquitetura em camadas.

Motivo

Separação de responsabilidades.

---

## DEC-002

Toda regra de negócio permanece na camada Service.

Motivo

Evitar acoplamento com a interface.

---

## DEC-003

Repository acessa exclusivamente o banco.

Motivo

Facilitar futura migração para PostgreSQL.

---

## DEC-004

CRUD é apenas suporte para funcionalidades futuras.

Motivo

O objetivo principal é a sincronização automática do Gmail.

---

## DEC-005

Toda Feature deve ser entregue completa.

Motivo

Evitar código incompleto.

---

## DEC-006

Documentação obrigatória.

Arquivos

PROJECT_CONTEXT.md

TECH_LEAD.md

docs/

Motivo

Evitar reconstrução de contexto em novas conversas.

---

## DEC-007

O GitHub é a fonte oficial do projeto.

Repositório

https://github.com/nickfeitosa/jornada-new-job
---

## DEC-008

Toda Feature somente será considerada concluída após:

- Código implementado
- Testes executados
- Commit realizado
- Push realizado
- Documentação atualizada
- Backlog atualizado (quando aplicável)

Motivo

Garantir rastreabilidade completa da evolução do projeto.