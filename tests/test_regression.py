"""
Tests para módulos de regresión.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pytest
from src.regression.linear_regression import LinearRegressionModel


class TestLinearRegression:
    """Tests para LinearRegressionModel."""
    
    @pytest.fixture
    def sample_data(self):
        """Crea datos de muestra para tests."""
        np.random.seed(42)
        X = np.linspace(0, 10, 50).reshape(-1, 1)
        y = 2 * X.flatten() + 3 + np.random.normal(0, 1, 50)
        return X, y
    
    def test_linear_regression_initialization(self):
        """Test inicialización del modelo."""
        model = LinearRegressionModel()
        assert model._is_fitted is False
    
    def test_linear_regression_fit(self, sample_data):
        """Test entrenamiento del modelo."""
        X, y = sample_data
        model = LinearRegressionModel()
        model.fit(X, y)
        
        assert model._is_fitted is True
        assert model.X_train is not None
        assert model.y_train is not None
    
    def test_linear_regression_predict(self, sample_data):
        """Test predicción."""
        X, y = sample_data
        model = LinearRegressionModel()
        model.fit(X, y)
        
        predictions = model.predict(X[:5])
        assert len(predictions) == 5
    
    def test_linear_regression_coefficients(self, sample_data):
        """Test obtención de coeficientes."""
        X, y = sample_data
        model = LinearRegressionModel()
        model.fit(X, y)
        
        slope, intercept = model.get_coefficients()
        assert isinstance(slope, float) or isinstance(slope, np.floating)
        assert isinstance(intercept, float) or isinstance(intercept, np.floating)
    
    def test_linear_regression_equation(self, sample_data):
        """Test obtención de ecuación."""
        X, y = sample_data
        model = LinearRegressionModel()
        model.fit(X, y)
        
        equation = model.get_equation()
        assert isinstance(equation, str)
        assert "Peso" in equation or "=" in equation
