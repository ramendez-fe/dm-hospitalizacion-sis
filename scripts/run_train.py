"""Entrena los modelos y guarda artefactos en models/ y tablas en reports/tables/."""
from dm_hosp.models.train import entrenar_todo

if __name__ == "__main__":
    entrenar_todo()
