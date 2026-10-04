"""Chequeos de fuga de informacion sobre el dataset procesado (se omiten si aun no existe)."""
import pytest

from dm_hosp.paths import PROCESSED

DATASET = PROCESSED / "dataset_modelado.parquet"
pytestmark = pytest.mark.skipif(not DATASET.exists(), reason="dataset_modelado.parquet no existe aun")


def test_targets_tienen_prefijo_y_no_hay_columnas_prohibidas():
    import pandas as pd

    cols = pd.read_parquet(DATASET).columns
    prohibidas = {"DESTINO_ASEGURADO", "FECATE_POST_FECFED", "destino"}
    assert not (prohibidas & set(cols)), "Columnas prohibidas como predictoras"
    assert "y_hosp_12m" in cols


def test_cortes_esperados():
    import pandas as pd

    df = pd.read_parquet(DATASET, columns=["cut"])
    assert df["cut"].nunique() >= 2
