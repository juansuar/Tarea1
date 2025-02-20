from typing import List

def sortByFrequency(nums: List[int]) -> List[int]:
  
    freq = [0] * 101 
    for num in nums:
        freq[num] += 1

  
    nums_sorted = sorted(nums, key=lambda x: (-freq[x], nums.index(x)))

    return nums_sorted


print(sortByFrequency([4,3,1,6,3,4,4,6]))  
