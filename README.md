# Laboratorio #3 - INF0157
## Clustering, Regresión Lineal y Filtros

**Autor:** Alberto Caro  
**Curso:** INF0157 - Sistemas  
**Fecha de entrega:** 19 de Noviembre

---

## 📋 Descripción del Proyecto

Este proyecto implementa algoritmos de clustering (KMeans y MeanShift), regresión lineal, cálculo de similitud mediante distancia del coseno, y filtros (Kalman y Complementario) utilizando **arquitectura limpia** en Python.

### 🎯 Objetivos

- **Parte A:** Aplicar KMeans de scikit-learn y analizar resultados
- **Parte B:** Aplicar MeanShift de scikit-learn y analizar resultados
- **Parte C:** 
  - Regresión lineal para predicción de peso
  - Distancia del coseno para similitud
  - Visualización 3D
  - Filtro de Kalman
  - Filtro complementario

---

## 🏗️ Estructura del Proyecto

```
Caro-Proyecto3-Sistemas/
├── src/                           # Código fuente principal
│   ├── __init__.py
│   ├── data_loader.py            # Carga de datos (.npy)
│   ├── clustering/
│   │   ├── kmeans_model.py       # Modelo KMeans
│   │   └── meanshift_model.py    # Modelo MeanShift
│   ├── regression/
│   │   └── linear_regression.py  # Regresión lineal
│   ├── similarity/
│   │   └── cosine_distance.py    # Distancia del coseno
│   ├── filters/
│   │   ├── kalman_filter.py      # Filtro de Kalman
│   │   └── complementary_filter.py # Filtro complementario
│   └── utils/
│       └── visualization.py      # Visualizaciones
├── notebooks/                     # Notebooks ejecutables
│   ├── parte_a_kmeans.ipynb
│   ├── parte_b_meanshift.ipynb
│   └── parte_c_adicionales.ipynb
├── tests/                         # Tests unitarios
├── config.py                      # Configuración centralizada
├── requirements.txt               # Dependencias
└── README.md                      # Este archivo
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

## 📖 Uso

### Cargar Datos

```python
from src.data_loader import DataLoader

# Cargar datos de KMeans
A, labels = DataLoader.load_kmeans_data()

# Cargar datos de MeanShift
X, labels = DataLoader.load_meanshift_data()

# Cargar puntos 3D
df = DataLoader.load_3d_points()
```

### KMeans

```python
from src.clustering.kmeans_model import KMeansModel

# Crear y entrenar modelo
model = KMeansModel(n_clusters=3)
model.fit(data)

# Obtener resultados
centroids = model.get_centroids()
labels = model.get_labels()
predictions = model.predict(test_data)
```

### MeanShift

```python
from src.clustering.meanshift_model import MeanShiftModel

# Crear y entrenar modelo
model = MeanShiftModel()
model.fit(data)

# Obtener resultados
centroids = model.get_centroids()
labels = model.get_labels()
```

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

**Alberto Caro** - INF0157 Sistemas

---

## 📅 Fechas

- **Entrega:** 19 de Noviembre, 09:00 - 16:00
- **Modalidad:** Individual o grupo de 2 personas
