"""Modelo de domínio para notícias do projeto Amapá Político Monitor."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class NewsItem:
    """Representa uma notícia política pública coletada pelo sistema."""

    id: str
    titulo: str
    resumo: str
    fonte: str
    url: str
    data_publicacao: str | None
    municipios: list[str] = field(default_factory=list)
    orgaos: list[str] = field(default_factory=list)
    pessoas: list[str] = field(default_factory=list)
    palavras_chave: list[str] = field(default_factory=list)
    categoria: str | None = None
    impacto_institucional: str | None = None
    coletado_em: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict[str, Any]:
        """Retorna uma representação serializável do objeto."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "resumo": self.resumo,
            "fonte": self.fonte,
            "url": self.url,
            "data_publicacao": self.data_publicacao,
            "municipios": list(self.municipios),
            "orgaos": list(self.orgaos),
            "pessoas": list(self.pessoas),
            "palavras_chave": list(self.palavras_chave),
            "categoria": self.categoria,
            "impacto_institucional": self.impacto_institucional,
            "coletado_em": self.coletado_em.isoformat(),
        }

    def to_json(self) -> str:
        """Retorna a representação JSON do objeto."""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "NewsItem":
        """Cria um NewsItem a partir de um dicionário."""
        coletado_em = data.get("coletado_em")
        if isinstance(coletado_em, str):
            coletado_em_dt = datetime.fromisoformat(coletado_em)
        else:
            coletado_em_dt = datetime.now(timezone.utc)

        return cls(
            id=str(data.get("id", "")),
            titulo=str(data.get("titulo", "")),
            resumo=str(data.get("resumo", "")),
            fonte=str(data.get("fonte", "")),
            url=str(data.get("url", "")),
            data_publicacao=data.get("data_publicacao"),
            municipios=list(data.get("municipios", [])),
            orgaos=list(data.get("orgaos", [])),
            pessoas=list(data.get("pessoas", [])),
            palavras_chave=list(data.get("palavras_chave", [])),
            categoria=data.get("categoria"),
            impacto_institucional=data.get("impacto_institucional"),
            coletado_em=coletado_em_dt,
        )
