# Guía rápida de Jupyter

Este archivo explica de forma práctica cómo crear, ejecutar y exportar notebooks Jupyter en Windows (PowerShell). Está pensado para que cualquiera pueda reproducir los pasos del laboratorio.

## Contenido
- Qué es Jupyter
- Preparar el entorno (virtualenv)
- Abrir y ejecutar un notebook
- Ejecutar todas las celdas desde la terminal
- Exportar a HTML / PDF
- Buenas prácticas y una celda `Setup` recomendada

---

## ¿Qué es Jupyter?
Jupyter es una aplicación web para crear y compartir documentos que contienen código ejecutable, ecuaciones, visualizaciones y texto narrativo. Los documentos se llaman "notebooks" y tienen extensión `.ipynb`.

## Preparar el entorno (Windows PowerShell)
1. Crear un entorno virtual (recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias del proyecto (desde la raíz del repo):

```powershell
pip install -r requirements.txt
```

3. (Opcional) Instalar el kernel para que Jupyter use este entorno:

```powershell
python -m ipykernel install --user --name=proyecto3_env --display-name "Proyecto3 (.venv)"
```

## Abrir y ejecutar un notebook
1. Iniciar el servidor Jupyter en la carpeta `notebooks/`:

```powershell
jupyter notebook notebooks/
```

2. En el navegador, abrir `parte_a.ipynb` o `parte_b.ipynb`.
3. Ejecutar una celda: seleccionar la celda y presionar `Shift+Enter`.
4. Ejecutar todas las celdas: `Kernel` → `Restart & Run All` para una ejecución reproducible desde cero.

## Ejecutar/ejecutar todo desde la terminal (sin abrir interfaz)
Para ejecutar todas las celdas de un notebook y sobrescribirlo con las salidas:

```powershell
jupyter nbconvert --to notebook --execute notebooks\parte_a.ipynb --output notebooks\parte_a_executed.ipynb
```

Para generar HTML (útil para subir a Overleaf o compartir):

```powershell
jupyter nbconvert --to html notebooks\parte_a.ipynb --output results\parte_a.html
```

Para generar PDF vía LaTeX (requiere una distribución TeX instalada, p.e. MiKTeX):

```powershell
jupyter nbconvert --to pdf notebooks\parte_a.ipynb --output results\parte_a.pdf
```

Si `nbconvert --to pdf` falla por falta de LaTeX, exporta a HTML y conviértelo a PDF con su navegador.

## Celda `Setup` recomendada
Inserta al inicio de tus notebooks una celda que prepare el entorno para ejecución reproducible. Ejemplo (célula de código Python):

```python
# Setup (celda 1) - Ejecutar siempre al iniciar el notebook
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Opcional: rutas relativas del repo
ROOT = os.path.abspath(os.path.join(os.getcwd(), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Mostrar figuras dentro del notebook
%matplotlib inline

# Semilla para reproducibilidad
np.random.seed(0)

print('Entorno preparado: Python', sys.version.split()[0])
```

Nota: en PowerShell, asegúrate de activar `.venv` antes de abrir Jupyter.

## Buenas prácticas
- Siempre usar un entorno virtual por proyecto.
- Colocar las dependencias en `requirements.txt` y mantenerlo actualizado.
- Añadir una celda `Setup` al inicio del notebook (como la anterior).
- Usar `Restart & Run All` para comprobar que el notebook se ejecuta desde cero.
- Guardar resultados exportados en la carpeta `results/` para evitar sobrescribir notebooks originales.
- Cuando automatices la ejecución (`nbconvert`), guarda la salida en un archivo independiente.

## Exportar figuras y reproducibilidad
- Para incluir figuras en Overleaf, exporta notebook a HTML y extrae las imágenes desde la carpeta `results/` o usa `matplotlib` para guardar PNGs explícitos:

```python
plt.savefig('results/mi_grafico.png', dpi=200, bbox_inches='tight')
```

- Para reproducir exactamente un experimento, anota versiones de paquetes:

```powershell
pip freeze > requirements_freeze.txt
```

## Solución rápida de problemas
- Kernel no responde: reinicia el kernel (`Kernel` → `Restart`) y ejecuta `Restart & Run All`.
- Error de imports: verifica que la ruta del repo esté en `sys.path` o instala el paquete con `pip install -e .` si el repo es un paquete.
- Error al exportar a PDF: instala MiKTeX o usa `--to html` y guarda como PDF desde el navegador.

---

## Resumen rápido (comandos útiles)
```powershell
# Activar entorno
.\.venv\Scripts\Activate.ps1

# Abrir Jupyter
jupyter notebook notebooks/

# Ejecutar todas las celdas y guardar ejecución en nuevo archivo
jupyter nbconvert --to notebook --execute notebooks\parte_a.ipynb --output notebooks\parte_a_executed.ipynb

# Exportar a HTML
jupyter nbconvert --to html notebooks\parte_a.ipynb --output results\parte_a.html
```

---

Si quieres, puedo:
- Añadir esta celda `Setup` directamente al inicio de `notebooks/parte_a.ipynb` (como nueva celda),
- O ajustar el texto del archivo `JUPYTER_GUIDE.md` (más breve o más técnico).

Archivo creado: `JUPYTER_GUIDE.md` en la raíz del repositorio.
