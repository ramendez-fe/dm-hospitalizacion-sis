# Diccionario de datos

> Completar la descripción de cada columna con el diccionario oficial del portal (datosabiertos.gob.pe).
> Las columnas marcadas **[VERIFICAR]** tienen significado dudoso: no usarlas hasta confirmarlo.

## Prestaciones (nivel: atención)
| Columna | Descripción | Tipo | Notas |
|---|---|---|---|
| FECHA_CORTE | Fecha de corte de la publicación | fecha (yyyymmdd) | Constante |
| ULTIMO_MES_CONSUMOS | Último mes con consumos | yyyymm | 202512 = fin real de los datos |
| CODIGO_ANONIMIZADO | Identificador anónimo del paciente | texto (hash) | Llave de paciente |
| SEXO | Sexo del asegurado | categórica | |
| ID_REGISTRO_REL | Identificador de la atención (FUA) | entero | Llave de unión con las demás tablas |
| FECHA_ATENCION | Fecha de la atención | yyyymmdd | |
| EDAD | Edad | entero | |
| TIPO_DIABETES | Tipo de diabetes registrado | categórica | ¿Cambia por paciente? **[VERIFICAR]** |
| UBIGEO / DEPARTAMENTO / PROVINCIA / DISTRITO | Ubicación | categórica | Alta cardinalidad (UBIGEO) |
| NIVEL_EESS | Nivel del establecimiento | categórica | |
| CODIGO_SERV_PRESTACIONAL / SERVICIO_PRESTACIONAL | Servicio prestacional | categórica | Base para identificar hospitalización |
| DIAS_HOSP | Días de hospitalización | numérica | Muchos nulos (solo aplica a hospitalización) |
| TIPO_PERSONAL_SALUD | Tipo de profesional | categórica | |
| FECATE_POST_FECFED | **[VERIFICAR]** significado | SI/NO | No usar hasta confirmar |
| ES_CAPITA | Atención bajo pago capitado | S/N | **[VERIFICAR]** |
| DESTINO_ASEGURADO | Destino tras la atención (Alta, Citado, ...) | categórica | Resultado de la atención: NO usar como predictora del mismo periodo |

## Diagnósticos (atención × diagnóstico)
| Columna | Descripción |
|---|---|
| ID_REGISTRO_REL | Llave de la atención |
| CODDIA | Código CIE-10 |
| TIPO_DIAGNOSTICO | DEFINITIVO / PRESUNTIVO / otros |

## Medicamentos / Procedimientos / Insumos (atención × ítem)
| Columna | Descripción | Notas |
|---|---|---|
| ID_REGISTRO_REL | Llave de la atención | |
| CODDIA | Diagnóstico asociado | No siempre es diabetes |
| COD_MEDICAMENTO / COD_PROCEDIMIENTO / COD_INSUMO | Código del ítem | Normalizar ceros a la izquierda al unir con catálogo |
| CANTIDAD_ENTREGADA | Cantidad | |
| VALOR_NETO | Valor monetario | Muchos ceros: **[VERIFICAR]** su significado |

## Catálogos (`6. Catálogos.xlsx`)
Hojas: Diagnóstico, Medicamentos, Procedimientos, Insumos.
