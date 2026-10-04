"""Particion temporal: train / valid / test por corte (nunca aleatoria)."""
import pandas as pd


def split_temporal(df: pd.DataFrame, cortes_train, cortes_valid, cortes_test, col: str = "cut") -> dict:
    """Devuelve {'train','valid','test'} filtrando por la columna de corte.

    Verifica que los conjuntos no se solapen y que respeten el orden temporal.
    """
    c = pd.to_datetime(df[col])
    tr, va, te = (set(pd.to_datetime(x)) for x in (cortes_train, cortes_valid, cortes_test))
    if tr & va or tr & te or va & te:
        raise ValueError("Los cortes de train/valid/test se solapan.")
    if not (max(tr) < min(va) < min(te)):
        raise ValueError("Se espera train < valid < test en el tiempo.")
    out = {"train": df[c.isin(tr)], "valid": df[c.isin(va)], "test": df[c.isin(te)]}
    vacios = [k for k, v in out.items() if v.empty]
    if vacios:
        raise ValueError(f"Conjuntos vacios: {vacios}. Revisa los cortes en config.yaml.")
    return out


def separar_xy(df: pd.DataFrame, target: str = "y_hosp_12m", id_cols=("pid", "cut")):
    """Separa X (features) de y; elimina todas las columnas y_* y los identificadores."""
    ys = [c for c in df.columns if c.startswith("y_")]
    X = df.drop(columns=ys + [c for c in id_cols if c in df.columns])
    return X, df[target]
