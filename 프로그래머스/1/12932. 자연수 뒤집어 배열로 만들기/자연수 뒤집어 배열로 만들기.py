def solution(n):
    answer = list(map(int, str(n)))
    temp = answer[::-1]
    return temp
    # answer.reverse()
    # return answer
    
# reverse() 쓰면 none이 리턴, answer를 반환 해야함
