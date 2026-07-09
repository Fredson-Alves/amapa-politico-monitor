# Release Acadêmica v1.0 — Amapá Político Monitor

## Título do Projeto

Amapá Político Monitor

## Objetivo Geral

Desenvolver uma solução em Python, baseada em arquitetura multiagente e técnicas de OSINT, para monitorar notícias públicas relacionadas à política e ao contexto institucional do Estado do Amapá.

## Problema que o Projeto Resolve

O cenário político e institucional do Amapá exige acompanhamento constante de informações públicas dispersas em diversas fontes. A coleta manual de notícias é trabalhosa, sujeita a lacunas e dificulta a consolidação de um panorama atualizado. O projeto busca organizar esse processo por meio de automação orientada a agentes especializados.

## Justificativa

A proposta é relevante em contextos institucionais, acadêmicos e de análise pública, pois permite reduzir a carga operacional de coleta e organizar informações em formato estruturado. A abordagem contribui para a compreensão do ambiente político, a geração de relatórios úteis e o fortalecimento de práticas de monitoramento baseado em fontes abertas.

## Tecnologias Utilizadas

- Python
- CrewAI
- estrutura de projeto em src/
- módulos de agentes, tarefas, serviços, modelos e ferramentas
- logging centralizado
- testes automatizados com pytest
- documentação técnica e acadêmica

## Arquitetura Geral

O projeto segue uma arquitetura simples e modular, organizada em camadas com foco em separação de responsabilidades. A estrutura principal inclui:

- agentes para execução especializada;
- tarefas para definição de objetivos e entregas;
- crews para composição do fluxo;
- services para encapsular lógica operacional;
- models para representação formal dos dados;
- tools para integração com mecanismos de busca;
- settings e logger para configuração e registro de execução.

## Explicação dos Agentes

O sistema conta com agentes especializados para diferentes funções:

- Pesquisador OSINT: responsável pela identificação de notícias públicas relevantes;
- Verificador de Fontes: responsável por organizar e validar as informações encontradas;
- Classificador Político-Institucional: responsável por categorizar as notícias conforme o contexto político e institucional;
- Redator de Relatório: responsável por consolidar os resultados em um relatório objetivo e estruturado.

## Explicação dos Serviços

Os serviços encapsulam a lógica operacional do projeto sem expor detalhes de implementação aos agentes. Entre os principais componentes estão:

- NewsCollectionService: responsável pela coleta de notícias;
- NewsEnrichmentService: responsável por enriquecer automaticamente os dados com informações determinísticas de domínio.

## Explicação do Modelo NewsItem

O modelo NewsItem representa a unidade principal de informação do sistema. Ele organiza os dados de uma notícia em uma estrutura padronizada, permitindo que diferentes camadas do projeto troquem informações por meio de um formato comum. O modelo inclui campos como título, resumo, fonte, URL, data de publicação, municípios, órgãos, pessoas, palavras-chave e metadados de contexto.

## Explicação do Enriquecimento Determinístico

O enriquecimento determinístico é realizado sem uso de IA ou chamadas externas. A partir do título e do resumo da notícia, o sistema identifica automaticamente:

- municípios;
- órgãos;
- palavras-chave.

Essa etapa utiliza listas de domínio previamente definidas, o que torna o processo previsível, transparente e adequado à arquitetura simples do projeto.

## Fluxo de Funcionamento

1. O sistema recebe uma consulta relacionada ao contexto político do Amapá.
2. O serviço de coleta busca informações públicas relevantes.
3. O modelo NewsItem estrutura os dados coletados.
4. O serviço de enriquecimento adiciona informações determinísticas de domínio.
5. Os agentes organizam e transformam esses dados em um fluxo de execução orientado a relatório.
6. O resultado final é apresentado em formato estruturado para consulta institucional.

## Resultados dos Testes

O projeto possui testes automatizados cobrindo importação, estrutura, modelo de domínio, serviço de coleta e enriquecimento determinístico. A suíte atual está passando, o que demonstra estabilidade estrutural para a versão apresentada.

## Limitações Atuais

- A coleta depende de mecanismos de busca disponíveis no ambiente de execução.
- O enriquecimento é determinístico e não substitui análise semântica mais sofisticada.
- O projeto ainda possui foco inicial em estrutura, organização e geração de relatórios básicos.
- A solução não inclui persistência, histórico extensivo ou interface avançada nesta versão.

## Próximos Passos

- melhorar a qualidade da coleta;
- ampliar a normalização de resultados;
- incluir saída em JSON;
- fortalecer a suíte de testes;
- evoluir a solução para versões posteriores com maior cobertura funcional.

## Conclusão

A release acadêmica v1.0 representa uma primeira versão consistente do Amapá Político Monitor, com arquitetura organizada, componentes bem definidos, modelo de domínio consolidado e fluxo de enriquecimento determinístico. A proposta demonstra a viabilidade de uma solução simples, institucional e orientada a critérios de monitoramento público e OSINT.
