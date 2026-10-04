"""Construye data/processed/dataset_modelado.parquet (paciente x corte)."""
from dm_hosp.features.build_dataset import construir_dataset

if __name__ == "__main__":
    construir_dataset()
