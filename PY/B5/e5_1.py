"""Crea five_number_summary(nums) que devuelva (min, Q1, median, Q3, max) usando statistics.
 Usa statistics.quantiles para los cuartiles y statistics.median para la mediana."""
import statistics

def five_number_summary(nums):
    return (
        min(nums),
        statistics.quantiles(nums, n=4)[0],
        statistics.median(nums),
        statistics.quantiles(nums, n=4)[2],
        max(nums)
    )



try:
    list = input("Ingrese una lista de números separados por comas: ")
    list = [float(num.strip()) for num in list.split(",")]
    summary = five_number_summary(list)
    print(summary)  
except Exception as e:
    print(f"error {e}")
