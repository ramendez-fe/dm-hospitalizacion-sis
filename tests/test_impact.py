import pytest

from dm_hosp.business.impact import Supuestos, valor_neto


def test_ejemplo_de_la_guia():
    # 10.000 intervenidos, 2.400 eventos capturados, 20 % efectividad, S/3.000 por hosp., S/80 por paciente
    s = Supuestos(costo_hospitalizacion=3000, costo_programa_por_paciente=80, efectividad=0.20)
    r = valor_neto(10_000, 2_400, s)
    assert r["valor_neto"] == pytest.approx(640_000)
