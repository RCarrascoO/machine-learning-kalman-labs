"""
Módulo para cargar y procesar datos.
Carga archivos .npy y los convierte en DataFrames de pandas.
"""

import numpy as np
import pandas as pd
from pathlib import Path
import config


class DataLoader:
    """Cargador de datos para el proyecto."""
    
    @staticmethod
    def load_3d_points():
        """
        Carga los puntos 3D del archivo puntos_3d.npy
        
        Returns:
            pd.DataFrame: DataFrame con columnas [x, y, z]
        """
        path = config.DATA_FILES["puntos_3d"]
        data = np.load(path)
        df = pd.DataFrame(data, columns=['x', 'y', 'z'])
        return df
    
    @staticmethod
    def load_kmeans_data():
        """
        Carga los datos de KMeans.
        
        Returns:
            tuple: (X: np.ndarray, labels: np.ndarray)
        """
        A = np.load(config.DATA_FILES["kmeans_A"])
        labels = np.load(config.DATA_FILES["kmeans_labels"])
        return A, labels
    
    @staticmethod
    def load_meanshift_data():
        """
        Carga los datos de MeanShift.
        
        Returns:
            tuple: (X: np.ndarray, labels: np.ndarray)
        """
        X = np.load(config.DATA_FILES["meanshift_X"])
        labels = np.load(config.DATA_FILES["meanshift_labels"])
        return X, labels
    
    @staticmethod
    def get_data_info(data, labels):
        """
        Obtiene información sobre los datos.
        
        Args:
            data (np.ndarray): Datos de entrada
            labels (np.ndarray): Etiquetas de los datos
            
        Returns:
            dict: Información sobre los datos
        """
        unique_labels = np.unique(labels)
        info = {
            "total_points": len(data),
            "total_classes": len(unique_labels),
            "classes": unique_labels,
            "data_shape": data.shape,
            "labels_shape": labels.shape,
            "samples_per_class": {
                cls: np.sum(labels == cls) for cls in unique_labels
            }
        }
        return info


def print_data_info(data, labels, title=""):
    """
    Imprime información sobre los datos.
    
    Args:
        data (np.ndarray): Datos
        labels (np.ndarray): Etiquetas
        title (str): Título para mostrar
    """
    info = DataLoader.get_data_info(data, labels)
    
    if title:
        print(f"\n{'='*50}")
        print(f"{title}")
        print(f"{'='*50}")
    
    print(f"📊 Total de puntos: {info['total_points']}")
    print(f"🏷️  Total de clases: {info['total_classes']}")
    print(f"📐 Forma de los datos: {info['data_shape']}")
    print(f"\n📈 Distribución por clase:")
    for cls, count in info['samples_per_class'].items():
        print(f"   Clase {int(cls)}: {count} puntos")
