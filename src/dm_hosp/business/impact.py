"""Caso de negocio: valor economico de intervenir al top K % de mayor riesgo."""
from dataclasses import dataclass

import numpy as np

from dm_hosp.models.evaluate import top_k_idx


@dataclass
class Supuestos:
    costo_hospitalizacion: float      # S/ por hospitalizacion
    costo_programa_por_paciente: float  # S/ por paciente intervenido
    efectividad: float                # fraccion de eventos evitados entre los intervenidos


def valor_neto(n_intervenidos: int, eventos_capturados: float, s: Supuestos) -> dict:
    evitados = eventos_capturados * s.efectividad
    beneficio = evitados * s.costo_hospitalizacion
    costo = n_intervenidos * s.costo_programa_por_paciente
    return {"evitados": evitados, "beneficio": beneficio, "costo_programa": costo,
            "valor_neto": beneficio - costo}


def valor_incremental(y_true, y_score, k_frac: float, s: Supuestos) -> dict:
    """Valor del modelo frente a seleccionar K % de pacientes al azar."""
    y_true = np.asarray(y_true)
    idx = top_k_idx(y_score, k_frac)
    n = len(idx)
    con_modelo = valor_neto(n, float(y_true[idx].sum()), s)
    azar = valor_neto(n, float(y_true.mean() * n), s)
    return {"con_modelo": con_modelo, "azar": azar,
            "valor_incremental": con_modelo["valor_neto"] - azar["valor_neto"]}
