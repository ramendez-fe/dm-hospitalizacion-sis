import numpy as np

from dm_hosp.models.evaluate import lift_at_k, precision_at_k, recall_at_k


def test_metricas_top_k_modelo_perfecto():
    y = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    s = np.array([0.9, 0.8, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    assert precision_at_k(y, s, 0.2) == 1.0
    assert recall_at_k(y, s, 0.2) == 1.0
    assert lift_at_k(y, s, 0.2) == 5.0
