def solution(nums):
    nums.sort()  # 리스트 정렬
    sum_min = sum(nums[:3])
    sum_max = sum(nums[-3:])
    
    # setting sieve
    harf_max = int(sum_max*.5)
    sieve = [0, 0] + [1]*(sum_max-1)
    for i in range(2, harf_max+1):
        if sieve[i]:
            for j in range(i+i, sum_max+1, i):
                sieve[j] = 0
    # count 
    count_ = 0
    for num in range(sum_min, sum_max+1):
        if sieve[num]:
            count_ += 1
    answer = count_ 
    return answer