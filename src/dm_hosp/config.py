"""Carga de configs/config.yaml."""
import yaml

from dm_hosp.paths import CONFIGS


def load_config(nombre: str = "config.yaml") -> dict:
    with open(CONFIGS / nombre, encoding="utf-8") as f:
        return yaml.safe_load(f)
