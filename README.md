# 🧪 Laboratorio #3 - Machine Learning# Laboratorio #3 - INF0157

## INF01157 - Sistemas Inteligentes## Clustering, Regresión Lineal, Visualización 3D y Filtros



**Autor:** Renato Carrasco  **Autor:** Renato Carrasco  

**Fecha de entrega:** 19 de Noviembre, 2025  **Curso:** INF0157 - Sistemas  

**Calificación esperada:** 7.0/7.0 (14/14 puntos brutos)**Fecha de entrega:** 19 de Noviembre



------



## 📋 Descripción del Proyecto## 📋 Descripción del Proyecto



Este proyecto implementa 8 puntos de Machine Learning usando Python y sklearn:Este proyecto implementa todos los puntos de la rúbrica del Laboratorio #3:



### 📊 Parte A (notebooks/parte_a.ipynb) - 7 puntos### 🎯 Contenido del Laboratorio

1. **KMeans Clustering** [2 pts]

2. **MeanShift Clustering** [2 pts]1. **KMeans (2 puntos)** - Clustering con KMeans y visualización

3. **Regresión Lineal** [1 pt]2. **MeanShift (2 puntos)** - Clustering con MeanShift y visualización

4. **Distancia del Coseno** [2 pts]3. **Regresión Lineal (1 punto)** - Predicción de pesos y cálculo de RSS

4. **Distancia del Coseno (2 puntos)** - Similitud entre vectores con ángulos

### 📊 Parte B (notebooks/parte_b.ipynb) - 7 puntos5. **Visualización 3D (1 punto)** - Centroide 3D en puntos_3d.npy

5. **Visualización 3D con Centroide** [1 pt]6. **KMeans en Iris (2 puntos)** - Clustering del dataset Iris

6. **KMeans en Dataset Iris** [2 pts]7. **Filtro de Kalman (3 puntos)** - Filtrado de trayectorias

7. **Filtro de Kalman** [3 pts]8. **Filtro Complementario (1 punto)** - Fusión de sensores

8. **Filtro Complementario** [1 pt]

**Total: 14 puntos brutos**

---

---

## 🚀 Guía de Testeo

## 🏗️ Estructura del Proyecto

### Paso 1: Verificar el Entorno

```

```powershellCaro-Proyecto3-Sistemas/

# Activar el entorno virtual├── src/                              # Código fuente modular

.venv\Scripts\Activate.ps1│   ├── data_loader.py               # Carga de datos .npy

│   ├── clustering/                  # Modelos de clustering

# Verificar que Python está disponible│   │   ├── kmeans_model.py

python --version│   │   └── meanshift_model.py

# Debe mostrar: Python 3.13.9 (o superior)│   ├── regression/

│   │   └── linear_regression.py

# Verificar paquetes instalados│   ├── similarity/

pip list│   │   └── cosine_distance.py

```│   ├── filters/

│   │   ├── kalman_filter.py

### Paso 2: Verificar Archivos de Datos│   │   └── complementary_filter.py

│   └── utils/

```powershell│       └── visualization.py

# Verificar estructura del proyecto├── notebooks/                        # Notebooks del laboratorio

ls│   ├── parte_a.ipynb                # Parte A: Puntos 1, 2, 3, 4 (7 pts)

│   └── parte_b.ipynb                # Parte B: Puntos 5, 6, 7, 8 (7 pts)

# Debe mostrar:├── KMeans/                           # Datos para KMeans

# ✓ KMeans/          (A.npy, _.npy, plot_*.png)│   ├── A.npy

# ✓ MeanShift/       (X.npy, _ .npy, plot_*.png)│   └── _.npy

# ✓ puntos_3d.npy├── MeanShift/                        # Datos para MeanShift

# ✓ notebooks/       (parte_a.ipynb, parte_b.ipynb)│   ├── X.npy

# ✓ src/             (módulos de Python)│   └── _ .npy

# ✓ PDF/             (documentos del proyecto)├── puntos_3d.npy                     # Datos para visualización 3D

```├── config.py                         # Configuración centralizada

├── requirements.txt                  # Dependencias

### Paso 3: Ejecutar Tests Automatizados (Opcional)└── README.md

```

```powershell

# Si hay carpeta tests/, ejecutar:---

pytest tests/ -v

```## 🚀 Instalación y Configuración



---### 1. Crear ambiente virtual



## 📓 Testeo de Notebooks```bash

python -m venv .venv

### 🔹 Parte A: notebooks/parte_a.ipynb```



#### Ejecutar en Jupyter:### 2. Activar ambiente virtual

```powershell

jupyter notebook notebooks/parte_a.ipynb**En Windows (PowerShell):**

``````bash

.venv\Scripts\Activate.ps1

#### Checklist de Verificación:```



