# Estadística en Python

Las pruebas estadísticas que uso en el laboratorio (chi cuadrada,
t de Student y ANOVA), primero hechas en Excel y ahora en Python con
SciPy. Proyecto de práctica para mi portafolio.

## Qué incluye

`pruebas_estadisticas.py` corre las tres pruebas sobre datos de ejemplo
e interpreta cada valor p con alfa = 0.05:

1. **Chi cuadrada** — independencia entre tratamiento y respuesta
   (tabla de frecuencias 2x2).
2. **t de Student** — comparación de dos grupos independientes
   (dos métodos de medición).
3. **ANOVA de una vía** — comparación de tres grupos
   (tres medios de cultivo).

## Cómo correrlo

```bash
python3 pruebas_estadisticas.py
```

## Ejemplo de salida

```
1) Chi cuadrada (independencia)
   chi2 = 6.95, gl = 1, p = 0.0084
   -> diferencia significativa (se rechaza H0)
```

Los datos son de ejemplo, para practicar la sintaxis y la
interpretación. Los datos reales de laboratorio van en archivos aparte.
