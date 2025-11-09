# ✅ VALIDACIÓN COMPLETA vs PDF - Laboratorio #3

**Fecha de validación:** 8 de Noviembre, 2025  
**Proyecto:** INF0157 - Laboratorio #3  
**Estudiante:** Renato Carrasco

---

## 📋 VERIFICACIÓN PUNTO POR PUNTO

### **PARTE A** (`parte_a.ipynb`)

#### ✅ Punto 1: KMeans (2 puntos)
- **Datos de entrenamiento:** ✓
  - Archivo: `KMeans/A.npy`
  - Etiquetas: `KMeans/_.npy`
- **Figuras requeridas:** ✓
  - Figura A: Datos originales
  - Figura B: Clusters con centroides (estrellas)
  - Figura C: Comparación
- **Preguntas respondidas:** ✓
  - Pregunta 4: Etiquetas y cantidad de datos
  - Pregunta 5: Predicción de 6 puntos de test
  - Pregunta 6: Clasificación detallada
- **Puntos de test (PDF):** ✓
  ```python
  [[2,5], [3.2,6.5], [7.2,5], [9.3,2], [9,-6], [11,-8]]
  ```

#### ✅ Punto 2: MeanShift (2 puntos)
- **Datos de entrenamiento:** ✓
  - Archivo: `MeanShift/X.npy`
  - Etiquetas: `MeanShift/_ .npy`
- **Figuras requeridas:** ✓
  - Figura A: Datos originales
  - Figura B: Clusters con centroides
  - Figura C: Comparación
- **Preguntas respondidas:** ✓
  - Pregunta 4: Etiquetas y cantidad de datos
  - Pregunta 5: Predicción de 4 puntos de test
  - Pregunta 6: Clasificación detallada
- **Puntos de test (PDF):** ✓
  ```python
  [[-7,-6], [1.5,-6.5], [7.9,0.5], [5.5,10]]
  ```

#### ✅ Punto 3: Regresión Lineal (1 punto)
- **Tabla de entrenamiento (PDF):** ✓
  ```python
  Peso (kg):   [60.0, 65.0, 72.3, 75.0, 80.0]
  Altura (m):  [1.60, 1.65, 1.70, 1.73, 1.80]
  ```
- **Alturas de test (PDF):** ✓
  ```python
  [1.58, 1.62, 1.69, 1.76, 1.82]
  ```
- **Cálculo de RSS:** ✓
- **Visualización:** ✓

#### ✅ Punto 4: Distancia del Coseno (2 puntos) - **CORREGIDO**
- **Vectores según PDF:** ✓
  ```python
  A = [2, 1, 0, 2, 0, 1, 1, 1]  # 8 elementos ✓
  B = [2, 1, 1, 1, 1, 0, 1, 1]  # 8 elementos ✓
  P = [1, 2, 3, 0, 4, 6, 7, 9]  # 8 elementos ✓
  Q = [2, 4, 3, 1, 8, 2, 4, 1]  # 8 elementos ✓
  S = [2, 1, 4, 7, 1, 4, 5, 6]  # 8 elementos ✓
  T = [3, 3, 3, 6, 1, 1, 7, 8]  # 8 elementos ✓
  ```
- **Cálculos requeridos:** ✓
  - Cos(A,B)
  - Cos(P,Q)
  - Cos(S,T)
- **Ángulos:** ✓
  - En radianes
  - En grados
- **Interpretación:** ✓
  - Significado de θ = 0 rad (vectores idénticos)
  - Significado de θ = π/2 rad (vectores ortogonales)
- **Visualización:** ✓

---

### **PARTE B** (`parte_b.ipynb`)

#### ✅ Punto 5: Visualización 3D con Centroide (1 punto)
- **Archivo de datos:** ✓
  - `puntos_3d.npy`
- **DataFrame con 3 columnas:** ✓
- **Visualización 3D:** ✓
  - Puntos en rojo
  - **Centroide en AZUL** (estrella grande)
