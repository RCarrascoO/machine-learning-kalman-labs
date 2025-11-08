# Mapeo de Rúbrica - Laboratorio #3
## Renato Carrasco - INF0157

### Total: 14 Puntos Brutos

---

## ✅ CHECKLIST DE PUNTOS

### 1. KMeans (2 Puntos) → `parte_a_kmeans.ipynb`
- [x] 0.5 Puntos: Implementación correcta de KMeans
- [x] 0.5 Puntos: Visualización correcta de blobs coloreados y clusters con centroides
- [x] 1.0 Puntos: Predicción precisa y asignación correcta de puntos de prueba a sus clases

**Ubicación:** Notebook `notebooks/parte_a_kmeans.ipynb`
- Celdas 3-4: Carga de datos
- Celdas 6-8: Entrenamiento del modelo
- Celdas 9-11: Visualización con centroides
- Celdas 12-17: Predicción de 6 puntos de prueba

---

### 2. MeanShift (2 Puntos) → `parte_b_meanshift.ipynb`
- [x] 0.5 Puntos: Implementación correcta de MeanShift
- [x] 0.5 Puntos: Visualización correcta de blobs coloreados y clusters con centroides
- [x] 1.0 Puntos: Predicción precisa y asignación correcta de puntos de prueba a sus clases

**Ubicación:** Notebook `notebooks/parte_b_meanshift.ipynb`
- Celdas 3-4: Carga de datos
- Celdas 6-8: Entrenamiento del modelo
- Celdas 9-11: Visualización con centroides
- Celdas 12-17: Predicción de 4 puntos de prueba

---

### 3. Regresión Lineal (1 Punto) → `parte_c_adicionales.ipynb` Sección 3
- [x] 0.5 Puntos: Implementación correcta de Regresión Lineal y predicción de pesos para alturas dadas
- [x] 0.5 Puntos: Cálculo y reporte correctos del RSS del predictor

**Ubicación:** Notebook `notebooks/parte_c_adicionales.ipynb`
- Celdas 6-7: Entrenamiento del modelo de regresión
- Celda 10: Predicción en 5 alturas de prueba
- Celda 12: Cálculo de métricas incluyendo RSS
- Celda 14: Visualización de la línea de regresión

---

### 4. Distancia del Coseno (2 Puntos) → `parte_c_adicionales.ipynb` Sección 4
- [x] 0.5 Puntos: Cálculo correcto de la Distancia del Coseno para todos los pares de vectores
- [x] 0.5 Puntos: Explicación clara de los resultados de Cos(A,B), Cos(P,Q), Cos(S,T)
- [x] 0.5 Puntos: Determinación correcta de los ángulos
- [x] 0.5 Puntos: Explicación clara del significado de 0 rad y π/2 rad

**Ubicación:** Notebook `notebooks/parte_c_adicionales.ipynb`
- Celda 17: Definición de 6 vectores (A, B, P, Q, S, T)
- Celda 19: Cálculo de similitud del coseno para todos los pares
- Celda 21: Análisis e interpretación de ángulos
- Explicación de 0° (vectores idénticos) y 90° (vectores ortogonales)

---

### 5. Visualización de Centroide 3D (1 Punto) → `parte_c_adicionales.ipynb` Sección 5
- [x] 0.5 Puntos: Procesamiento correcto de puntos_3d.npy en un DataFrame de 3 columnas
- [x] 0.5 Puntos: Visualización correcta del centroide en color azul en el gráfico 3D

**Ubicación:** Notebook `notebooks/parte_c_adicionales.ipynb`
- Celda 24: Carga de puntos_3d.npy
- Celda 26: Visualización 3D sin centroide
- Celda 28: Cálculo del centroide
- Celda 30: Visualización 3D con centroide en azul

---

### 6. KMeans en Dataset Iris (2 Puntos) → `parte_6_kmeans_iris.ipynb`
- [x] 1.0 Puntos: Script completado correctamente usando load_iris y Kmeans de sklearn
- [x] 1.0 Puntos: Visualización correcta del dataset Iris clusterizado

**Ubicación:** Notebook `notebooks/parte_6_kmeans_iris.ipynb`
- Celda 2: Importación de load_iris y KMeans de sklearn
- Celda 4: Carga del dataset Iris
- Celda 6: Aplicación de KMeans con 3 clusters
- Celda 8: Visualización 2D del dataset clusterizado con centroides
- Celda 10: Visualización de todas las combinaciones de características
- Celda 12: Métricas de evaluación (ARI, Silhouette)

---

### 7. Filtro de Kalman (3 Puntos) → `parte_c_adicionales.ipynb` Sección 7
- [x] 1.0 Puntos: Implementación correcta y aplicación correctas del Filtro de Kalman
- [x] 1.0 Puntos: Generación correcta de mediciones y la trayectoria real
- [x] 1.0 Puntos: Gráfico claro y preciso con mediciones, trayectoria real y predicción del filtro

**Ubicación:** Notebook `notebooks/parte_c_adicionales.ipynb`
- Celda 40: Generación de trayectoria sintética con ruido
- Celda 42: Aplicación del Filtro de Kalman
- Celda 44: Gráfico comparativo con 3 líneas (mediciones ruidosas, trayectoria real, estimación filtrada)
- Comparación de métricas de error

---

### 8. Filtro Complementario (1 Punto) → `parte_c_adicionales.ipynb` Sección 8
- [x] 0.5 Puntos: Implementación y aplicación correctas del Filtro Complementario
- [x] 0.5 Puntos: Selección apropiada de Alpha y visualización clara de la curva suavizada

**Ubicación:** Notebook `notebooks/parte_c_adicionales.ipynb`
- Celda 47: Generación de dos streams de sensores (ruidoso e integrado)
- Celda 49: Aplicación del Filtro Complementario con diferentes alphas
- Celda 51: Búsqueda del alpha óptimo
- Visualización de la fusión de sensores con curva suavizada

---

## 📋 Archivos del Proyecto

```
notebooks/
├── parte_a_kmeans.ipynb          → Punto 1 (2 puntos)
├── parte_b_meanshift.ipynb       → Punto 2 (2 puntos)
├── parte_c_adicionales.ipynb     → Puntos 3, 4, 5, 7, 8 (8 puntos)
└── parte_6_kmeans_iris.ipynb     → Punto 6 (2 puntos)
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
