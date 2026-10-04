# Supuestos del caso de negocio

> Todo número del caso de negocio debe tener **fuente** o justificación, y un rango para el análisis de sensibilidad.

| Supuesto | Valor base | Rango sensibilidad | Fuente / justificación |
|---|---|---|---|
| Costo promedio por hospitalización (S/) | 3 000 | 2 000 – 5 000 | _(tarifario SIS / literatura / estimación con DIAS_HOSP)_ |
| Costo del programa por paciente intervenido (S/) | 80 | 50 – 150 | _(supuesto razonable; documentar)_ |
| Efectividad de la intervención (reducción de eventos) | 20 % | 10 % – 30 % | _(literatura sobre gestión de casos en diabetes)_ |
| Capacidad de intervención (K) | 10 % | 5 % – 20 % | _(capacidad operativa del programa)_ |

## Fórmula
```
Valor del modelo = Valor neto (top K con modelo) - Valor neto (K aleatorio)
Valor neto = hospitalizaciones evitadas x costo hospitalizacion - pacientes intervenidos x costo programa
```
