"""
Configuración centralizada del proyecto.
Laboratorio #3 - INF0157
"""

import os
from pathlib import Path

# Rutas principales
PROJECT_ROOT = Path(__file__).parent.absolute()
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# Archivos de datos
DATA_FILES = {
    "puntos_3d": PROJECT_ROOT / "puntos_3d.npy",
    "kmeans_A": PROJECT_ROOT / "KMeans" / "A.npy",
    "kmeans_labels": PROJECT_ROOT / "KMeans" / "_.npy",
    "meanshift_X": PROJECT_ROOT / "MeanShift" / "X.npy",
    "meanshift_labels": PROJECT_ROOT / "MeanShift" / "_ .npy",
}

# Configuración de KMeans
KMEANS_CONFIG = {
    "n_clusters": 3,
    "random_state": 42,
    "n_init": 10,
    "max_iter": 300,
}

# Configuración de MeanShift
MEANSHIFT_CONFIG = {
    "bandwidth": "scott",
    "cluster_all": True,
}

# Configuración de visualización
PLOT_CONFIG = {
    "figsize": (15, 5),
    "dpi": 100,
    "style": "seaborn-v0_8-darkgrid",
}

# Configuración de regresión lineal
REGRESSION_CONFIG = {
    "test_size": 0.2,
    "random_state": 42,
}

# Crear directorios si no existen
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)
