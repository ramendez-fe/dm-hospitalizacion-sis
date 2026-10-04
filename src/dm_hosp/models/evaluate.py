"""Metricas de evaluacion alineadas al negocio (capacidad limitada: top K %)."""
import numpy as np


def _n_top(n: int, k_frac: float) -> int:
    return max(1, int(np.ceil(n * k_frac)))


def top_k_idx(y_score, k_frac: float):
    y_score = np.asarray(y_score)
    return np.argsort(-y_score, kind="stable")[: _n_top(len(y_score), k_frac)]


def precision_at_k(y_true, y_score, k_frac: float = 0.10) -> float:
    y_true = np.asarray(y_true)
    return float(y_true[top_k_idx(y_score, k_frac)].mean())


def recall_at_k(y_true, y_score, k_frac: float = 0.10) -> float:
    y_true = np.asarray(y_true)
    total = y_true.sum()
    return float(y_true[top_k_idx(y_score, k_frac)].sum() / total) if total else float("nan")


def lift_at_k(y_true, y_score, k_frac: float = 0.10) -> float:
    base = float(np.asarray(y_true).mean())
    return precision_at_k(y_true, y_score, k_frac) / base if base else float("nan")


def evaluar(y_true, y_score, ks=(0.05, 0.10, 0.20)) -> dict:
    """PR-AUC, ROC-AUC, Brier y Precision/Recall/Lift @K."""
    from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score

    out = {
        "pr_auc": average_precision_score(y_true, y_score),
        "roc_auc": roc_auc_score(y_true, y_score),
        "brier": brier_score_loss(y_true, y_score),
        "tasa_base": float(np.mean(y_true)),
    }
    for k in ks:
        out[f"precision@{int(k * 100)}%"] = precision_at_k(y_true, y_score, k)
        out[f"recall@{int(k * 100)}%"] = recall_at_k(y_true, y_score, k)
        out[f"lift@{int(k * 100)}%"] = lift_at_k(y_true, y_score, k)
    return out
