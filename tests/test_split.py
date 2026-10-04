import pandas as pd
import pytest

from dm_hosp.models.split import separar_xy, split_temporal


def _df():
    return pd.DataFrame({
        "pid": [1, 2, 3, 4],
        "cut": ["2022-12-31", "2023-12-31", "2024-12-31", "2024-12-31"],
        "x": [1, 2, 3, 4],
        "y_hosp_12m": [0, 1, 0, 1],
        "y_costo_12m": [0, 10, 0, 5],
    })


def test_split_respeta_orden_y_no_solapa():
    out = split_temporal(_df(), ["2022-12-31"], ["2023-12-31"], ["2024-12-31"])
    assert len(out["train"]) == 1 and len(out["valid"]) == 1 and len(out["test"]) == 2


def test_split_falla_si_hay_solape():
    with pytest.raises(ValueError):
        split_temporal(_df(), ["2022-12-31"], ["2022-12-31"], ["2024-12-31"])


def test_split_falla_si_orden_incorrecto():
    with pytest.raises(ValueError):
        split_temporal(_df(), ["2024-12-31"], ["2023-12-31"], ["2022-12-31"])


def test_separar_xy_quita_targets_e_ids():
    X, y = separar_xy(_df())
    assert list(X.columns) == ["x"]
    assert y.tolist() == [0, 1, 0, 1]
