# ?g문제 설명
# ?g문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다.
# ?gstr에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수,
# ?gsolution을 완성하세요.
# ?g예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고,
# ?g"-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
# ?g
# ?g제한 조건
# ?gs에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

def solution(s: str) -> str:
    list_int = [int(i) for i in s.split()]
    list_int.sort()
    answer = f'{list_int[0]} {list_int[-1]}'
    return answer