import numpy as np

def solution(arr1, arr2):
    answer = [[]]
    narr1 = np.array(arr1)
    narr2 = np.array(arr2)
    
    answer = np.dot(arr1, arr2)

    
    
    return answer.tolist()