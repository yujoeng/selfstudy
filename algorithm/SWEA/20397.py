'''
돌 던지기 게임

[문제]
동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고, 게임의 규칙은 다음과 같다.

i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

[입력]
첫 줄에 게임의 개수 T, 
다음 줄부터 게임별로 첫 줄에 돌의 수 N, 뒤집기 횟수 M, .
다음 줄에 N개 돌의 초기상태, 이후 M개의 줄에 걸쳐 i, j가 주어진다.
(1<=T<=50, 3<=N<=20,   1<=M<=10, 1<=i, j<=N)

[출력]
#과 게임번호, 빈칸에 이어 빈칸으로 구분된 돌의 상태를 출력한다.
'''

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    stones = list(map(int,input().split()))

    for _ in range(M):
        i, j = map(int, input().split()) # i는 기준 돌, j는 확인할 최대 거리 
        a = i - 1  # 인덱스 - 1
    
        # b = 1 ~ j까지, 기준 c를 중심으로 좌우 d칸 떨어진 쌍(L, R)을 본다
        for b in range(1, j +1):
            L, R = a - b, a + b  #왼쪽/ 오른쪽 인덱스 
            if L < 0 or R >= N :  # 범위를 벗어나면 더 이상 진행하지 않고 이번 연산 종료
                break
            
            if stones[L] == stones[R]:
                stones[L] = 1 - stones[L]
                stones[R] = 1 - stones[R]

    print(f'#{tc}', *stones)

        