**✅ PUNTO 1: KMeans (Celdas 1-17)****En Linux/Mac:**

- [ ] Importaciones correctas```bash

- [ ] Datos cargados: A.npy (900 puntos), _.npy (etiquetas 0,1,2)source .venv/bin/activate

- [ ] Figura A: Datos originales visualizados```

- [ ] Modelo entrenado con 3 clusters

- [ ] Figura B: Clusters con centroides marcados con estrella### 3. Instalar dependencias

- [ ] Figura C: Comparación antes/después

- [ ] Pregunta 4: Etiquetas [0,1,2], Total: 900 datos```bash

- [ ] Pregunta 5: Predicciones para 6 puntos testpip install -r requirements.txt

- [ ] Pregunta 6: Clasificación detallada con distancias```



**Test Points (verificar):**---

```python

[[2, 5], [3.2, 6.5], [7.2, 5], [9.3, 2], [9, -6], [11, -8]]## 📦 Dependencias

```

- **numpy>=1.21.0** - Computación numérica

---- **scikit-learn>=1.0.0** - Machine learning

- **matplotlib>=3.4.0** - Visualización

**✅ PUNTO 2: MeanShift (Celdas 18-33)**- **pandas>=1.3.0** - Manejo de datos

- [ ] Importaciones correctas- **scipy>=1.7.0** - Computación científica

- [ ] Datos cargados: X.npy (1000 puntos), _ .npy (etiquetas 0,1,2,3)- **jupyter>=1.0.0** - Notebooks interactivos

- [ ] Figura A: Datos originales visualizados- **seaborn>=0.11.0** - Visualización estadística

- [ ] Modelo entrenado (detecta automáticamente 4 clusters)

- [ ] Figura B: Clusters con centroides marcados---

- [ ] Figura C: Comparación antes/después

- [ ] Pregunta 4: Etiquetas [0,1,2,3], Total: 1000 datos## 📖 Ejecución del Laboratorio

- [ ] Pregunta 5: Predicciones para 4 puntos test

- [ ] Pregunta 6: Clasificación detallada### Ejecutar Jupyter Notebooks



**Test Points (verificar):**```bash

```python# Activar ambiente virtual

[[-7, -6], [1.5, -6.5], [7.9, 0.5], [5.5, 10]].venv\Scripts\Activate.ps1

```

# Iniciar Jupyter

---jupyter notebook notebooks/

```

**✅ PUNTO 3: Regresión Lineal (Celdas 34-45)**

- [ ] Importaciones correctas### Notebooks del Laboratorio

- [ ] Datos de entrenamiento correctos:

  - Peso: `[60, 65, 72.3, 75, 80]`El laboratorio está dividido en 2 notebooks principales:

  - Altura: `[1.60, 1.65, 1.70, 1.73, 1.80]`

- [ ] Modelo entrenado (sklearn.linear_model)1. **`parte_a.ipynb`** → Parte A: Puntos 1, 2, 3, 4 (7 puntos)

- [ ] Ecuación de la recta mostrada   - Punto 1: KMeans Clustering (2 pts)

- [ ] Predicciones para alturas test: `[1.58, 1.62, 1.69, 1.76, 1.82]`   - Punto 2: MeanShift Clustering (2 pts)

- [ ] RSS calculado y explicado   - Punto 3: Regresión Lineal con RSS (1 pt)

- [ ] Gráfico con línea de regresión y predicciones   - Punto 4: Distancia del Coseno con ángulos (2 pts)



---2. **`parte_b.ipynb`** → Parte B: Puntos 5, 6, 7, 8 (7 puntos)

   - Punto 5: Visualización 3D con centroide (1 pt)

**✅ PUNTO 4: Distancia del Coseno (Celdas 46-55)**   - Punto 6: KMeans en dataset Iris (2 pts)

- [ ] Importaciones correctas   - Punto 7: Filtro de Kalman (3 pts)

- [ ] Vectores definidos (8 elementos cada uno):   - Punto 8: Filtro Complementario (1 pt)

  - A = `[2,1,0,2,0,1,1,1]`

  - B = `[2,1,1,1,1,0,1,1]`### Regresión Lineal

  - P = `[1,2,3,0,4,6,7,9]`

  - Q = `[2,4,3,1,8,2,4,1]````python

  - S = `[2,1,4,7,1,4,5,6]`from src.regression.linear_regression import LinearRegressionModel

  - T = `[3,3,3,6,1,1,7,8]`

- [ ] Similitud calculada para (A,B), (P,Q), (S,T)# Crear y entrenar modelo

- [ ] Ángulos calculados (radianes y grados)model = LinearRegressionModel()

- [ ] Interpretación de θ=0 rad (vectores idénticos)model.fit(X_train, y_train)

- [ ] Interpretación de θ=π/2 rad (vectores ortogonales)

- [ ] Visualización con gráficos de barras# Predicciones

predictions = model.predict(X_test)

---

# Evaluación

### 🔹 Parte B: notebooks/parte_b.ipynbmetrics = model.evaluate(X_test, y_test)

print(f"R² = {metrics['r2']:.4f}")

#### Ejecutar en Jupyter:print(f"RMSE = {metrics['rmse']:.4f}")

```powershell```

jupyter notebook notebooks/parte_b.ipynb

```### Distancia del Coseno



