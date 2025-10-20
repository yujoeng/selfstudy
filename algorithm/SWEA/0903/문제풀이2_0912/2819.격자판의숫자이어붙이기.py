'''
문제를 읽고 파악할 수 있는 내용
1. 델타 배열
2. 한번 거쳤던 격차판은 다시 거쳐도 됨 = visited 안 씀
3. 서로 다른 일곱 자리 수 - 서로 다른 수 -> set
4. 서로 다른 일곱 자리 수들의 개수 = 6번 이동


종료 조건 : 6번
가지의 수 : 4개 (상하좌우)

'''

# [재귀호출 풀이]
import sys
sys.stdin = open("input.txt")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 1. 종료조건 : 숫자 7자리일 때 종료
# 2. 가지의 수 : 4개(상하좌우)
def recur(y, x, number):
    if len(number) == 7 :   # 7자리면 종료
        result.add(number) # set 에 추가
        return

    for i in range(4):  # 상하좌우
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 밖이면 다음 방향 확인 (continue)
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        # 다음 위치로 이동
        recur(ny, nx, number + matrix[ny][nx])

T = int(input())

for tc in range(1, T + 1):
    matrix = [input().split() for _ in range(4)]  # input().split() 숫자지만 문자라고 생각하고 입력받기 위함
    result = set()

    # 7자리 만드는 코드
    # - 4 * 4가 모두 출발점이 될 수 있다.
    for sy in range(4):
        for sx in range(4):
            recur(y, x, matrix[y][x])