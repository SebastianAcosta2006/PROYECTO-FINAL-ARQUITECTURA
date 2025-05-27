Proyecto Final: Simulador de Procesador risc con pipeline

Descripción
Este proyecto implementa un simulador educativo de un procesador con arquitectura RISC segmentado en 5 etapas (IF, ID, EX, MEM, WB), incluyendo soporte para detección de *hazards*, manejo de interrupciones y simulación de una memoria caché L1 con mapeo directo. Fue desarrollado en Python con una ISA personalizada, y está orientado a demostrar conceptos de arquitectura de computadores y procesamiento en paralelo.

Estructura del Proyecto
PROYECTO_FINAL/
│
├── CPU/
│ ├── isa.py # Definición de la ISA personalizada
│ ├── pipeline.py # Lógica del pipeline y detección de hazards
│
├── memoria/
│ └── cache.py # Simulación de la caché L1
│
├── io/
│ ├── dispositivo.py # Simulación de entrada/salida
│ └── simuinterrupciones.py # Manejo de interrupciones
│
├── Test/
│ └── benchmarks.py # Benchmarks para pruebas (secuencial, aleatoria, aritmética)
│
└── main.py # Punto de entrada principal del simulador

markdown

Instrucciones de Ejecución
1. **Requisitos**:
Python 3.8 o superior
No requiere librerías externas

2. **Ejecutar el simulador**:
Desde la raíz del proyecto, corre:
```bash
   python main.py
Elegir un benchmark:
Dentro del archivo main.py, puedes seleccionar uno de los programas de prueba importando alguna función desde Test/benchmarks.py, por ejemplo:
python
from Test.benchmarks import load_program1

Comentarios del Código
El código fuente está comentado línea por línea para facilitar su comprensión, especialmente en:
pipeline.py: Cada etapa del pipeline está claramente separada y documentada.
cache.py: Describe el comportamiento de la caché en mapeo directo.
benchmarks.py: Explica los distintos tipos de patrones de acceso a memoria.

Objetivos Didácticos
Entender el flujo de instrucciones en una arquitectura tipo pipeline.
Observar cómo se gestionan los conflictos de datos (hazards).
Visualizar el impacto de una caché en el rendimiento del sistema.
Explorar cómo se manejan interrupciones y E/S en una arquitectura simple.
