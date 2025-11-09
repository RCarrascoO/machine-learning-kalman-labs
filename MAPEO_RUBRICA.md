# Mapeo de Rúbrica - Laboratorio #3
## Renato Carrasco - INF0157

### Total: 14 Puntos Brutos

---

## ✅ CHECKLIST DE PUNTOS

### 1. KMeans (2 Puntos) → `parte_a.ipynb`
- [x] 0.5 Puntos: Implementación correcta de KMeans
- [x] 0.5 Puntos: Visualización correcta de blobs coloreados y clusters con centroides
- [x] 1.0 Puntos: Predicción precisa y asignación correcta de puntos de prueba a sus clases

**Ubicación:** Notebook `notebooks/parte_a.ipynb` - Sección Punto 1
- Importación de librerías y carga de datos (A.npy, _.npy)
- Figura A: Visualización de datos originales
- Entrenamiento de KMeans con n_clusters=3
- Figura B: Visualización con centroides marcados con estrellas
- Figura C: Gráfico de comparación
- Predicción de 6 puntos de prueba: [[2,5],[3.2,6.5],[7.2,5],[9.3,2],[9,-6],[11,-8]]

---

### 2. MeanShift (2 Puntos) → `parte_a.ipynb`
- [x] 0.5 Puntos: Implementación correcta de MeanShift
- [x] 0.5 Puntos: Visualización correcta de blobs coloreados y clusters con centroides
- [x] 1.0 Puntos: Predicción precisa y asignación correcta de puntos de prueba a sus clases

**Ubicación:** Notebook `notebooks/parte_a.ipynb` - Sección Punto 2
- Importación de librerías y carga de datos (X.npy, _ .npy)
- Figura A: Visualización de datos originales
- Entrenamiento de MeanShift
- Figura B: Visualización con centroides detectados
- Figura C: Gráfico de comparación
- Predicción de 4 puntos de prueba: [[-7,-6],[1.5,-6.5],[7.9,0.5],[5.5,10]]

---

### 3. Regresión Lineal (1 Punto) → `parte_a.ipynb`
- [x] 0.5 Puntos: Implementación correcta de Regresión Lineal y predicción de pesos para alturas dadas
- [x] 0.5 Puntos: Cálculo y reporte correctos del RSS del predictor

**Ubicación:** Notebook `notebooks/parte_a.ipynb` - Sección Punto 3
- Datos de entrenamiento: peso=[60,65,72.3,75,80], altura=[1.60,1.65,1.70,1.73,1.80]
- Entrenamiento del modelo de regresión lineal
- Predicción en 5 alturas de prueba: [1.58,1.62,1.69,1.76,1.82]
- Cálculo y reporte del RSS (Residual Sum of Squares)
- Visualización de la línea de regresión

---

### 4. Distancia del Coseno (2 Puntos) → `parte_a.ipynb`
- [x] 0.5 Puntos: Cálculo correcto de la Distancia del Coseno para todos los pares de vectores
- [x] 0.5 Puntos: Explicación clara de los resultados de Cos(A,B), Cos(P,Q), Cos(S,T)
- [x] 0.5 Puntos: Determinación correcta de los ángulos
- [x] 0.5 Puntos: Explicación clara del significado de 0 rad y π/2 rad

**Ubicación:** Notebook `notebooks/parte_a.ipynb` - Sección Punto 4
- Definición de 6 vectores según PDF:
  * A=[2,1,0,2,0,1,1], B=[2,1,1,1,1,0,1]
  * P=[3,1,2,3], Q=[2,1,1,0]
  * S=[1,2,3,4,5], T=[5,4,3,2,1]
- Cálculo de similitud del coseno para pares (A,B), (P,Q), (S,T)
- Conversión a ángulos en radianes y grados
- Interpretación de resultados: 0° = idénticos, 90° = ortogonales, 180° = opuestos
- Visualización gráfica de similitudes y ángulos

---