- **Cálculo del centroide:** ✓ (promedio de todos los puntos)

#### ✅ Punto 6: KMeans en Dataset Iris (2 puntos)
- **Importaciones requeridas (PDF):** ✓
  ```python
  from sklearn.datasets import load_iris
  from sklearn.cluster import KMeans
  ```
- **Dataset Iris:** ✓
  - Cargado con `load_iris()`
- **Clustering:** ✓
  - KMeans con n_clusters=3, random_state=42
- **Visualización:** ✓
  - Gráfico 2D (proyección)
  - Centroides marcados
- **Métricas de evaluación:** ✓
  - Adjusted Rand Index (ARI)
  - Silhouette Score

#### ✅ Punto 7: Filtro de Kalman (3 puntos)
- **Implementación:** ✓
  - Clase KalmanFilter
- **Generación de datos:** ✓
  - Trayectoria real: y = 2x + 10
  - Mediciones con ruido gaussiano
- **Visualización (PDF):** ✓
  - Línea verde: Trayectoria real
  - Puntos rojos: Mediciones ruidosas
  - Línea azul: Predicción Kalman Filter
- **Análisis de error:** ✓
  - MAE comparativo
  - Reducción de error porcentual

#### ✅ Punto 8: Filtro Complementario (1 punto)
- **Implementación:** ✓
  - Clase ComplementaryFilter
- **Dos sensores simulados:** ✓
  - Sensor 1: Alta frecuencia, bajo drift
  - Sensor 2: Baja frecuencia, con drift
- **Optimización de Alpha:** ✓
  - Prueba con múltiples valores (0.2, 0.5, 0.8)
  - Selección del alpha óptimo
- **Visualización:** ✓
  - 4 subplots comparativos
  - Mejor alpha resaltado

---

## 📊 PUNTUACIÓN TOTAL

| Punto | Descripción | Puntaje | Estado |
|-------|-------------|---------|--------|
| 1 | KMeans | 2 | ✅ |
| 2 | MeanShift | 2 | ✅ |
| 3 | Regresión Lineal | 1 | ✅ |
| 4 | Distancia del Coseno | 2 | ✅ |
| 5 | Visualización 3D | 1 | ✅ |
| 6 | KMeans en Iris | 2 | ✅ |
| 7 | Filtro de Kalman | 3 | ✅ |
| 8 | Filtro Complementario | 1 | ✅ |
| **TOTAL** | | **14** | **✅** |

---

## 🔧 CORRECCIONES APLICADAS

### Corrección Final (8 Nov 2025):
- **Punto 4 - Vectores del Coseno:**
  - ❌ **Error detectado:** Vectores con longitudes incorrectas
  - ✅ **Corregido:** Todos los vectores ahora tienen 8 elementos
  - Los vectores A, B, P, Q, S, T ahora coinciden exactamente con el PDF

### Correcciones Previas:
1. Autor cambiado de "Alberto Caro" a "Renato Carrasco"
2. Puntos de test KMeans corregidos según PDF
3. Datos de regresión verificados
4. Estructura reorganizada: 2 notebooks en lugar de 4

---

## ✅ VERIFICACIÓN FINAL

- [x] Todos los 8 puntos implementados correctamente
- [x] Todos los datos coinciden con el PDF
- [x] Notebooks organizados correctamente (Parte A y Parte B)
- [x] Código modular en `src/`
- [x] Visualizaciones según especificaciones
- [x] Documentación actualizada (README.md, MAPEO_RUBRICA.md)
- [x] Entorno virtual con todas las dependencias

---

## 🚀 LISTO PARA ENTREGA

**Estado:** ✅ COMPLETO  
**Fecha límite:** 19 de Noviembre, 09:00 - 16:00  
**Modalidad:** Grupo de 2 personas o individual

---

**Validado por:** GitHub Copilot  
**Fecha:** 8 de Noviembre, 2025
