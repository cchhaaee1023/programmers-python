def solution(elements):
    n = len(elements)
    plus = set()

    for i in range(n):      # 더하는 위치
        total = 0
        for length in range(1, n + 1):      # 더하기 개수
            total += elements[(i + length - 1) % n]         # i + length - 1) % n
            plus.add(total)

    return len(plus)