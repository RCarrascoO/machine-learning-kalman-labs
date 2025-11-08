"""
Módulo de KMeans clustering.
"""

import numpy as np
from sklearn.cluster import KMeans as SklearnKMeans
import config


class KMeansModel:
    """Modelo de KMeans personalizado."""
    
    def __init__(self, n_clusters=None, random_state=None, n_init=None, max_iter=None):
        """
        Inicializa el modelo de KMeans.
        
        Args:
            n_clusters (int): Número de clusters
            random_state (int): Seed para reproducibilidad
            n_init (int): Número de inicializaciones
            max_iter (int): Número máximo de iteraciones
        """
        # Usar valores de config si no se proporcionan
        n_clusters = n_clusters or config.KMEANS_CONFIG["n_clusters"]
        random_state = random_state or config.KMEANS_CONFIG["random_state"]
        n_init = n_init or config.KMEANS_CONFIG["n_init"]
        max_iter = max_iter or config.KMEANS_CONFIG["max_iter"]
        
        self.model = SklearnKMeans(
            n_clusters=n_clusters,
            random_state=random_state,
            n_init=n_init,
            max_iter=max_iter
        )
        self.labels = None
        self.centroids = None
        self.inertia = None
    
    def fit(self, X):
        """
        Entrena el modelo de KMeans.
        
        Args:
            X (np.ndarray): Datos de entrenamiento
            
        Returns:
            self: Modelo entrenado
        """
        self.model.fit(X)
        self.labels = self.model.labels_
        self.centroids = self.model.cluster_centers_
        self.inertia = self.model.inertia_
        return self
    
    def predict(self, X):
        """
        Predice las etiquetas para nuevos datos.
        
        Args:
            X (np.ndarray): Datos para predecir
            
        Returns:
            np.ndarray: Etiquetas predichas
        """
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
    
    def get_inertia(self):
        """
        Obtiene la inercia del modelo.
        
        Returns:
            float: Inercia
        """
        return self.inertia
    
    def get_info(self):
        """
        Obtiene información del modelo.
        
        Returns:
            dict: Información del modelo
        """
        info = {
            "n_clusters": self.model.n_clusters,
            "inertia": self.inertia,
            "n_iterations": self.model.n_iter_,
            "centroids_shape": self.centroids.shape if self.centroids is not None else None,
            "n_labels": len(np.unique(self.labels)) if self.labels is not None else None,
        }
        return info
