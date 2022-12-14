# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록
# solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

def solution(nums: list) -> int:
    nums.sort()  # 리스트 정렬
    sum_max = sum(nums[-3:])
    
    # setting sieve
    harf_max = int(sum_max**.5)
    sieve = [0, 0] + [1]*(sum_max-1)
    for i in range(2, harf_max+1):
        if sieve[i]:
            for j in range(i+i, sum_max+1, i):
                sieve[j] = 0
    # count 
    count_ = 0
    len_ = len(nums)
    for first_num in range(len_):
        for second_num in range(first_num+1, len_):
            for last_num in range(second_num+1, len_):
                sum_all = sum((nums[first_num],nums[second_num],nums[last_num]))
                if sieve[sum_all]:
                    count_ += 1
                    
    answer = count_
    return answer