"""Graficos reutilizables (estilo consistente para la presentacion)."""
import matplotlib.pyplot as plt

PALETA = {"azul": "#2E75B6", "rojo": "#C00000", "verde": "#548235", "naranja": "#ED7D31"}


def guardar(fig, nombre: str, carpeta=None, dpi: int = 160) -> None:
    from dm_hosp.paths import FIGURES

    carpeta = carpeta or FIGURES
    carpeta.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(carpeta / nombre, dpi=dpi)
    plt.close(fig)
