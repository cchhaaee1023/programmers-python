def solution(k, tangerine):
    count = 0
    answer = 0
    
    uniq = list(set(tangerine))     # 중복제거
    
    count_tangerine = {}
    for i in tangerine:          # dict에 개수정리
        if i in count_tangerine:
            count_tangerine[i] += 1
        else:
            count_tangerine[i] = 1
    
    # 정렬(내림차순), 리스트로 변환
    count_tangerine = sorted(count_tangerine.items(), key=lambda x: x[1], reverse=True)
    # print(count_tangerine)
    
    i = 0
    while count < k:
        count += count_tangerine[i][1]
        i += 1
        answer += 1
        
        
    return answer