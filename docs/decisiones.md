# Registro de decisiones (ADR)

Cada decisión importante se registra con fecha, contexto y consecuencias. Esto demuestra rigor metodológico.

## ADR-001 – Problema y target
- **Decisión:** clasificación binaria; target = hospitalización en los 12 meses posteriores al corte.
- **Motivo:** valor económico directo, accionable, desbalance + multi-tabla + validación temporal.
- **Alternativas descartadas:** costo anual (VALOR_NETO con muchos ceros), complicaciones (sesgo de vigilancia).

## ADR-002 – Unidad de análisis y cohorte
- **Decisión:** paciente × corte (31-dic). Cohorte: DM definitiva (E10–E14) ≤ corte, ≥1 atención en 12 meses previos, sin fallecimiento registrado.
- **Consecuencia:** el mismo paciente puede aparecer en varios cortes (válido con split temporal).

## ADR-003 – Validación temporal
- **Decisión:** train corte 2022 → valid 2023 → test 2024. Nunca mezclar cortes al azar.
- **Motivo:** evitar fuga y simular uso real; se evita el periodo COVID en el diseño principal.

## ADR-004 – Stack y estructura
- **Decisión:** DuckDB + Parquet para el procesamiento (3,3 GB); código reutilizable en `src/`, notebooks para la narrativa.
- **Motivo:** reproducibilidad, memoria controlada, notebooks livianos.

## ADR-005 – Métricas
- **Decisión:** PR-AUC como métrica principal + Recall@K / Lift@K (capacidad limitada) + Brier (calibración).
- **Motivo:** desbalance y costos asimétricos; accuracy no es informativa.

## Plantilla
```
## ADR-00X – Título
- Fecha:
- Contexto:
- Decisión:
- Alternativas:
- Consecuencias:
```
