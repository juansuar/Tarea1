from typing import List

def minOperations(boxes: str) -> List[int]:
    n = len(boxes)
    answer = [0] * n
    left_balls, left_moves = 0, 0
    right_balls, right_moves = 0, 0

   
    for i in range(n):
        if boxes[i] == '1':
            right_balls += 1
            right_moves += i

    for i in range(n):
        answer[i] = left_moves + right_moves
        
        if boxes[i] == '1':
            left_balls += 1
            right_balls -= 1

        left_moves += left_balls
        right_moves -= right_balls

    return answer


print(minOperations("110"))  
print(minOperations("001011"))  
