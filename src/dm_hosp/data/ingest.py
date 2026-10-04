"""Ingesta: ZIP -> CSV -> Parquet (zstd) usando DuckDB (no carga todo en memoria)."""
import unicodedata
import zipfile
from pathlib import Path

import duckdb

from dm_hosp.paths import INTERIM, RAW

TABLAS = ["prestaciones", "diagnosticos", "medicamentos", "procedimientos", "insumos"]


def _norm(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def extraer_zips(raw_dir: Path = RAW) -> None:
    """Extrae recursivamente todos los .zip de data/raw (incluye zips dentro de zips)."""
    pendientes = list(raw_dir.rglob("*.zip"))
    vistos = set()
    while pendientes:
        z = pendientes.pop()
        if z in vistos:
            continue
        vistos.add(z)
        destino = z.with_suffix("")
        if not destino.exists():
            print(f"Extrayendo {z.name} ...")
            with zipfile.ZipFile(z) as f:
                f.extractall(destino)
        pendientes.extend(p for p in destino.rglob("*.zip") if p not in vistos)


def csv_a_parquet(raw_dir: Path = RAW, out_dir: Path = INTERIM, memoria: str = "8GB") -> None:
    """Convierte cada tabla (todos sus CSV) a un unico Parquet comprimido."""
    out_dir.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect()
    con.execute(f"PRAGMA memory_limit='{memoria}'")
    csvs = [p for p in raw_dir.rglob("*") if p.suffix.lower() in (".csv", ".txt")]
    for tabla in TABLAS:
        archivos = [p.as_posix() for p in csvs if tabla in _norm(p.name)]
        if not archivos:
            print(f"[AVISO] No se encontraron CSV para '{tabla}'")
            continue
        lista = ", ".join(f"'{a}'" for a in archivos)
        destino = (out_dir / f"{tabla}.parquet").as_posix()
        print(f"{tabla}: {len(archivos)} archivo(s) -> {destino}")
        con.execute(
            f"COPY (SELECT * FROM read_csv_auto([{lista}], union_by_name=true, ignore_errors=true)) "
            f"TO '{destino}' (FORMAT PARQUET, COMPRESSION ZSTD)"
        )
