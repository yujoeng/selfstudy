#0 = 통로
#1 = 장애물(벽)
#2 = 괴물

'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0 # 공격받지 않은 공간의 수를 계산하기 위한 cnt
    ai, aj = 0, 0

    #몬스터 위치 정보 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:    # for문을 돌다가 2를 만난다면
                ai, aj = i, j       # ai, aj 에 2의 위치를 저장
                break

    # 외계인 광선빔을 맞은  0인 방을 1로 바꾸기
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        for d in range(1, N):
            # d 는 거리 / 외계인의 위치에서부터 1칸, 2칸 최대 N-1칸까지 뻗어나감  /
            # (1, N)을 쓰는 이유는 0칸은 자기 자신(외계인 위치)이므로 건너띔

            ni = ai + di*d  # 외계인(ai, aj)위치에서 di, dj 방향으로 d 칸 떨어진 곳
            nj = aj + dj*d
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] ==   0:      # 계산한 공간이 n의공간에  벗어나지 않는지 확인
                arr[ni][nj] = 2
            else:
                break

        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    cnt += 1
        print(f'#{tc} {cnt}')
'''

''''
1. 2차원 배열 받기 
2. 변수 설정 
3. 델타 세우기 
4. 외계인 위치 찾기 
5. 외계인 광선빔 위치 찾고 숫자 변경 
6. 0인 벽 개수  cnt 

'''

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    ai, aj = 0, 0
    ni, nj = 0, 0
    # 2차원 배열 형식 만들기
    for i in range(N):
        for j in range(N):
            # 외계인 좌표 찾고 위치 확인하기
           if arr[i][j] == 2:
               ai, aj = i, j
               break
       # 델타 이용해서 광선빔 확인하기
    for di, dj in [[-1,0], [1, 0], [0, -1], [0, 1]]:
        for d in range(1, N):
            ni = ai + di*d # 광선빔 거리 확인하기
            nj = aj + dj*d
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 :
                arr[ni][nj] = 2
            else:
                break
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    print(f'#{tc} {cnt}')

