# Predicción de hospitalización a 12 meses en pacientes con Diabetes Mellitus (SIS)

Trabajo final – Analítica Predictiva (Diplomado de posgrado en Data Science).

## Resumen
Modelo supervisado de **clasificación binaria** que estima la probabilidad de que un paciente con
Diabetes Mellitus asegurado al SIS sea **hospitalizado en los 12 meses siguientes** a un punto de corte,
para priorizar acciones preventivas con capacidad limitada (top K % de mayor riesgo).

- **Datos:** Prestaciones de salud asociadas a asegurados con DM – SIS (datosabiertos.gob.pe), 2018–2025.
- **Unidad de análisis:** paciente × corte anual (31-dic).
- **Validación:** temporal (train 2022 → valid 2023 → test 2024).
- **Métricas:** PR-AUC, ROC-AUC, Recall@K, Lift@K, Brier, valor económico.

## Estructura
Ver `docs/`. Resumen:

| Carpeta | Contenido |
|---|---|
| `configs/` | Parámetros del proyecto (`config.yaml`) |
| `data/` | `raw` (original, no se versiona) → `interim` (parquet) → `processed` (dataset de modelado) |
| `notebooks/` | Narrativa: verificaciones, EDA, modelado, negocio, interpretabilidad |
| `src/dm_hosp/` | Código reutilizable (ingesta, features, modelos, negocio) |
| `scripts/` | Pipelines ejecutables (procesos pesados) |
| `tests/` | Pruebas automáticas (fugas de información, split temporal, métricas) |
| `reports/` | Figuras, tablas y guion de la presentación |
| `docs/` | Diccionario de datos, decisiones (ADR) y supuestos de negocio |

## Instalación
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      |  Linux/Mac: source .venv/bin/activate
pip install -e ".[dev]"
python -m ipykernel install --user --name dm-hosp --display-name "Python (dm-hosp)"
```

## Cómo reproducir
1. Descargar el ZIP desde datosabiertos.gob.pe y dejarlo en `data/raw/`.
2. `python scripts/run_ingesta.py` (descomprime y convierte a Parquet en `data/interim/`).
3. `python scripts/run_build_dataset.py` (genera `data/processed/dataset_modelado.parquet`).
4. Abrir los notebooks en orden (`notebooks/00_...` a `05_...`).
5. `python scripts/run_train.py` (entrena y guarda artefactos en `models/`).

(Con `make`: `make install`, `make ingesta`, `make dataset`, `make entrenar`, `make test`.)

## Limitaciones
- Sin valores clínicos (HbA1c, glucosa, presión); solo se sabe si se hizo el examen.
- Población asegurada al SIS (no representa a toda la población con diabetes).
- Datos administrativos: sesgos de registro por establecimiento/región.

## Resultados
_(completar al final: tabla comparativa de modelos, variables importantes, impacto económico)_
