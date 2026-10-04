"""Descomprime los ZIP de data/raw y convierte los CSV a Parquet en data/interim."""
from dm_hosp.config import load_config
from dm_hosp.data.ingest import csv_a_parquet, extraer_zips

if __name__ == "__main__":
    cfg = load_config()
    extraer_zips()
    csv_a_parquet(memoria=cfg["datos"]["memoria_duckdb"])
    print("Ingesta lista: revisa data/interim/*.parquet")
