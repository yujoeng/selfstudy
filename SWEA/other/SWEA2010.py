arr = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 2, 0],
]

N = 5
start_r, start_c = -1, -1
for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            start_r, start_c = r, c

print(f"({start_r}, {start_c}) 에서 출발")
r, c = start_r, start_c  # 출발점 찾기

while r > 0:  # r > 0일 때까지 (r == 1 이상은 되어야 위로 갈 수 있음)
    # 위로 올라가기 전에 좌우부터 체크
    while arr[r][c - 1] == 1:  # 만약에 왼쪽에 1이 있다면 (if일 때는 1칸만 갔음, while이면 반복해서 간다.)
        c -= 1  # 왼쪽으로 간다.
        arr[r][c] = 3

    r -= 1  # 위로 올라간다.
    arr[r][c] = 3

for i in range(N):
    print(arr[i])

for tc in range(1, 11):
    input()  # 테스트 케이스 번호 무시

    arr = [[0] * 100 for _ in range(100)]
    endR, endC = -1, -1

    # 입력 받기 및 지도 초기화
    for r in range(100):
        row = list(map(int, input().split()))
        for c in range(100):
            if row[c] == 1:
                arr[r][c] = 1
            elif row[c] == 2:
                arr[r][c] = 2
                endR, endC = r, c

    r, c = endR, endC

    # 위로 올라가면서 경로 추적
    while r > 0:
        if c - 1 >= 0 and arr[r][c - 1] == 1:  # 왼쪽으로 이동
            while c - 1 >= 0 and arr[r][c - 1] == 1:
                c -= 1
        elif c + 1 < 100 and arr[r][c + 1] == 1:  # 오른쪽으로 이동
            while c + 1 < 100 and arr[r][c + 1] == 1:
                c += 1
        r -= 1  # 위로 이동

    print(f"#{tc} {c}")

# 테케의 개수가 따로 주어지지 않고
# 무조건 10개가 주어짐

for tc in range(1, 11):
    input()  # 첫번째 줄의 테케 번호 무시

    arr = [list(map(int, input().split())) for _ in range(100)]

    start_r, start_c = -1, -1
    for r in range(100):
        for c in range(100):
            if arr[r][c] == 2:
                start_r, start_c = r, c

    r, c = start_r, start_c

    # 위로 올라가면서 경로 추적
    while r > 0:
        # 위로 올라가기 전에 좌우로 갈 수 있다면 먼저 좌우로 최대한 갈수 있는 만큼 간다.
        if c - 1 >= 0 and arr[r][c - 1] == 1:  # 왼쪽으로 갈수 있다면
            while c - 1 >= 0 and arr[r][c - 1] == 1:
                c -= 1
        elif c + 1 < 100 and arr[r][c + 1] == 1:  # 오른쪽으로 갈 수 있다면
            while c + 1 < 100 and arr[r][c + 1] == 1:
                c += 1

        r -= 1  # 위로 이동

    print(f"#{tc} {c}")

