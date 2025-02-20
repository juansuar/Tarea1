from typing import List
from collections import defaultdict

def convertTo2DArray(nums: List[int]) -> List[List[int]]:
    seen = defaultdict(int)
    result = []
    
    for num in nums:
        row = seen[num]
        if row == len(result):
            result.append([])
        result[row].append(num)
        seen[num] += 1
    
    return result

# Pruebas
print(convertTo2DArray([1,3,4,1,2,3,1]))  # [[1,3,4,2],[1,3],[1]]
print(convertTo2DArray([1,2,3,4]))  # [[4,3,2,1]]
