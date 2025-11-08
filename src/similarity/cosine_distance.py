"""
Módulo de Distancia del Coseno.
Calcula la similitud entre vectores usando la distancia del coseno.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class CosineSimilarity:
    """Calcula similitud usando distancia del coseno."""
    
    @staticmethod
    def cosine_distance(vector_a, vector_b):
        """
        Calcula la distancia del coseno entre dos vectores.
        
        Formula:
        cos(θ) = (A · B) / (||A|| × ||B||)
        
        Args:
            vector_a (np.ndarray): Primer vector
            vector_b (np.ndarray): Segundo vector
            
        Returns:
            float: Similitud del coseno (entre -1 y 1)
        """
        # Asegurar que son arrays de numpy
        a = np.array(vector_a).flatten()
        b = np.array(vector_b).flatten()
        
        # Calcular el producto punto
        dot_product = np.dot(a, b)
        
        # Calcular las normas
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        
        # Evitar división por cero
        if norm_a == 0 or norm_b == 0:
            return 0.0
        
        # Calcular coseno
        cos_theta = dot_product / (norm_a * norm_b)
        
        return cos_theta
    
    @staticmethod
    def cosine_distance_matrix(vectors):
        """
        Calcula la matriz de similitud del coseno.
        
        Args:
            vectors (np.ndarray): Matriz de vectores (n_vectors, n_features)
            
        Returns:
            np.ndarray: Matriz de similitud (n_vectors, n_vectors)
        """
        return cosine_similarity(vectors)
    
    @staticmethod
    def angle_from_cosine(cos_theta):
        """
        Convierte el coseno a ángulo en radianes.
        
        Args:
            cos_theta (float): Valor del coseno
            
        Returns:
            float: Ángulo en radianes
        """
        # Limitar a [-1, 1] por precisión numérica
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        return np.arccos(cos_theta)
    
    @staticmethod
    def angle_from_cosine_degrees(cos_theta):
        """
        Convierte el coseno a ángulo en grados.
        
        Args:
            cos_theta (float): Valor del coseno
            
        Returns:
            float: Ángulo en grados
        """
        radians = CosineSimilarity.angle_from_cosine(cos_theta)
        return np.degrees(radians)


def print_cosine_analysis(vectors_dict):
    """
    Imprime un análisis de similitud del coseno entre vectores.
    
    Args:
        vectors_dict (dict): Diccionario con nombre:vector
    """
    print("\n" + "="*60)
    print("ANÁLISIS DE DISTANCIA DEL COSENO")
    print("="*60)
    
    vector_names = list(vectors_dict.keys())
    
    for i, name_a in enumerate(vector_names):
        for j, name_b in enumerate(vector_names):
            if i < j:  # Evitar duplicados
                v_a = vectors_dict[name_a]
                v_b = vectors_dict[name_b]
                
                cos_sim = CosineSimilarity.cosine_distance(v_a, v_b)
                angle_rad = CosineSimilarity.angle_from_cosine(cos_sim)
                angle_deg = np.degrees(angle_rad)
                
                print(f"\n{name_a} vs {name_b}:")
                print(f"  Cos(θ) = {cos_sim:.6f}")
                print(f"  θ (rad) = {angle_rad:.6f}")
                print(f"  θ (deg) = {angle_deg:.2f}°")
                
                # Interpretación
                if angle_deg == 0:
                    print("  → Vectores idénticos")
                elif angle_deg == 90:
                    print("  → Vectores ortogonales")
                elif angle_deg == 180:
                    print("  → Vectores opuestos")
                else:
                    print(f"  → Ángulo de {angle_deg:.2f}° entre vectores")
