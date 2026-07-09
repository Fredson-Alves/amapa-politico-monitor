# Arquitetura do Sistema

# Amapá Político Monitor

Versão: 1.0

---

# Visão Geral

O **Amapá Político Monitor** é um sistema baseado em Inteligência Artificial desenvolvido para automatizar o monitoramento de notícias políticas relacionadas ao Estado do Amapá.

O projeto utiliza o framework **CrewAI** para orquestrar agentes especializados, responsáveis por coletar, verificar, classificar e organizar informações provenientes de fontes públicas (OSINT - Open Source Intelligence).

O objetivo é disponibilizar informações estruturadas para apoiar atividades de acompanhamento institucional.

---

# Objetivos da Arquitetura

A arquitetura foi concebida seguindo cinco princípios:

- Modularidade
- Baixo acoplamento
- Alta coesão
- Facilidade de manutenção
- Facilidade de expansão

Cada componente possui uma responsabilidade específica.

---

# Arquitetura Geral

```text
                         Internet
                              │
                              │
                              ▼
                 Ferramenta de Pesquisa
                              │
                              ▼
                 Pesquisador OSINT
                              │
                              ▼
               Verificador de Fontes
                              │
                              ▼
        Classificador Político-Institucional
                              │
                              ▼
          Redator do Relatório Executivo
                              │
                              ▼
                 Relatório Final (Markdown)
```

---

# Organização do Projeto

```text
src/
└── amapa_politico_monitor/
    │
    ├── agents/
    ├── crews/
    ├── tasks/
    ├── tools/
    ├── services/
    ├── models/
    ├── utils/
    │
    ├── settings.py
    ├── logger.py
    ├── crew.py
    └── main.py
```

Cada diretório possui uma responsabilidade bem definida.

---

# Camadas da Aplicação

## 1. Camada de Entrada

Arquivo:

```
main.py
```

Responsável por:

- iniciar a aplicação;
- carregar configurações;
- iniciar a Crew;
- registrar logs;
- tratar exceções.

---

## 2. Camada de Orquestração

Arquivo:

```
crews/political_monitor_crew.py
```

Responsável por:

- criar os agentes;
- criar as tarefas;
- montar a Crew;
- definir a ordem de execução.

---

## 3. Camada de Agentes

Diretório:

```
agents/
```

Cada agente representa um especialista.

### Pesquisador OSINT

Responsável pela coleta de informações.

---

### Verificador de Fontes

Valida:

- links;
- duplicidades;
- consistência.

---

### Classificador

Organiza as notícias por categoria.

---

### Redator

Produz o relatório final.

---

# Camada de Ferramentas

Diretório

```
tools/
```

Contém ferramentas utilizadas pelos agentes.

Exemplo:

```
Pesquisa Web
```

No futuro poderá conter:

- RSS
- APIs
- Scrapers
- Leitores de PDF
- Banco de Dados

---

# Camada de Serviços

Diretório

```
services/
```

Reservado para integrações externas.

Exemplos futuros:

- Portal da Transparência
- Diário Oficial
- API do Senado
- API da Câmara
- APIs de notícias

---

# Camada de Modelos

Diretório

```
models/
```

Destinado à representação estruturada dos dados da aplicação.

Exemplos futuros:

- Notícia
- Pessoa
- Órgão
- Município
- Fonte

---

# Camada Utilitária

Diretório

```
utils/
```

Funções reutilizáveis.

Exemplos:

- normalização de texto;
- datas;
- validações;
- exportações.

---

# Configurações

Arquivo

```
settings.py
```

Centraliza:

- variáveis de ambiente;
- caminhos;
- modelos de IA;
- diretórios.

---

# Sistema de Logs

Arquivo

```
logger.py
```

Responsável pelo registro de:

- inicialização;
- execução;
- erros;
- exceções.

Os logs ficam em:

```
logs/
```

---

# Fluxo de Execução

```text
main.py

↓

PoliticalMonitorCrew

↓

Pesquisador

↓

Verificador

↓

Classificador

↓

Redator

↓

Relatório Final
```

---

# Fluxo de Dados

```text
Internet

↓

Pesquisa

↓

Lista de Notícias

↓

Validação

↓

Classificação

↓

Relatório

↓

Arquivo Markdown
```

---

# Padrões de Projeto Utilizados

O projeto utiliza conceitos inspirados em:

- Factory
- Separation of Concerns
- Modular Architecture
- Single Responsibility Principle (SRP)
- Dependency Organization

---

# Escalabilidade

A arquitetura foi preparada para permitir a inclusão de novos componentes sem alterações significativas na estrutura existente.

Exemplos de evolução:

- novos agentes especializados;
- novas ferramentas de busca;
- integração com APIs institucionais;
- persistência em banco de dados;
- geração de dashboards;
- notificações automáticas;
- exportação para PDF, HTML e JSON.

---

# Segurança

O sistema foi projetado para utilizar:

- variáveis de ambiente para armazenamento de credenciais;
- arquivos `.env` não versionados;
- logs separados da aplicação;
- segregação entre código e configuração.

---

# Considerações Finais

Esta arquitetura privilegia simplicidade, organização e possibilidade de crescimento incremental.

O projeto foi estruturado para evoluir de um monitorador de notícias para uma plataforma de monitoramento de fontes abertas, preservando a modularidade e facilitando futuras integrações.