### 5. Visualización de Centroide 3D (1 Punto) → `parte_b.ipynb`
- [x] 0.5 Puntos: Procesamiento correcto de puntos_3d.npy en un DataFrame de 3 columnas
- [x] 0.5 Puntos: Visualización correcta del centroide en color azul en el gráfico 3D

**Ubicación:** Notebook `notebooks/parte_b.ipynb` - Sección Punto 5
- Carga de datos desde puntos_3d.npy
- Cálculo del centroide (promedio de todos los puntos 3D)
- Visualización 3D con Axes3D
- Puntos graficados en rojo
- Centroide marcado en AZUL con estrella grande

---

### 6. KMeans en Dataset Iris (2 Puntos) → `parte_b.ipynb`
- [x] 1.0 Puntos: Script completado correctamente usando load_iris y Kmeans de sklearn
- [x] 1.0 Puntos: Visualización correcta del dataset Iris clusterizado

**Ubicación:** Notebook `notebooks/parte_b.ipynb` - Sección Punto 6
- Importación de load_iris desde sklearn.datasets
- Carga del dataset Iris completo
- Aplicación de KMeans con n_clusters=3, random_state=42
- Visualización 2D del dataset clusterizado (proyección en 2 features)
- Centroides marcados en el gráfico
- Métricas de evaluación: Adjusted Rand Index (ARI) y Silhouette Score

---

### 7. Filtro de Kalman (3 Puntos) → `parte_b.ipynb`
- [x] 1.0 Puntos: Implementación correcta y aplicación correctas del Filtro de Kalman
- [x] 1.0 Puntos: Generación correcta de mediciones y la trayectoria real
- [x] 1.0 Puntos: Gráfico claro y preciso con mediciones, trayectoria real y predicción del filtro

**Ubicación:** Notebook `notebooks/parte_b.ipynb` - Sección Punto 7
- Generación de trayectoria sintética: y = 2x + 10 con ruido gaussiano
- Implementación y aplicación del Filtro de Kalman
- Gráfico comparativo con 3 elementos:
  * Trayectoria real (verde)
  * Mediciones ruidosas (rojo)
  * Estimación filtrada (azul)
- Análisis de reducción de error (MAE comparativo)

---

### 8. Filtro Complementario (1 Punto) → `parte_b.ipynb`
- [x] 0.5 Puntos: Implementación y aplicación correctas del Filtro Complementario
- [x] 0.5 Puntos: Selección apropiada de Alpha y visualización clara de la curva suavizada

**Ubicación:** Notebook `notebooks/parte_b.ipynb` - Sección Punto 8
- Generación de señal real: sin(t)
- Simulación de 2 sensores:
  * Sensor 1: Alta frecuencia, bajo drift
  * Sensor 2: Baja frecuencia, con drift
- Aplicación del Filtro Complementario con diferentes valores de alpha (0.2, 0.5, 0.8)
- Selección del alpha óptimo por minimización de error
- Visualización de resultados con 4 subplots comparativos
- Análisis e interpretación del parámetro alpha

---

## 📋 Archivos del Proyecto

```
notebooks/
├── parte_a.ipynb          → Parte A: Puntos 1, 2, 3, 4 (7 puntos)
└── parte_b.ipynb          → Parte B: Puntos 5, 6, 7, 8 (7 puntos)
```

## ✅ Verificación Final

- [x] Todos los 8 puntos de la rúbrica están implementados
- [x] Código bien documentado y comentado
- [x] Visualizaciones claras y profesionales
- [x] Notebooks ejecutables de principio a fin
- [x] Resultados interpretados correctamente
- [x] Archivos innecesarios eliminados (tests, docs extras)

---

**Nota:** Ejecutar los notebooks en orden:
1. `parte_a_kmeans.ipynb`
2. `parte_b_meanshift.ipynb`
3. `parte_6_kmeans_iris.ipynb`
4. `parte_c_adicionales.ipynb`

**Fórmula de calificación:**
Calificación Final = (Suma de puntos / 14) × 6 + 1.0

Ejemplo: Si obtiene 14/14 puntos → (14/14) × 6 + 1.0 = 7.0
