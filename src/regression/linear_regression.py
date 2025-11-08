"""
Módulo de Regresión Lineal.
Predice el peso a partir de la altura de una persona.
"""

import numpy as np
from sklearn.linear_model import LinearRegression as SklearnLinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import config


class LinearRegressionModel:
    """Modelo de Regresión Lineal personalizado."""
    
    def __init__(self):
        """Inicializa el modelo de regresión lineal."""
        self.model = SklearnLinearRegression()
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.predictions = None
        self._is_fitted = False
    
    def fit(self, X, y):
        """
        Entrena el modelo de regresión lineal.
        
        Args:
            X (np.ndarray): Características de entrenamiento (altura)
            y (np.ndarray): Valores objetivo (peso)
            
        Returns:
            self: Modelo entrenado
        """
        self.X_train = X
        self.y_train = y
        self.model.fit(X, y)
        self._is_fitted = True
        return self
    
    def predict(self, X):
        """
        Realiza predicciones.
        
        Args:
            X (np.ndarray): Características para predecir
            
        Returns:
            np.ndarray: Predicciones
        """
        if not self._is_fitted:
            raise ValueError("El modelo debe ser entrenado primero con fit()")
        
        self.predictions = self.model.predict(X)
        return self.predictions
    
    def evaluate(self, X_test, y_test):
        """
        Evalúa el modelo en datos de prueba.
        
        Args:
            X_test (np.ndarray): Características de prueba
            y_test (np.ndarray): Valores objetivo de prueba
            
        Returns:
            dict: Métricas de evaluación
        """
        self.X_test = X_test
        self.y_test = y_test
        predictions = self.predict(X_test)
        
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, predictions)
        mae = np.mean(np.abs(y_test - predictions))
        
        metrics = {
            "mse": mse,
            "rmse": rmse,
            "r2": r2,
            "mae": mae,
        }
        
        return metrics
    
    def get_coefficients(self):
        """
        Obtiene los coeficientes del modelo.
        
        Returns:
            tuple: (slope, intercept)
        """
        if not self._is_fitted:
            raise ValueError("El modelo debe ser entrenado primero")
        
        return self.model.coef_[0], self.model.intercept_
    
    def get_equation(self):
        """
        Obtiene la ecuación del modelo.
        
        Returns:
            str: Ecuación del modelo (y = mx + b)
        """
        if not self._is_fitted:
            raise ValueError("El modelo debe ser entrenado primero")
        
        m, b = self.get_coefficients()
        return f"Peso = {m:.4f} × Altura + {b:.4f}"
    
    def get_info(self):
        """
        Obtiene información del modelo.
        
        Returns:
            dict: Información del modelo
        """
        info = {
            "coefficient": self.model.coef_[0] if self._is_fitted else None,
            "intercept": self.model.intercept_ if self._is_fitted else None,
            "is_fitted": self._is_fitted,
            "equation": self.get_equation() if self._is_fitted else None,
        }
        return info