#### Checklist de Verificación:```python

from src.similarity.cosine_distance import CosineSimilarity

**✅ PUNTO 5: Visualización 3D (Celdas 1-9)**

- [ ] Importaciones correctas# Similitud entre dos vectores

- [ ] puntos_3d.npy cargadosim = CosineSimilarity.cosine_distance(v1, v2)

- [ ] Centroide calculado: `np.mean(puntos_3d, axis=0)`angle = CosineSimilarity.angle_from_cosine_degrees(sim)

- [ ] Gráfico 3D generado

- [ ] Puntos en color rojoprint(f"Similitud: {sim:.4f}")

- [ ] **Centroide en color AZUL** (requisito importante)print(f"Ángulo: {angle:.2f}°")

- [ ] Marcador de estrella grande para centroide```

- [ ] Ejes X, Y, Z etiquetados

### Filtro de Kalman

---

```python

**✅ PUNTO 6: KMeans en Iris (Celdas 10-19)**from src.filters.kalman_filter import KalmanFilter

- [ ] Importaciones: `sklearn.datasets.load_iris`

- [ ] Dataset Iris cargado# Crear filtro

- [ ] **2 columnas seleccionadas** (Sepal Length, Sepal Width)kf = KalmanFilter(dt=0.1, process_variance=1e-5, measurement_variance=1e-2)

- [ ] KMeans aplicado con 3 clusters

- [ ] Gráfico 1: Etiquetas reales# Aplicar a mediciones

- [ ] Gráfico 2: Clusters predichosestimates = kf.filter(measurements)

- [ ] Centroides marcados en ambos gráficos```

- [ ] Visualización clara y profesional

### Filtro Complementario

---

```python

**✅ PUNTO 7: Filtro de Kalman (Celdas 20-29)**from src.filters.complementary_filter import ComplementaryFilter

- [ ] Importaciones correctas

- [ ] Trayectoria definida exactamente como PDF:# Crear filtro

  - `dt = 0.1`cf = ComplementaryFilter(alpha=0.95)

  - `t = np.arange(0, 100, dt)`

  - `pos = 0.1*(3*t - t**2)`# Aplicar a series

- [ ] Filtro de Kalman implementadoestimates = cf.filter_series(measurements_noisy, measurements_integrated)

- [ ] Matrices A, H, Q, R, P definidas```

- [ ] Mediciones con ruido generadas

- [ ] Predicciones de Kalman calculadas### Visualización

- [ ] **Gráfico con 3 líneas:**

  - Mediciones (azul, puntos dispersos)```python

  - Real Track (verde)from src.utils.visualization import Visualizer

  - Predicción Kalman Filter (roja)

# Graficar clusters 2D

---Visualizer.plot_2d_clusters(data, labels, centroids)



**✅ PUNTO 8: Filtro Complementario (Celdas 30-39)**# Graficar puntos 3D

- [ ] Importaciones correctasVisualizer.plot_3d_points(data, labels, centroids)

- [ ] Filtro Complementario implementado

- [ ] **Múltiples valores de alpha probados** (ej: 0.3, 0.5, 0.7, 0.9)# Graficar regresión

- [ ] Mejor alpha seleccionado (basado en MSE)Visualizer.plot_regression(X_train, y_train, X_test, y_test, predictions, equation)

- [ ] Filtro aplicado sobre salida de Kalman```

- [ ] Gráfico comparativo generado

- [ ] Curva suavizada visible---

- [ ] Mejor alpha resaltado en el gráfico

## 📓 Notebooks

---

Ejecutar los notebooks con:

## ✅ Criterios de Éxito

```bash

### Para aprobar con 7.0/7.0:jupyter notebook notebooks/

```

1. **Todas las celdas se ejecutan sin errores** ✓

2. **Todos los gráficos se generan correctamente** ✓### Parte A: KMeans

3. **Datos coinciden exactamente con el PDF** ✓- Cargar datos de entrenamiento

4. **Respuestas explícitas a todas las preguntas** ✓- Generar gráficos de blobes

5. **Visualizaciones profesionales y claras** ✓- Entrenar KMeans

- Visualizar clusters y centroides

---- Realizar predicciones en puntos de test



## 🐛 Solución de Problemas### Parte B: MeanShift

- Cargar datos de entrenamiento

### Problema: ModuleNotFoundError- Generar gráficos de blobes

**Solución:**- Entrenar MeanShift

```powershell- Visualizar clusters y centroides

