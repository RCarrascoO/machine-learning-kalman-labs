# Laboratorio #3 - INF0157
## Clustering, Regresión Lineal, Visualización 3D y Filtros

**Autor:** Renato Carrasco  
**Curso:** INF0157 - Sistemas  
**Fecha de entrega:** 19 de Noviembre, 09:00 - 16:00

---

## 📋 Descripción del Proyecto

Este proyecto implementa todos los puntos de la rúbrica del Laboratorio #3:

### 🎯 Contenido del Laboratorio

1. **KMeans (2 puntos)** - Clustering con KMeans y visualización
2. **MeanShift (2 puntos)** - Clustering con MeanShift y visualización
3. **Regresión Lineal (1 punto)** - Predicción de pesos y cálculo de RSS
4. **Distancia del Coseno (2 puntos)** - Similitud entre vectores con ángulos
5. **Visualización 3D (1 punto)** - Centroide 3D en puntos_3d.npy
6. **KMeans en Iris (2 puntos)** - Clustering del dataset Iris
7. **Filtro de Kalman (3 puntos)** - Filtrado de trayectorias
8. **Filtro Complementario (1 punto)** - Fusión de sensores

**Total: 14 puntos brutos**

---

## 🏗️ Estructura del Proyecto

```
Caro-Proyecto3-Sistemas/
├── src/                              # Código fuente modular
│   ├── data_loader.py               # Carga de datos .npy
│   ├── clustering/                  # Modelos de clustering
│   │   ├── kmeans_model.py
│   │   └── meanshift_model.py
│   ├── regression/
│   │   └── linear_regression.py
│   ├── similarity/
│   │   └── cosine_distance.py
│   ├── filters/
│   │   ├── kalman_filter.py
│   │   └── complementary_filter.py
│   └── utils/
│       └── visualization.py
├── notebooks/                        # Notebooks del laboratorio
│   ├── parte_a.ipynb                # Parte A: Puntos 1, 2, 3, 4 (7 pts)
│   └── parte_b.ipynb                # Parte B: Puntos 5, 6, 7, 8 (7 pts)
├── KMeans/                           # Datos para KMeans
│   ├── A.npy
│   └── _.npy
├── MeanShift/                        # Datos para MeanShift
│   ├── X.npy
│   └── _ .npy
├── puntos_3d.npy                     # Datos para visualización 3D
├── config.py                         # Configuración centralizada
├── requirements.txt                  # Dependencias
└── README.md
```

---

## 🚀 Instalación y Configuración

### 1. Crear ambiente virtual

```bash
python -m venv .venv
```

### 2. Activar ambiente virtual

**En Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**En Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 📦 Dependencias

- **numpy>=1.21.0** - Computación numérica
- **scikit-learn>=1.0.0** - Machine learning
- **matplotlib>=3.4.0** - Visualización
- **pandas>=1.3.0** - Manejo de datos
- **scipy>=1.7.0** - Computación científica
- **jupyter>=1.0.0** - Notebooks interactivos
- **seaborn>=0.11.0** - Visualización estadística

---

## 📖 Ejecución del Laboratorio

### Ejecutar Jupyter Notebooks

```bash
# Activar ambiente virtual
.venv\Scripts\Activate.ps1

# Iniciar Jupyter
jupyter notebook notebooks/
```

### Notebooks del Laboratorio

El laboratorio está dividido en 2 notebooks principales:

1. **`parte_a.ipynb`** → Parte A: Puntos 1, 2, 3, 4 (7 puntos)
   - Punto 1: KMeans Clustering (2 pts)
   - Punto 2: MeanShift Clustering (2 pts)
   - Punto 3: Regresión Lineal con RSS (1 pt)
   - Punto 4: Distancia del Coseno con ángulos (2 pts)

2. **`parte_b.ipynb`** → Parte B: Puntos 5, 6, 7, 8 (7 puntos)
   - Punto 5: Visualización 3D con centroide (1 pt)
   - Punto 6: KMeans en dataset Iris (2 pts)
   - Punto 7: Filtro de Kalman (3 pts)
   - Punto 8: Filtro Complementario (1 pt)

### Regresión Lineal

