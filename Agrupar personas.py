from typing import List
from collections import defaultdict

def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    groups = defaultdict(list)
    result = []

    for i, size in enumerate(groupSizes):
        groups[size].append(i)
        if len(groups[size]) == size:
            result.append(groups[size])
            groups[size] = []

    return result

# Pruebas
print(groupThePeople([3,3,3,3,3,1,3]))  # [[5],[0,1,2],[3,4,6]]
print(groupThePeople([2,1,3,3,3,2]))  # [[1],[0,5],[2,3,4]]
