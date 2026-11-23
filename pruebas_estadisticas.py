#!/usr/bin/env python3
"""Pruebas estadísticas que uso en el laboratorio, ahora en Python.

Las mismas pruebas que antes hacía en Excel (chi cuadrada, t de Student
y ANOVA de una vía), con SciPy, sobre datos de ejemplo.

Uso:
    python3 pruebas_estadisticas.py

Se interpreta cada resultado con alfa = 0.05.
"""

from scipy import stats

ALFA = 0.05


def interpretar(p):
    """Interpreta un valor p con alfa = 0.05."""
    if p < ALFA:
        return "diferencia significativa (se rechaza H0)"
    return "sin diferencia significativa (no se rechaza H0)"


def chi_cuadrada():
    """Chi cuadrada: ¿la respuesta depende del tratamiento?

    Tabla de ejemplo (frecuencias observadas):
                    Respondió   No respondió
      Tratamiento A     30           10
      Tratamiento B     20           25
    """
    tabla = [[30, 10], [20, 25]]
    chi2, p, gl, _ = stats.chi2_contingency(tabla)
    print("1) Chi cuadrada (independencia)")
    print(f"   chi2 = {chi2:.2f}, gl = {gl}, p = {p:.4f}")
    print(f"   -> {interpretar(p)}")


def t_student():
    """t de Student: ¿difieren dos grupos?

    Ejemplo: concentración medida (mg/L) con dos métodos.
    """
    metodo_a = [10.2, 10.5, 9.8, 10.4, 10.1, 10.6]
    metodo_b = [11.3, 11.0, 11.5, 10.9, 11.2, 11.4]
    t, p = stats.ttest_ind(metodo_a, metodo_b)
    print("2) t de Student (dos muestras independientes)")
    print(f"   media A = {sum(metodo_a) / len(metodo_a):.2f}, "
          f"media B = {sum(metodo_b) / len(metodo_b):.2f}")
    print(f"   t = {t:.2f}, p = {p:.4f}")
    print(f"   -> {interpretar(p)}")


def anova():
    """ANOVA de una vía: ¿difiere al menos un grupo de tres?

    Ejemplo: crecimiento celular (mm) con tres medios de cultivo.
    """
    medio_1 = [12, 13, 11, 12, 14]
    medio_2 = [15, 16, 14, 15, 16]
    medio_3 = [12, 11, 13, 12, 12]
    f, p = stats.f_oneway(medio_1, medio_2, medio_3)
    print("3) ANOVA de una vía (tres grupos)")
    print(f"   F = {f:.2f}, p = {p:.4f}")
    print(f"   -> {interpretar(p)}")


if __name__ == "__main__":
    print("Pruebas estadísticas (alfa = 0.05, datos de ejemplo)")
    print()
    chi_cuadrada()
    print()
    t_student()
    print()
    anova()
