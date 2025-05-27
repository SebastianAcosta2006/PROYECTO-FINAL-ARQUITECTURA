# 🧠 PROYECTO FINAL – SIMULADOR DE ARQUITECTURA DE COMPUTADORES

Este proyecto es un simulador educativo de arquitectura de computadores implementado en Python. Modela componentes clave como la CPU (con pipeline), la memoria caché, dispositivos de entrada/salida y maneja interrupciones.

## 📁 ESTRUCTURA DEL PROYECTO

```
PROYECTO FINAL CODES ARQUITECTURA/
│
├── main.py                          # Punto de entrada principal del simulador
│
├── CPU/
│   ├── isa.py                       # Definición de la ISA (conjunto de instrucciones)
│   ├── pipeline.py                  # Lógica del pipeline de instrucciones
│   └── __init__.py.txt              # Archivo de inicialización (renombrar si necesario)
│
├── io/
│   ├── dispositivo.py               # Simulación de dispositivos de entrada/salida
│   └── simuinterrupciones.py        # Gestión de interrupciones simuladas
│
├── memoria/
│   └── cache.py                     # Simulación de caché
│
└── Test/
    └── benchmarks.py               # Pruebas de rendimiento del simulador
```

## 🛠️ REQUISITOS

- Python 3.10 o superior (idealmente el mismo usado durante el desarrollo, ya que hay `.pyc` de CPython 3.13)
- No se requieren librerías externas (basado en el contenido observado)

## ▶️ INSTRUCCIONES DE EJECUCIÓN

1. **Renombrar `__init__.py.txt`**  
   Asegúrate de que el archivo `CPU/__init__.py.txt` se renombre a `__init__.py`.

   ```bash
   mv "CPU/__init__.py.txt" "CPU/__init__.py"
   ```

2. **Ejecutar el simulador:**

   Desde el directorio raíz (donde está `main.py`):

   ```bash
   python main.py
   ```

3. **(Opcional) Ejecutar pruebas de rendimiento:**

   ```bash
   python Test/benchmarks.py
   ```

## 💬 COMENTARIOS

- La lógica del pipeline y el comportamiento de la caché están modularizados para facilitar su modificación y pruebas.
- Los `.pyc` pueden ser eliminados si se quiere limpiar el proyecto.
- El proyecto está preparado para ampliaciones, como agregar nuevas instrucciones o dispositivos.
