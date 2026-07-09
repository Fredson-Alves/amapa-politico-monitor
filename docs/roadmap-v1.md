# Roadmap da Versão 1.0 — Amapá Político Monitor

## Visão Geral

O Amapá Político Monitor é uma plataforma OSINT em Python, baseada em CrewAI, voltada para o monitoramento de notícias políticas públicas do Estado do Amapá. A versão 1.0 deve consolidar uma arquitetura simples, estável e profissional, com foco em coleta, organização e geração de relatórios em formato Markdown.

A evolução do projeto deve priorizar clareza, confiabilidade e manutenção, evitando complexidade desnecessária.

---

## Versão 1.0

### Objetivo

Entregar uma primeira versão funcional, com estrutura bem definida, componentes alinhados e capacidade de gerar um relatório institucional básico a partir da coleta de informações públicas.

### Escopo da Versão 1.0

- Estrutura estável e consistente com arquitetura em src/
- Implementação de agentes multiagente com papéis bem definidos
- Coleta de informações por meio de ferramenta de busca
- Geração de relatório em Markdown
- Configuração de logs para acompanhamento de execução
- Testes básicos de importação e estrutura
- Documentação inicial do projeto

### Entregáveis Esperados

- Pacote Python importável e organizado
- Módulos de agentes, tarefas, crew e tools alinhados
- Configurações centralizadas em settings.py
- Logging funcional em logs/execucao.log
- Relatório inicial gerado em output/
- Documentação mínima para execução e entendimento do projeto

---

## Versão 1.1

### Objetivo

Melhorar a qualidade e a robustez da execução inicial, sem ampliar a complexidade da arquitetura.

### Escopo da Versão 1.1

- Melhoria da coleta e refinamento do fluxo de busca
- Normalização de resultados para maior consistência
- Suporte a saída em JSON além do relatório Markdown
- Testes mais robustos, cobrindo cenários principais de execução
- Ajustes de qualidade em logs e tratamento de erros

### Entregáveis Esperados

- Melhor organização dos dados coletados
- Estrutura de saída mais padronizada
- Maior confiabilidade dos testes
- Melhor experiência operacional para execução local

---

## Versão 2.0

### Objetivo

Expandir o alcance do projeto para uma solução mais completa de monitoramento institucional e visualização de informações.

### Escopo da Versão 2.0

- Suporte a múltiplas fontes de coleta
- Histórico de monitoramento e registros de execução
- Agendamento de execuções periódicas
- Dashboard ou interface para visualização dos resultados
- Relatórios mais avançados, com filtros e organização temática

### Entregáveis Esperados

- Plataforma com maior cobertura de fontes e contexto
- Operação contínua e programada
- Interface mais acessível para consulta e análise
- Relatórios com maior profundidade e utilidade institucional

---

## Backlog Futuro

Itens que podem ser considerados após a versão 2.0, conforme maturidade do projeto e demanda institucional:

- Integração com fontes adicionais e APIs públicas
- Classificação semântica mais avançada das notícias
- Exportação para outros formatos, como CSV e PDF
- Funcionalidades de alerta e notificação
- Melhorias em análise temporal e tendências
- Ferramentas de busca mais específicas e especializadas
- Evolução da interface para uso operacional intensivo

---

## Fora do Escopo da Versão 1.0

A versão 1.0 não deve incluir, neste momento:

- Integração com múltiplas fontes de forma ampla e robusta
- Histórico persistente de consultas
- Agendamento automático de execução
- Interface gráfica ou dashboard completo
- Relatórios avançados com visualizações complexas
- Recursos de automação operacional além do fluxo básico
- Implementações que aumentem a complexidade da arquitetura

O foco da versão 1.0 é estabelecer uma base sólida e confiável.

---

## Critérios de Pronto

A versão 1.0 poderá ser considerada pronta quando atender aos seguintes critérios:

- A arquitetura permanecer simples, organizada e consistente
- O pacote Python estiver importável e executável
- Os agentes, tarefas e crew estiverem alinhados com a estrutura do projeto
- A coleta básica estiver funcionando sem depender de YAML
- O relatório Markdown estiver sendo produzido corretamente
- Os logs estiverem configurados e registrando execuções
- Os testes básicos estiverem passando
- A documentação inicial estiver presente e suficiente para uso básico

---

## Regras de Evolução

A evolução do projeto deve seguir as regras abaixo:

1. Manter a arquitetura simples e previsível.
2. Evitar introduzir novas camadas ou abstrações desnecessárias.
3. Preservar o foco institucional e OSINT do projeto.
4. Priorizar melhorias que aumentem confiabilidade e clareza.
5. Não adicionar dependências sem necessidade clara e justificável.
6. Garantir compatibilidade com a estrutura atual antes de expandir recursos.
7. Evoluir de forma incremental, mantendo versões menores e bem delimitadas.
8. Documentar mudanças relevantes à medida que o projeto crescer.
9. Respeitar o princípio de não introduzir complexidade desnecessária.
10. Manter testes e documentação alinhados com cada evolução.

---

## Conclusão

A versão 1.0 deve servir como base sólida para o projeto, permitindo validar o modelo de agentes, a coleta de dados e a geração de relatórios com uma estrutura simples e sustentável. As versões posteriores devem ampliar a capacidade do sistema sem comprometer sua clareza e manutenção.
