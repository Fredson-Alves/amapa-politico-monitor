from amapa_politico_monitor.models.news_item import NewsItem
from amapa_politico_monitor.services.news_enrichment_service import NewsEnrichmentService


def test_enrichment_identifies_municipios():
    service = NewsEnrichmentService()
    item = NewsItem(
        id="1",
        titulo="Prefeito de Macapá anuncia medida",
        resumo="Ação no município de Macapá gera repercussão.",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao="2024-01-01",
    )

    enriched = service.enrich(item)

    assert enriched.municipios == ["Macapá"]


def test_enrichment_identifies_orgaos():
    service = NewsEnrichmentService()
    item = NewsItem(
        id="2",
        titulo="MP-AP abre investigação",
        resumo="A decisão foi tomada pelo Governo do Estado do Amapá.",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao="2024-01-01",
    )

    enriched = service.enrich(item)

    assert enriched.orgaos == ["MP-AP", "Governo do Estado do Amapá"]


def test_enrichment_identifies_palavras_chave():
    service = NewsEnrichmentService()
    item = NewsItem(
        id="3",
        titulo="Contrato e licitação no orçamento",
        resumo="Discussão sobre emenda parlamentar e transparência.",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao="2024-01-01",
    )

    enriched = service.enrich(item)

    assert enriched.palavras_chave == ["contrato", "licitação", "orçamento", "emenda parlamentar", "transparência"]


def test_enrichment_avoids_duplicates():
    service = NewsEnrichmentService()
    item = NewsItem(
        id="4",
        titulo="Macapá, Macapá e Macapá",
        resumo="Macapá, Macapá",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao="2024-01-01",
    )

    enriched = service.enrich(item)

    assert enriched.municipios == ["Macapá"]


def test_enrichment_returns_empty_lists_when_no_matches():
    service = NewsEnrichmentService()
    item = NewsItem(
        id="5",
        titulo="Texto sem correspondência",
        resumo="Nada relevante para esta regra.",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao="2024-01-01",
    )

    enriched = service.enrich(item)

    assert enriched.municipios == []
    assert enriched.orgaos == []
    assert enriched.palavras_chave == []


def test_enrichment_preserves_non_related_fields():
    service = NewsEnrichmentService()
    item = NewsItem(
        id="6",
        titulo="Nomeação no governo",
        resumo="Assunto relevante para a administração pública.",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao="2024-01-01",
        categoria="Governo",
        impacto_institucional="Alta",
    )

    enriched = service.enrich(item)

    assert enriched.categoria == "Governo"
    assert enriched.impacto_institucional == "Alta"
    assert enriched.pessoas == []
