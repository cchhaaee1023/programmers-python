def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper()
            continue
            
        elif s[i - 1] == " " and s[i] != " ":   # 공백다음이 문자.숫자 일 때
            if s[i].isdecimal() == False:
                answer += s[i].upper()
            else:
                answer += s[i]
                
        elif s[i-1] != ' ':
            answer += s[i].lower()
            
        else:
            answer += s[i]
            
    return answer