pip install -r requirements.txt- Realizar predicciones en puntos de test

```

### Parte C: Adicionales

### Problema: Kernel no se conecta- Regresión lineal (altura vs peso)

**Solución:**- Distancia del coseno

```powershell- Visualización 3D

python -m ipykernel install --user --name=.venv- Filtro de Kalman

```- Filtro complementario



### Problema: Gráficos no se muestran---

**Solución:**

```python## 🧪 Tests

# Agregar al inicio del notebook

%matplotlib inlineEjecutar tests con:

```

```bash

### Problema: Archivos .npy no se encuentranpytest tests/

**Solución:**```

```powershell

# Verificar estructura---

ls KMeans/      # Debe tener: A.npy, _.npy

ls MeanShift/   # Debe tener: X.npy, _ .npy## 📊 Resultados Esperados

ls              # Debe tener: puntos_3d.npy

```### KMeans (Parte A)

- 3 clusters identificados

---- Centroides claramente separados

- Predicciones en puntos de test

## 📊 Resultados Esperados

### MeanShift (Parte B)

### Métricas de Éxito:- Clusters detectados automáticamente

- Centroides sin necesidad de especificar número

| Punto | Descripción | Verificación |- Predicciones en puntos de test

|-------|-------------|--------------|

| 1 | KMeans | 3 figuras + 6 respuestas |### Regresión Lineal (Parte C)

| 2 | MeanShift | 3 figuras + 6 respuestas |- Ecuación: `Peso = m × Altura + b`

| 3 | Regresión | RSS < 0.1, R² > 0.95 |- Métrica RSS (Residual Sum of Squares)

| 4 | Coseno | 3 similitudes + interpretaciones |- Predicciones en set de test

| 5 | 3D | Centroide azul visible |

| 6 | Iris | 2 gráficos comparativos |### Distancia del Coseno

| 7 | Kalman | 3 líneas en gráfico |- Cálculo de similitud entre vectores

| 8 | Complementario | Múltiples alphas comparados |- Interpretación de ángulos

- Matriz de similitud

---

### Filtros

## 🎯 Checklist Final de Entrega- Filtro de Kalman: suavizado de trayectoria

- Filtro complementario: fusión de sensores

Antes de entregar, verificar:

---

- [ ] ✅ Ambos notebooks ejecutan completamente sin errores

- [ ] ✅ Todas las visualizaciones se generan correctamente## 🔍 Arquitectura Limpia

- [ ] ✅ Todos los datos coinciden con el PDF original

- [ ] ✅ Respuestas explícitas a todas las preguntasEl proyecto sigue principios de arquitectura limpia:

- [ ] ✅ Código limpio y bien comentado

- [ ] ✅ Carpetas KMeans/ y MeanShift/ con archivos .npy y .png1. **Separación de responsabilidades:** Cada módulo tiene una función específica

- [ ] ✅ Archivo puntos_3d.npy presente2. **Independencia de frameworks:** Lógica desacoplada de sklearn

- [ ] ✅ Carpeta PDF/ con documentación del proyecto3. **Testabilidad:** Funciones puras y fáciles de testear

- [ ] ✅ requirements.txt actualizado4. **Mantenibilidad:** Código legible y bien documentado

- [ ] ✅ README.md presente5. **Configuración centralizada:** Parámetros en `config.py`



------



## 🎓 Información del Curso## 📝 Notas Importantes



**Curso:** INF01157 - Sistemas Inteligentes  - Los archivos `.npy` deben estar en la raíz del proyecto

**Profesor:** Alberto Caro  - Las configuraciones se centralizan en `config.py`

**Fecha límite:** Miércoles 19 de Noviembre, 2025 (09:00 - 16:00)  - Cada módulo es independiente y reutilizable

**Modalidad:** Trabajo en grupo de 2 personas o individual  - Los notebooks sirven como ejemplos de uso

- El código incluye docstrings completos

---

---

## ✨ Estado del Proyecto

## 👤 Autor

```

╔══════════════════════════════════════════════════╗**Renato Carrasco** - INF0157 Sistemas

║                                                  ║

║         PROYECTO COMPLETO Y LISTO               ║---

║                                                  ║

║     Calificación esperada: 7.0 / 7.0            ║## 📅 Fechas

║     Puntos brutos: 14 / 14                      ║

║                                                  ║- **Entrega:** 19 de Noviembre, 09:00 - 16:00

║              ✅ 100% COMPLETO ✅                ║- **Modalidad:** Individual o grupo de 2 personas

║                                                  ║
╚══════════════════════════════════════════════════╝
```

**¡Éxito en tu presentación!** 🚀
