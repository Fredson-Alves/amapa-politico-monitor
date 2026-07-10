# Amapá Político Monitor

Sistema inteligente para monitoramento de notícias políticas públicas do Estado do Amapá, desenvolvido com Python, CrewAI e princípios de OSINT.

Versão atual: v1.0.0-academic (Release Candidate)

---

## Objetivo Geral

O Amapá Político Monitor tem como finalidade apoiar o acompanhamento de informações públicas relacionadas ao cenário político e institucional do Amapá, organizando notícias em um fluxo estruturado de coleta, análise e geração de relatórios.

O projeto foi concebido para uso acadêmico, institucional e experimental, com foco em clareza arquitetural, simplicidade e rastreabilidade.

---

## Principais Características

- Arquitetura multiagente com CrewAI
- Coleta de notícias em fluxo estruturado
- Modelo de domínio padronizado para notícias
- Enriquecimento determinístico de dados
- Geração de relatório em Markdown
- Interface acadêmica com Streamlit e dados simulados
- Testes automatizados
- Documentação técnica e acadêmica

---

## Arquitetura do Sistema

O projeto segue uma arquitetura em camadas, com separação entre:

- agentes: execução de papéis especializados;
- tasks: definição das atividades do fluxo;
- crews: composição do processo;
- services: encapsulamento da lógica operacional;
- models: representação formal do domínio;
- tools: integração com mecanismos de busca;
- settings e logger: configuração e registro de execução.

A estrutura principal está localizada em [src/amapa_politico_monitor](src/amapa_politico_monitor).

---

## Fluxo de Funcionamento

1. A aplicação recebe uma consulta relacionada ao contexto político do Amapá.
2. O serviço de coleta prepara e organiza os dados de entrada.
3. O modelo NewsItem representa a notícia de forma padronizada.
4. O serviço de enriquecimento adiciona informações determinísticas de domínio.
5. Os agentes executam o fluxo definido pela crew.
6. O resultado é apresentado em relatório, logs e interface acadêmica.

---

## Tecnologias Utilizadas

- Python 3.11+
- CrewAI
- Streamlit
- Loguru
- Python-dotenv
- Requests
- BeautifulSoup
- Pandas
- pytest

---

## Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/FredsonAlves/amapa-politico-monitor.git
cd amapa-politico-monitor
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o ponto de entrada principal

```bash
python -m amapa_politico_monitor.main
```

---

## Como Executar os Testes

```bash
pytest -q
```

Os testes cobrem estrutura do projeto, importações, modelo de domínio, serviço de coleta e enriquecimento determinístico.

---

## Como Executar a Interface Streamlit

```bash
streamlit run src/amapa_politico_monitor/ui/app.py
```

A interface acadêmica utiliza dados simulados para demonstrar filtros, estatísticas, detalhes de notícia e relatório em Markdown.

---

## Deploy no Streamlit Community Cloud

Para publicar o projeto manualmente no Streamlit Community Cloud, utilize as seguintes configurações:

- Repositório: https://github.com/Fredson-Alves/amapa-politico-monitor
- Branch: main
- Main file path: src/amapa_politico_monitor/ui/app.py

Instruções resumidas:

1. Acesse o Streamlit Community Cloud e escolha "New app".
2. Selecione o repositório acima e a branch main.
3. Defina o caminho do arquivo principal como src/amapa_politico_monitor/ui/app.py.
4. Mantenha o projeto sem secrets ou chaves de API e confirme que a interface roda apenas com dados mockados.
5. Publique o app e valide a interface após o deploy.

---

## Estrutura do Projeto

```text
amapa-politico-monitor/
├── docs/
├── logs/
├── output/
├── src/
│   └── amapa_politico_monitor/
│       ├── agents/
│       ├── crews/
│       ├── models/
│       ├── services/
│       ├── tasks/
│       ├── tools/
│       ├── ui/
│       ├── config/
│       ├── settings.py
│       ├── logger.py
│       ├── crew.py
│       └── main.py
├── tests/
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

Documentação complementar:

- [docs/release-academica-v1.md](docs/release-academica-v1.md)
- [docs/roadmap-v1.md](docs/roadmap-v1.md)

---

## Arquitetura dos Agentes

O sistema é composto por agentes especializados com papéis bem definidos:

- Pesquisador OSINT: identifica notícias públicas relevantes.
- Verificador de Fontes: organiza e valida as referências encontradas.
- Classificador Político-Institucional: categoriza as notícias pelo contexto institucional.
- Redator de Relatório: consolida as informações em um relatório objetivo.

---

## Serviços e Modelo de Domínio

O projeto utiliza:

- NewsCollectionService: camada de coleta de notícias.
- NewsEnrichmentService: enriquecimento determinístico de dados.
- NewsItem: modelo oficial de representação da notícia.

---

## Roadmap

A evolução do projeto está organizada em:

- Versão 1.0: estrutura estável, agentes, coleta, relatório Markdown, logs e testes básicos.
- Versão 1.1: melhoria da coleta, normalização de resultados e saída JSON.
- Versão 2.0: múltiplas fontes, histórico, agendamento e interface mais completa.

Consulte [docs/roadmap-v1.md](docs/roadmap-v1.md) para mais detalhes.

---

## Decisões Arquiteturais

As principais decisões de arquitetura foram:

- manter a estrutura simples e modular;
- preservar a organização em camadas;
- centralizar configurações em settings;
- evitar dependência de YAML para o fluxo principal;
- manter o backend separado da interface acadêmica;
- priorizar testabilidade e clareza sobre complexidade.

---

## Uso de Inteligência Artificial no Desenvolvimento

Este projeto foi desenvolvido com apoio de ferramentas de IA em diferentes papéis:

- ChatGPT como arquiteto: auxiliou na organização conceitual, definição de estrutura e revisão de decisões de design.
- Codex como desenvolvedor: contribuiu com implementação, refatoração e geração de código alinhado ao escopo definido.
- Revisão técnica humana: todas as alterações foram avaliadas para garantir consistência arquitetural, segurança e alinhamento com os objetivos do projeto.

---

## Limitações Atuais

- o fluxo de coleta depende de mecanismos de busca disponíveis no ambiente de execução;
- o enriquecimento é determinístico e não substitui análise semântica mais sofisticada;
- a versão atual prioriza estrutura, estabilidade e apresentação acadêmica sobre funcionalidades avançadas;
- não há persistência, histórico extensivo ou interface operacional completa nesta release.

---

## Trabalhos Futuros

- melhoria da qualidade da coleta;
- normalização mais robusta de resultados;
- exportação em JSON e outros formatos;
- fortalecimento da suíte de testes;
- evolução para versões posteriores com maior cobertura funcional e operacional.

---

## Licença

Este projeto está licenciado sob a licença MIT.

---

## Autor

Fredson Alves

GitHub: https://github.com/FredsonAlves

---

## Agradecimentos

Agradeço à comunidade acadêmica, aos materiais de referência em IA aplicada e à estrutura de desenvolvimento colaborativo que possibilitou a consolidação desta primeira release do projeto.

---

## Aviso

Este projeto destina-se exclusivamente ao monitoramento de informações públicas obtidas de fontes abertas (OSINT). As informações produzidas não substituem procedimentos formais de análise, verificação ou investigação conduzidos pelos órgãos competentes.