from collections import deque

T=int(input())

for tc in range(1,T+1):
    N, M =map(int, input().split())
    arr = deque(list(map(int, input().split())))  #덱 자체에 리스트입력

    for i in range(M):  # 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 하기 위한 for문
        a = arr.popleft()
        arr.append(a)

    print(f'#{tc} {arr[0]}')