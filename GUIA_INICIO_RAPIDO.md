"""
GUÍA DE INICIO RÁPIDO
Laboratorio #3 - INF0157 - Sistemas
"""

📋 CONTENIDOS DEL PROYECTO
==========================

✅ Estructura lista:
   ✓ Arquitectura limpia implementada
   ✓ Módulos separados por responsabilidad
   ✓ Configuración centralizada
   ✓ Documentación completa

📁 DIRECTORIOS PRINCIPALES:
   src/                  - Código fuente
   ├── data_loader.py    - Carga de archivos .npy
   ├── clustering/       - KMeans y MeanShift
   ├── regression/       - Regresión lineal
   ├── similarity/       - Distancia del coseno
   ├── filters/          - Kalman y Complementario
   └── utils/            - Visualización

   notebooks/            - Jupyter Notebooks ejecutables
   └── parte_a_kmeans.ipynb
   └── parte_b_meanshift.ipynb
   └── parte_c_adicionales.ipynb

   tests/                - Tests unitarios

🚀 PASOS PARA EJECUTAR:
=======================

1. CONFIGURAR AMBIENTE VIRTUAL (Windows PowerShell):
   
   # Crear ambiente virtual
   python -m venv .venv
   
   # Activar
   .venv\Scripts\Activate.ps1
   
   # Instalar dependencias
   pip install -r requirements.txt

2. EJECUTAR LOS NOTEBOOKS:
   
   # Iniciar Jupyter
   jupyter notebook notebooks/
   
   # Ejecutar en orden:
   ① parte_a_kmeans.ipynb
   ② parte_b_meanshift.ipynb
   ③ parte_c_adicionales.ipynb

3. EJECUTAR TESTS:
   
   pytest tests/ -v

📊 QUÉ HACE CADA PARTE:
========================

PARTE A - KMeans:
   ✓ Carga datos de A.npy y _.npy
   ✓ Entrena modelo KMeans con 3 clusters
   ✓ Visualiza datos originales
   ✓ Visualiza clusters predichos
   ✓ Muestra información de etiquetas
   ✓ Realiza predicciones en 6 puntos de test

PARTE B - MeanShift:
   ✓ Carga datos de X.npy y _ .npy
   ✓ Entrena modelo MeanShift (detección automática de clusters)
   ✓ Visualiza datos originales
   ✓ Visualiza clusters predichos
   ✓ Muestra información de etiquetas
   ✓ Realiza predicciones en 4 puntos de test

PARTE C - Adicionales:
   
   3. Regresión Lineal:
      ✓ Tabla de Peso vs Altura
      ✓ Entrena modelo lineal
      ✓ Predice en set de test
      ✓ Calcula métricas: R², RMSE, MAE, RSS
      ✓ Visualiza línea de regresión

   4. Distancia del Coseno:
      ✓ Define 6 vectores (A, B, P, Q, S, T)
      ✓ Calcula similitud coseno entre todos los pares
      ✓ Convierte a ángulos en radianes y grados
      ✓ Interpreta resultados

   5. Visualización 3D:
      ✓ Carga puntos_3d.npy
      ✓ Crea DataFrame con coordenadas x, y, z
      ✓ Visualiza puntos sin centroide
      ✓ Calcula y visualiza centroide

   7. Filtro de Kalman:
      ✓ Genera trayectoria sintética
      ✓ Agrega ruido gaussiano
      ✓ Aplica filtro de Kalman
      ✓ Compara con trayectoria real
      ✓ Calcula mejora en error

   8. Filtro Complementario:
      ✓ Genera dos sensores (ruidoso + integrado)
      ✓ Aplica filtro complementario
      ✓ Prueba diferentes valores de alpha
      ✓ Encuentra alpha óptimo
      ✓ Visualiza resultados

🔧 MÓDULOS DISPONIBLES:
========================

from src.data_loader import DataLoader
   - load_3d_points()
   - load_kmeans_data()
   - load_meanshift_data()
   - get_data_info()
   - print_data_info()

from src.clustering.kmeans_model import KMeansModel
   - fit(X)
   - predict(X)
   - get_centroids()
   - get_labels()
   - get_inertia()

from src.clustering.meanshift_model import MeanShiftModel
   - fit(X)
   - predict(X)
   - get_centroids()
   - get_labels()

from src.regression.linear_regression import LinearRegressionModel
   - fit(X, y)
   - predict(X)
   - evaluate(X_test, y_test)
   - get_coefficients()
   - get_equation()

from src.similarity.cosine_distance import CosineSimilarity
   - cosine_distance(v1, v2)
   - cosine_distance_matrix(vectors)
   - angle_from_cosine(cos_theta)
   - angle_from_cosine_degrees(cos_theta)

from src.filters.kalman_filter import KalmanFilter
   - filter(measurements)
   - predict()
   - update(z)
   - get_state()

from src.filters.complementary_filter import ComplementaryFilter
   - filter(measurement_noisy, measurement_integrated)
   - filter_series(measurements_noisy, measurements_integrated)
   - set_alpha(alpha)
   - find_optimal_alpha(...)

from src.utils.visualization import Visualizer
   - plot_2d_clusters(data, labels, centroids, title)
   - plot_3d_points(data, labels, centroids, title)
   - plot_training_vs_clusters(...)
   - plot_regression(X_train, y_train, X_test, y_test, predictions)
   - plot_kalman_filter(measurements, estimates, real_trajectory)
   - plot_complementary_filter(...)

📝 ARCHIVOS CLAVE:
===================

config.py
   - Configuración centralizada
   - Rutas de archivos
   - Parámetros de modelos
   - Configuración de visualización

requirements.txt
   - Todas las dependencias necesarias
   - Versiones especificadas

README.md
   - Documentación completa
   - Ejemplos de uso
   - Estructura del proyecto

❓ PREGUNTAS FRECUENTES:
==========================

P: ¿Dónde están los archivos .npy?
R: Deben estar en la raíz del proyecto:
   - puntos_3d.npy
   - KMeans/A.npy
   - KMeans/_.npy
   - MeanShift/X.npy
   - MeanShift/_ .npy

P: ¿Cómo uso los módulos en mi propio código?
R: Importa desde src y usa directamente:
   from src.clustering.kmeans_model import KMeansModel
   model = KMeansModel()

P: ¿Cómo modifico los parámetros?
R: Edita config.py o pasa parámetros al crear el modelo:
   model = KMeansModel(n_clusters=5, random_state=100)

P: ¿Cómo agrego más gráficos?
R: Edita src/utils/visualization.py y agrega nuevas funciones

✨ CARACTERÍSTICAS:
====================

✓ Arquitectura limpia y escalable
✓ Código modular y reutilizable
✓ Separación de responsabilidades
✓ Fácil de entender y mantener
✓ Bien documentado
✓ Tests unitarios incluidos
✓ Ejemplos completos en notebooks
✓ Parámetros configurables

🎯 OBJETIVOS ALCANZADOS:
==========================

✅ Parte A: KMeans clustering completo
✅ Parte B: MeanShift clustering completo
✅ Sección 3: Regresión lineal con métricas
✅ Sección 4: Distancia del coseno analizada
✅ Sección 5: Visualización 3D con centroide
✅ Sección 7: Filtro de Kalman implementado
✅ Sección 8: Filtro complementario con alpha óptimo

🚀 LISTO PARA USAR - ¡Disfruta del proyecto!
"""
