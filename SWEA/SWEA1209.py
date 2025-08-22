T = 10  # 10개 고정

for tc in range(1, T + 1):  # 테스트케이스 10번 반복
    input()  # 첫번째 줄은 그냥 버리기
    # 100 x 100 배열 입력받기
    arr = [list(map(int, input().split())) for _ in range(100)]

    # arr = [] # 빈 리스트 만들기
    # for _ in range(100): # 100개의 줄 입력받기
    #     arr.append(list(map(int, input().split())))

    # 합을 구하면서, 동시에 최대값 구하기
    max_val = -float('inf')  # Python 정수 범위에서 가장 최소값(무한대 최소)

    # for row in arr:
    #     row_sum = sum(arr[row])

    # python에서는 sum이 내장함수임

    # 1. 행의 합 구하기
    for r in range(100):  # 행 우선순회
        # r이 고정된 상태에서
        sum = 0  # 내장함수 sum을 0으로 덮어씀 : 함수 객체 -> 숫자 0 객체
        for c in range(100):  # 열을 0부터 99까지 반복
            # (r, 0) ~ (r, 99)
            sum += arr[r][c]

        # sum <- r 행의 합이 들어감

        if sum > max_val:  # r행의 합과 max_val 비교
            max_val = sum  # 업데이트

    # 2. 열의 합 구하기
    for c in range(100):  # 열 좌표 반복
        sum = 0
        for r in range(100):  # 행 좌표를 반복
            # arr[행좌표][열좌표]
            sum += arr[r][c]

        # sum <= c열의 합
        if sum > max_val:
            max_val = sum

    # 우하향 대각선
    sum = 0
    for i in range(100):
        sum += arr[i][i]

    if sum > max_val:
        max_val = sum

    # 우상향 대각선
    # (r,c) r+c = 99
    # c = 99 - r
    sum = 0
    for r in range(100):
        sum += arr[r][99 - r]

    if sum > max_val:
        max_val = sum

    print(f"#{tc} {max_val}")