```python
from src.regression.linear_regression import LinearRegressionModel

# Crear y entrenar modelo
model = LinearRegressionModel()
model.fit(X_train, y_train)

# Predicciones
predictions = model.predict(X_test)

# Evaluación
metrics = model.evaluate(X_test, y_test)
print(f"R² = {metrics['r2']:.4f}")
print(f"RMSE = {metrics['rmse']:.4f}")
```

### Distancia del Coseno

```python
from src.similarity.cosine_distance import CosineSimilarity

# Similitud entre dos vectores
sim = CosineSimilarity.cosine_distance(v1, v2)
angle = CosineSimilarity.angle_from_cosine_degrees(sim)

print(f"Similitud: {sim:.4f}")
print(f"Ángulo: {angle:.2f}°")
```

### Filtro de Kalman

```python
from src.filters.kalman_filter import KalmanFilter

# Crear filtro
kf = KalmanFilter(dt=0.1, process_variance=1e-5, measurement_variance=1e-2)

# Aplicar a mediciones
estimates = kf.filter(measurements)
```

### Filtro Complementario

```python
from src.filters.complementary_filter import ComplementaryFilter

# Crear filtro
cf = ComplementaryFilter(alpha=0.95)

# Aplicar a series
estimates = cf.filter_series(measurements_noisy, measurements_integrated)
```

### Visualización

```python
from src.utils.visualization import Visualizer

# Graficar clusters 2D
Visualizer.plot_2d_clusters(data, labels, centroids)

# Graficar puntos 3D
Visualizer.plot_3d_points(data, labels, centroids)

# Graficar regresión
Visualizer.plot_regression(X_train, y_train, X_test, y_test, predictions, equation)
```

---

## 📓 Notebooks

Ejecutar los notebooks con:

```bash
jupyter notebook notebooks/
```

### Parte A: KMeans
- Cargar datos de entrenamiento
- Generar gráficos de blobes
- Entrenar KMeans
- Visualizar clusters y centroides
- Realizar predicciones en puntos de test

### Parte B: MeanShift
- Cargar datos de entrenamiento
- Generar gráficos de blobes
- Entrenar MeanShift
- Visualizar clusters y centroides
- Realizar predicciones en puntos de test

### Parte C: Adicionales
- Regresión lineal (altura vs peso)
- Distancia del coseno
- Visualización 3D
- Filtro de Kalman
- Filtro complementario

---

## 🧪 Tests

Ejecutar tests con:

```bash
pytest tests/
```

---

## 📊 Resultados Esperados

### KMeans (Parte A)
- 3 clusters identificados
- Centroides claramente separados
- Predicciones en puntos de test

### MeanShift (Parte B)
- Clusters detectados automáticamente
- Centroides sin necesidad de especificar número
- Predicciones en puntos de test

### Regresión Lineal (Parte C)
- Ecuación: `Peso = m × Altura + b`
- Métrica RSS (Residual Sum of Squares)
- Predicciones en set de test

### Distancia del Coseno
- Cálculo de similitud entre vectores
- Interpretación de ángulos
- Matriz de similitud

### Filtros
- Filtro de Kalman: suavizado de trayectoria
- Filtro complementario: fusión de sensores

---

## 🔍 Arquitectura Limpia

El proyecto sigue principios de arquitectura limpia:

1. **Separación de responsabilidades:** Cada módulo tiene una función específica
2. **Independencia de frameworks:** Lógica desacoplada de sklearn
3. **Testabilidad:** Funciones puras y fáciles de testear
4. **Mantenibilidad:** Código legible y bien documentado
5. **Configuración centralizada:** Parámetros en `config.py`

---

## 📝 Notas Importantes

- Los archivos `.npy` deben estar en la raíz del proyecto
- Las configuraciones se centralizan en `config.py`
- Cada módulo es independiente y reutilizable
- Los notebooks sirven como ejemplos de uso
- El código incluye docstrings completos

---

## 👤 Autor

**Renato Carrasco** - INF0157 Sistemas

---

## 📅 Fechas

- **Entrega:** 19 de Noviembre, 09:00 - 16:00
- **Modalidad:** Individual o grupo de 2 personas
