"""Interface acadêmica em Streamlit para demonstração do projeto Amapá Político Monitor."""

from __future__ import annotations

import streamlit as st

from amapa_politico_monitor.models.news_item import NewsItem
from amapa_politico_monitor.ui.mock_data import get_mock_news


st.set_page_config(page_title="Amapá Político Monitor", page_icon="📰", layout="wide")


def build_sidebar() -> dict[str, str]:
    """Constrói o formulário de filtros da interface."""
    st.sidebar.header("Filtro de Monitoramento")
    termo = st.sidebar.text_input("Termo de pesquisa", value="política")
    periodo = st.sidebar.selectbox("Período", ["Últimos 7 dias", "Últimos 30 dias", "Últimos 90 dias"])
    municipio = st.sidebar.selectbox("Município", ["Todos", "Macapá", "Santana", "Oiapoque"])
    categoria = st.sidebar.selectbox("Categoria", ["Todas", "Governo", "Ministério Público", "Legislativo", "Eleitoral"])

    executar = st.sidebar.button("Executar Monitoramento")
    return {
        "termo": termo,
        "periodo": periodo,
        "municipio": municipio,
        "categoria": categoria,
        "executar": executar,
    }


def filter_news(news_items: list[NewsItem], filters: dict[str, str]) -> list[NewsItem]:
    """Filtra notícias mockadas com base nos valores do formulário."""
    filtered = list(news_items)

    if filters["termo"]:
        termo = filters["termo"].lower()
        filtered = [item for item in filtered if termo in item.titulo.lower() or termo in item.resumo.lower()]

    if filters["municipio"] != "Todos":
        filtered = [item for item in filtered if filters["municipio"] in item.municipios]

    if filters["categoria"] != "Todas":
        filtered = [item for item in filtered if item.categoria == filters["categoria"]]

    return filtered


def render_metrics(news_items: list[NewsItem]) -> None:
    """Exibe cards com estatísticas simuladas."""
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Notícias exibidas", len(news_items))
    col2.metric("Municípios", len({municipio for item in news_items for municipio in item.municipios}))
    col3.metric("Órgãos", len({orgao for item in news_items for orgao in item.orgaos}))
    col4.metric("Categorias", len({item.categoria for item in news_items if item.categoria}))


def render_results(news_items: list[NewsItem]) -> None:
    """Exibe tabela e detalhes das notícias simuladas."""
    st.subheader("Resultados simulados")
    if not news_items:
        st.info("Nenhuma notícia corresponde aos filtros selecionados.")
        return

    table_data = [
        {
            "Título": item.titulo,
            "Fonte": item.fonte,
            "Município": ", ".join(item.municipios) or "—",
            "Categoria": item.categoria or "—",
            "Impacto": item.impacto_institucional or "—",
        }
        for item in news_items
    ]
    st.dataframe(table_data, use_container_width=True)

    st.subheader("Detalhes da notícia")
    selected = st.selectbox("Selecione uma notícia", options=[item.id for item in news_items], format_func=lambda value: next(item.titulo for item in news_items if item.id == value))
    selected_item = next(item for item in news_items if item.id == selected)
    st.markdown(f"### {selected_item.titulo}")
    st.write(selected_item.resumo)
    st.write(f"**Fonte:** {selected_item.fonte}")
    st.write(f"**URL:** {selected_item.url}")
    st.write(f"**Municípios:** {', '.join(selected_item.municipios) or '—'}")
    st.write(f"**Órgãos:** {', '.join(selected_item.orgaos) or '—'}")
    st.write(f"**Palavras-chave:** {', '.join(selected_item.palavras_chave) or '—'}")


def render_report(news_items: list[NewsItem]) -> None:
    """Exibe um relatório simulado em Markdown."""
    st.subheader("Relatório simulado")
    report = "# Relatório de Monitoramento\n\n"
    report += f"- Notícias exibidas: {len(news_items)}\n"
    report += f"- Municípios identificados: {len({municipio for item in news_items for municipio in item.municipios})}\n"
    report += f"- Órgãos identificados: {len({orgao for item in news_items for orgao in item.orgaos})}\n\n"
    report += "## Destaques\n"
    for item in news_items[:3]:
        report += f"- {item.titulo}\n"
    st.markdown(report)


def main() -> None:
    """Renderiza a interface acadêmica principal."""
    st.title("Amapá Político Monitor")
    st.write("Protótipo acadêmico de monitoramento de notícias políticas públicas do Estado do Amapá.")

    filters = build_sidebar()
    all_news = get_mock_news()
    visible_news = filter_news(all_news, filters)

    render_metrics(visible_news)

    tab1, tab2 = st.tabs(["Resultados", "Sobre o Projeto"])
    with tab1:
        render_results(visible_news)
        render_report(visible_news)
    with tab2:
        st.markdown(
            """
            ## Sobre o Projeto

            O Amapá Político Monitor é um protótipo acadêmico para demonstrar um fluxo simples de coleta, estruturação e enriquecimento de notícias políticas públicas.

            Esta interface utiliza apenas dados simulados para fins de apresentação e não executa chamadas reais a APIs ou serviços externos.
            """
        )


if __name__ == "__main__":
    main()
