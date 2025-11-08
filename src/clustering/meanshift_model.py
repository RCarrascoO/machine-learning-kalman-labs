"""
Módulo de MeanShift clustering.
"""

import numpy as np
from sklearn.cluster import MeanShift as SklearnMeanShift
from sklearn.cluster import estimate_bandwidth
import config


class MeanShiftModel:
    """Modelo de MeanShift personalizado."""
    
    def __init__(self, bandwidth=None, cluster_all=None):
        """
        Inicializa el modelo de MeanShift.
        
        Args:
            bandwidth (float o str): Ancho de banda para el kernel
            cluster_all (bool): Si se deben agrupar todos los puntos
        """
        bandwidth = bandwidth or config.MEANSHIFT_CONFIG["bandwidth"]
        cluster_all = cluster_all or config.MEANSHIFT_CONFIG["cluster_all"]
        
        self.bandwidth = bandwidth
        self.cluster_all = cluster_all
        self.model = None
        self.labels = None
        self.centroids = None
        self._is_fitted = False
    
    def fit(self, X):
        """
        Entrena el modelo de MeanShift.
        
        Args:
            X (np.ndarray): Datos de entrenamiento
            
        Returns:
            self: Modelo entrenado
        """
        # Estimar ancho de banda si es necesario
        if self.bandwidth == "scott":
            bandwidth = estimate_bandwidth(X, quantile=0.3)
        else:
            bandwidth = self.bandwidth
        
        self.model = SklearnMeanShift(
            bandwidth=bandwidth,
            cluster_all=self.cluster_all
        )
        self.model.fit(X)
        self.labels = self.model.labels_
        self.centroids = self.model.cluster_centers_
        self._is_fitted = True
        
        return self
    
    def predict(self, X):
        """
        Predice las etiquetas para nuevos datos.
        
        Args:
            X (np.ndarray): Datos para predecir
            
        Returns:
            np.ndarray: Etiquetas predichas
        """
        if not self._is_fitted:
            raise ValueError("El modelo debe ser entrenado primero con fit()")
        
        return self.model.predict(X)
    
    def get_centroids(self):
        """
        Obtiene los centroides del modelo.
        
        Returns:
            np.ndarray: Centroides (n_clusters, n_features)
        """
        return self.centroids
    
    def get_labels(self):
        """
        Obtiene las etiquetas del entrenamiento.
        
        Returns:
            np.ndarray: Etiquetas
        """
        return self.labels
    
    def get_info(self):
        """
        Obtiene información del modelo.
        
        Returns:
            dict: Información del modelo
        """
        info = {
            "n_clusters": len(np.unique(self.labels)) if self.labels is not None else None,
            "centroids_shape": self.centroids.shape if self.centroids is not None else None,
            "bandwidth": self.bandwidth,
            "cluster_all": self.cluster_all,
        }
        return info
