"""
Módulo de Filtro de Kalman.
Implementa el filtro de Kalman para estimar la posición de una partícula.
"""

import numpy as np


class KalmanFilter:
    """Filtro de Kalman 1D."""
    
    def __init__(self, dt=0.1, process_variance=1e-5, measurement_variance=1e-2, 
                 initial_position=0, initial_velocity=0):
        """
        Inicializa el filtro de Kalman.
        
        Args:
            dt (float): Intervalo de tiempo
            process_variance (float): Varianza del proceso (Q)
            measurement_variance (float): Varianza de medición (R)
            initial_position (float): Posición inicial
            initial_velocity (float): Velocidad inicial
        """
        self.dt = dt
        self.Q = process_variance  # Varianza del proceso
        self.R = measurement_variance  # Varianza de medición
        
        # Estado: [posición, velocidad]
        self.x = np.array([[initial_position], [initial_velocity]])
        
        # Matriz de covarianza del estado
        self.P = np.eye(2)
        
        # Matriz de transición de estado
        self.F = np.array([[1, dt], [0, 1]])
        
        # Matriz de medición
        self.H = np.array([[1, 0]])
        
        # Ruido del proceso
        self.q = np.array([[dt**2/4, dt/2], [dt/2, 1]]) * process_variance
        
        # Historial de estimaciones
        self.position_history = [initial_position]
        self.measurement_history = []
    
    def predict(self):
        """Paso de predicción del filtro de Kalman."""
        # Predicción del estado
        self.x = self.F @ self.x
        
        # Predicción de la covarianza
        self.P = self.F @ self.P @ self.F.T + self.q
    
    def update(self, z):
        """
        Paso de actualización del filtro de Kalman.
        
        Args:
            z (float): Medición
        """
        # Residuo (innovation)
        y = z - self.H @ self.x
        
        # Covarianza del residuo
        S = self.H @ self.P @ self.H.T + self.R
        
        # Ganancia de Kalman
        K = self.P @ self.H.T / S
        
        # Actualización del estado
        self.x = self.x + K * y
        
        # Actualización de la covarianza
        self.P = (np.eye(2) - K @ self.H) @ self.P
    
    def filter(self, measurements):
        """
        Aplica el filtro a una serie de mediciones.
        
        Args:
            measurements (np.ndarray): Mediciones
            
        Returns:
            np.ndarray: Posiciones estimadas
        """
        self.measurement_history = measurements.copy()
        estimates = [self.x[0, 0]]
        
        for z in measurements:
            self.predict()
            self.update(z)
            self.position_history.append(self.x[0, 0])
            estimates.append(self.x[0, 0])
        
        return np.array(estimates)
    
    def get_state(self):
        """
        Obtiene el estado actual.
        
        Returns:
            tuple: (posición, velocidad)
        """
        return self.x[0, 0], self.x[1, 0]
    
    def get_position_history(self):
        """Obtiene el historial de posiciones."""
        return np.array(self.position_history)
