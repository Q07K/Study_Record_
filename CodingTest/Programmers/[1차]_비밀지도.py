# 문제 설명
# 네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다.
# 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다.
# 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.
# 1. 지도는 한 변의 길이가 n인 정사각형 배열 형태로,
#    각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
# 2. 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다.
#    각각 "지도 1"과 "지도 2"라고 하자.
#    지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다.
#    지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
# 3. "지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
# 4. 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1,
#    공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.
# 네오가 프로도의 비상금을 손에 넣을 수 있도록,
# 비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.
#
# 입력 형식
# 입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.
# 1 ≦ n ≦ 16
# arr1, arr2는 길이 n인 정수 배열로 주어진다.
# 정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다.
# 즉, 0 ≦ x ≦ 2n - 1을 만족한다.
#
# 출력 형식
# 원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.

def solution(n, arr1: list, arr2: list) -> list:
    answer: list = []
    for i in zip(arr1, arr2):
        # 2진수 변환 및 자릿수 맞춰주기
        bin1 = f'{i[0]:b}'
        bin1 = '0'*(n-len(bin1))+bin1
        bin2 = f'{i[1]:b}'
        bin2 = '0'*(n-len(bin2))+bin2

        # 0이 먼저 오는 경우 정수(int)로 변환시 0이 지워짐에 따라,
        # 변환 한 2진수 앞, 뒤에 더미 수(2) 입력
        bin1 = int('2'+bin1+'2')
        bin2 = int('2'+bin2+'2')

        # [1: -1] 슬라이싱을 통해 더미 수 제거
        sum_bin = f'{bin1+bin2}'[1:-1]

        # replace를 사용하여 문자열 변경
        sum_bin = sum_bin.replace('2', '1')  # '2' -> '1'
        sum_bin = sum_bin.replace('1', '#')  # '1' -> '#'
        # '0' -> ' ' 변환 및 answer에 append
        answer.append(sum_bin.replace('0', ' '))
    return answer