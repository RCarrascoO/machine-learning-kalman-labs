"""
Módulo de Filtro Complementario.
Combina múltiples fuentes de datos usando filtro complementario.
"""

import numpy as np


class ComplementaryFilter:
    """Filtro complementario para fusión de sensores."""
    
    def __init__(self, alpha=0.95, dt=0.1):
        """
        Inicializa el filtro complementario.
        
        Args:
            alpha (float): Factor de peso para integración (0 a 1)
            dt (float): Intervalo de tiempo
        """
        self.alpha = alpha
        self.dt = dt
        self.position = 0.0
        self.velocity = 0.0
        self.acceleration = 0.0
        
        self.position_history = [0.0]
        self.velocity_history = [0.0]
    
    def filter(self, measurement_noisy, measurement_integrated):
        """
        Aplica el filtro complementario.
        
        El filtro combina una medición ruidosa pero sin drift
        con una medición integrada que tiene drift.
        
        Args:
            measurement_noisy (float): Medición ruidosa (sensor directo)
            measurement_integrated (float): Medición integrada (acelerómetro integrado)
            
        Returns:
            float: Estimación filtrada
        """
        # Combinar usando alpha
        estimate = (self.alpha * measurement_noisy + 
                   (1 - self.alpha) * measurement_integrated)
        
        # Actualizar posición
        self.position = estimate
        
        # Actualizar historial
        self.position_history.append(self.position)
        
        return estimate
    
    def filter_series(self, measurements_noisy, measurements_integrated):
        """
        Aplica el filtro a series de tiempo.
        
        Args:
            measurements_noisy (np.ndarray): Mediciones ruidosas
            measurements_integrated (np.ndarray): Mediciones integradas
            
        Returns:
            np.ndarray: Series filtradas
        """
        estimates = []
        for m_noisy, m_integrated in zip(measurements_noisy, measurements_integrated):
            est = self.filter(m_noisy, m_integrated)
            estimates.append(est)
        
        return np.array(estimates)
    
    def get_position_history(self):
        """Obtiene el historial de posiciones."""
        return np.array(self.position_history)
    
    def get_alpha(self):
        """Obtiene el factor alpha actual."""
        return self.alpha
    
    def set_alpha(self, alpha):
        """
        Establece un nuevo factor alpha.
        
        Args:
            alpha (float): Nuevo factor (0 a 1)
        """
        if not 0 <= alpha <= 1:
            raise ValueError("Alpha debe estar entre 0 y 1")
        self.alpha = alpha
    
    @staticmethod
    def find_optimal_alpha(measurements_noisy, measurements_integrated, 
                          reference_measurements):
        """
        Encuentra el alpha óptimo comparando contra una referencia.
        
        Args:
            measurements_noisy (np.ndarray): Mediciones ruidosas
            measurements_integrated (np.ndarray): Mediciones integradas
            reference_measurements (np.ndarray): Mediciones de referencia
            
        Returns:
            float: Valor óptimo de alpha
        """
        alphas = np.linspace(0, 1, 21)
        errors = []
        
        for alpha in alphas:
            cf = ComplementaryFilter(alpha=alpha)
            estimates = cf.filter_series(measurements_noisy, measurements_integrated)
            error = np.mean((estimates - reference_measurements) ** 2)
            errors.append(error)
        
        optimal_alpha = alphas[np.argmin(errors)]
        return optimal_alpha
