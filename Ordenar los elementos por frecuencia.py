from typing import List

def sortByFrequency(nums: List[int]) -> List[int]:
    # Contar frecuencias
    freq = [0] * 101  # Asumiendo que los números están en el rango 0-100
    for num in nums:
        freq[num] += 1

    # Crear una copia de nums para conservar el orden de aparición
    nums_sorted = sorted(nums, key=lambda x: (-freq[x], nums.index(x)))

    return nums_sorted

# Pruebas
print(sortByFrequency([4,3,1,6,3,4,4,6]))  # [4,4,4,3,3,6,6,1]
