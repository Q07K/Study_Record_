# 문제 설명
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행,
# 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

def solution(arr1: list, arr2: list) -> list:
    """
    2차원 행렬 덧셈 함수
    ----------------------
    arr1, arr2 : 최대 500열을 넘기지 않는 행렬
        return : type=list
                각 2차원 행렬의 더해진 값을 반환한다.
    """
    answer: list = []
    for dim2 in zip(arr1, arr2):
        dim1_list: list = []
        for dim1 in zip(dim2[0], dim2[1]):
            dim1_list.append(sum(dim1))
        answer.append(dim1_list)
    return answer