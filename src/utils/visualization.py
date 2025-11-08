"""
Módulo de Visualización.
Funciones para visualizar datos, clusters y resultados.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import config


class Visualizer:
    """Clase para visualización de datos."""
    
    @staticmethod
    def plot_2d_clusters(data, labels, centroids=None, title="Clusters 2D"):
        """
        Grafica clusters en 2D.
        
        Args:
            data (np.ndarray): Datos (n_samples, 2)
            labels (np.ndarray): Etiquetas de cluster
            centroids (np.ndarray): Centroides
            title (str): Título del gráfico
        """
        plt.figure(figsize=config.PLOT_CONFIG["figsize"])
        
        # Scatter plot de los datos
        scatter = plt.scatter(data[:, 0], data[:, 1], c=labels, 
                            cmap='viridis', s=50, alpha=0.6, edgecolors='k')
        
        # Plotear centroides si existen
        if centroids is not None:
            plt.scatter(centroids[:, 0], centroids[:, 1], c='red', 
                       marker='X', s=300, edgecolors='black', linewidths=2,
                       label='Centroides')
        
        plt.xlabel('Característica 1')
        plt.ylabel('Característica 2')
        plt.title(title)
        plt.colorbar(scatter, label='Cluster')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        return plt.gcf()
    
    @staticmethod
    def plot_3d_points(data, labels=None, centroids=None, title="Puntos 3D"):
        """
        Grafica puntos en 3D.
        
        Args:
            data (np.ndarray): Datos (n_samples, 3)
            labels (np.ndarray): Etiquetas de cluster
            centroids (np.ndarray): Centroides
            title (str): Título del gráfico
        """
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        if labels is None:
            labels = np.zeros(len(data))
        
        # Scatter plot de los datos
        scatter = ax.scatter(data[:, 0], data[:, 1], data[:, 2], 
                           c=labels, cmap='viridis', s=50, alpha=0.6)
        
        # Plotear centroides si existen
        if centroids is not None:
            ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2],
                      c='red', marker='X', s=300, edgecolors='black', linewidths=2)
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(title)
        plt.colorbar(scatter, ax=ax, label='Cluster')
        
        return fig
    
    @staticmethod
    def plot_training_vs_clusters(original_data, original_labels, 
                                 clustered_data, cluster_labels, 
                                 centroids=None):
        """
        Compara datos originales con clusters.
        
        Args:
            original_data (np.ndarray): Datos originales
            original_labels (np.ndarray): Etiquetas originales
            clustered_data (np.ndarray): Datos agrupados
            cluster_labels (np.ndarray): Etiquetas de clusters
            centroids (np.ndarray): Centroides
        """
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Gráfico original
        scatter1 = axes[0].scatter(original_data[:, 0], original_data[:, 1],
                                  c=original_labels, cmap='viridis', s=50,
                                  alpha=0.6, edgecolors='k')
        axes[0].set_title('Datos Originales')
        axes[0].set_xlabel('Característica 1')
        axes[0].set_ylabel('Característica 2')
        plt.colorbar(scatter1, ax=axes[0], label='Clase')
        
        # Gráfico de clusters
        scatter2 = axes[1].scatter(clustered_data[:, 0], clustered_data[:, 1],
                                  c=cluster_labels, cmap='viridis', s=50,
                                  alpha=0.6, edgecolors='k')
        if centroids is not None:
            axes[1].scatter(centroids[:, 0], centroids[:, 1], c='red',
                           marker='X', s=300, edgecolors='black', linewidths=2)
        axes[1].set_title('Clusters')
        axes[1].set_xlabel('Característica 1')
        axes[1].set_ylabel('Característica 2')
        plt.colorbar(scatter2, ax=axes[1], label='Cluster')
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def plot_regression(X_train, y_train, X_test, y_test, predictions, 
                       equation=""):
        """
        Grafica la regresión lineal.
        
        Args:
            X_train (np.ndarray): X de entrenamiento
            y_train (np.ndarray): y de entrenamiento
            X_test (np.ndarray): X de prueba
            y_test (np.ndarray): y de prueba
            predictions (np.ndarray): Predicciones
            equation (str): Ecuación del modelo
        """
        plt.figure(figsize=(10, 6))
        
        # Datos de entrenamiento
        plt.scatter(X_train, y_train, color='blue', s=50, alpha=0.6, 
                   label='Datos de entrenamiento')
        
        # Datos de prueba
        plt.scatter(X_test, y_test, color='green', s=50, alpha=0.6,
                   label='Datos de prueba')
        
        # Línea de regresión
        sort_idx = np.argsort(X_test.flatten())
        plt.plot(X_test[sort_idx], predictions[sort_idx], 'r-', linewidth=2,
                label='Línea de regresión')
        
        plt.xlabel('Altura (m)')
        plt.ylabel('Peso (kg)')
        plt.title('Regresión Lineal: Predicción de Peso a partir de Altura')
        if equation:
            plt.text(0.05, 0.95, equation, transform=plt.gca().transAxes,
                    verticalalignment='top', bbox=dict(boxstyle='round', 
                    facecolor='wheat', alpha=0.5), fontsize=10)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        return plt.gcf()
    
    @staticmethod
    def plot_kalman_filter(measurements, estimates, real_trajectory=None):
        """
        Grafica el resultado del filtro de Kalman.
        
        Args:
            measurements (np.ndarray): Mediciones ruidosas
            estimates (np.ndarray): Estimaciones filtradas
            real_trajectory (np.ndarray): Trayectoria real (opcional)
        """
        plt.figure(figsize=(12, 5))
        
        time = np.arange(len(measurements))
        
        plt.plot(time, measurements, 'o-', label='Mediciones (ruidosas)',
                alpha=0.6, markersize=4)
        plt.plot(time, estimates, 's-', label='Estimaciones (Kalman)',
                alpha=0.8, markersize=4)
        
        if real_trajectory is not None:
            plt.plot(time, real_trajectory, 'g--', label='Trayectoria real',
                    alpha=0.8, linewidth=2)
        
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Posición (m)')
        plt.title('Filtro de Kalman')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        return plt.gcf()
    
    @staticmethod
    def plot_complementary_filter(measurements_noisy, measurements_integrated,
                                estimates, reference=None):
        """
        Grafica el resultado del filtro complementario.
        
        Args:
            measurements_noisy (np.ndarray): Mediciones ruidosas
            measurements_integrated (np.ndarray): Mediciones integradas
            estimates (np.ndarray): Estimaciones filtradas
            reference (np.ndarray): Referencia (opcional)
        """
        plt.figure(figsize=(12, 5))
        
        time = np.arange(len(estimates))
        
        plt.plot(time, measurements_noisy, 'o-', label='Sensor ruidoso',
                alpha=0.5, markersize=3)
        plt.plot(time, measurements_integrated, 's-', label='Integrado',
                alpha=0.5, markersize=3)
        plt.plot(time, estimates, 'r-', label='Filtro Complementario',
                alpha=0.8, linewidth=2)
        
        if reference is not None:
            plt.plot(time, reference, 'g--', label='Referencia',
                    alpha=0.8, linewidth=2)
        
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Valor')
        plt.title('Filtro Complementario')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        return plt.gcf()
