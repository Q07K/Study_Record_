

from random import randrange


def sieve_of_Eratosthenes(search_max_num):
    """
    1 부터 search_max_num 사이 숫자중 소수의 개수를 찾아주는 함수
    ----------------------------------------------------
    Return : int, 소수의 개수

    search_max_num : int, 소수의 개수를 찾을 최대 범위 지정
    ----------------------------------------------------
    Sieve of Eratosthenes 에라토스테네스의 체
    고대 그리스 수학자 에라토스테네서가 만들어 낸 소수를 찾는 방법

    방법 : 임의의 자연수 n에 대해 그 이하의 소수를 찾는 가장 간단하고 빠른 방법
        1. 소수, 합성수도 아닌 유일한 자연수 1 제거
        2. 2를 제외한 2의 배수 제거
        3. 3을 제외한 3의 배수 제거
        4. 5를 제외한 5의 배수 제거
        5. 7을 제외한 7의 배수 제거
        6. ... 반복

    """

    list_ = [0, 0] + [1]*(search_max_num-1)
    for i in range(2, int(search_max_num**.5)+1):
        if list_[i]:
            for j in range(i+i, search_max_num, i):
                list_[j] = 0
    return list_.count(1)

print(sieve_of_Eratosthenes(10))
