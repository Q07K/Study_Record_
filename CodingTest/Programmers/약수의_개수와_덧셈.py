# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다.
# left부터 right까지의 모든 수들 중에서,
# 약수의 개수가 짝수인 수는 더하고,
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록
# solution 함수를 완성해주세요.
# 
# 제한사항
# 1 ≤ left ≤ right ≤ 1,000

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count_ = 0
        
        for j in range(1, int(i**.5)+1):
            if not i%j:
                if i**.5 == j:
                    count_ += 1
                else:
                    count_ += 2
        
        result = i
        
        if count_%2:
            result = -i
            
        answer += result
        
    return answer