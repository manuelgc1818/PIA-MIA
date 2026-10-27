'''Escribe compare_means(nums) que reciba una lista de números positivos y devuelva un dict con: media aritmética (mean), 
media armónica (harmonic_mean), 
media geométrica (geometric_mean), 
desviación poblacional (pstdev) y coeficiente de variación (cv = pstdev/mean). 
'''

import statistics
import math 

def compare_means(nums):
    mean = statistics.mean(nums)
    harmonic_mean = statistics.harmonic_mean(nums)
    geometric_mean = statistics.geometric_mean(nums)
    pstdev = statistics.pstdev(nums)
    cv = pstdev / mean if mean != 0 else 0
    return {
        "mean": mean,
        "harmonic_mean": harmonic_mean,
        "geometric_mean": geometric_mean,
        "pstdev": pstdev,
        "cv": cv
    }

try:
    list = input("Ingrese una lista de números separados por comas: ")
    list = [float(num.strip()) for num in list.split(",")]
    summary = compare_means(list)
    print(summary)
except Exception as e:
    print(f"error {e}")
