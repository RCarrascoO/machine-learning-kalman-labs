"""
Tests para módulos de clustering.
"""

import numpy as np
import pytest
from src.clustering.kmeans_model import KMeansModel
from src.clustering.meanshift_model import MeanShiftModel


class TestKMeansModel:
    """Tests para KMeansModel."""
    
    @pytest.fixture
    def sample_data(self):
        """Crea datos de muestra para tests."""
        np.random.seed(42)
        # Crear 3 clusters sintéticos
        cluster1 = np.random.normal(0, 0.5, (30, 2))
        cluster2 = np.random.normal(5, 0.5, (30, 2))
        cluster3 = np.random.normal(10, 0.5, (30, 2))
        return np.vstack([cluster1, cluster2, cluster3])
    
    def test_kmeans_initialization(self):
        """Test inicialización de KMeans."""
        model = KMeansModel(n_clusters=3)
        assert model.model is not None
        assert model.labels is None
        assert model.centroids is None
    
    def test_kmeans_fit(self, sample_data):
        """Test entrenamiento de KMeans."""
        model = KMeansModel(n_clusters=3)
        model.fit(sample_data)
        
        assert model.labels is not None
        assert model.centroids is not None
        assert len(model.labels) == len(sample_data)
        assert model.centroids.shape == (3, 2)
    
    def test_kmeans_predict(self, sample_data):
        """Test predicción de KMeans."""
        model = KMeansModel(n_clusters=3)
        model.fit(sample_data)
        
        new_data = np.array([[0, 0], [5, 5], [10, 10]])
        predictions = model.predict(new_data)
        
        assert len(predictions) == len(new_data)
        assert all(p in [0, 1, 2] for p in predictions)
    
    def test_kmeans_get_info(self, sample_data):
        """Test obtención de información."""
        model = KMeansModel(n_clusters=3)
        model.fit(sample_data)
        
        info = model.get_info()
        assert 'n_clusters' in info
        assert 'inertia' in info
        assert info['n_clusters'] == 3


class TestMeanShiftModel:
    """Tests para MeanShiftModel."""
    
    @pytest.fixture
    def sample_data(self):
        """Crea datos de muestra para tests."""
        np.random.seed(42)
        cluster1 = np.random.normal(0, 0.5, (30, 2))
        cluster2 = np.random.normal(5, 0.5, (30, 2))
        return np.vstack([cluster1, cluster2])
    
    def test_meanshift_initialization(self):
        """Test inicialización de MeanShift."""
        model = MeanShiftModel()
        assert model.model is None
        assert model.labels is None
        assert model.centroids is None
    
    def test_meanshift_fit(self, sample_data):
        """Test entrenamiento de MeanShift."""
        model = MeanShiftModel(bandwidth=1.0)
        model.fit(sample_data)
        
        assert model.labels is not None
        assert model.centroids is not None
        assert len(model.labels) == len(sample_data)
    
    def test_meanshift_predict(self, sample_data):
        """Test predicción de MeanShift."""
        model = MeanShiftModel(bandwidth=1.0)
        model.fit(sample_data)
        
        new_data = np.array([[0, 0], [5, 5]])
        predictions = model.predict(new_data)
        
        assert len(predictions) == len(new_data)
