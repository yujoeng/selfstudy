def f(i, N, e, c) : # i 정류장 번호, , e 남은 배터리, c i-1까지 교환횟수
    global min_v
    global cnt
    cnt += 1
    if e < 0 :
        return
    if i == N: # 종점에 도착
        if min_v > c:
            min_v = c
    elif min_v <= c :   # 최소 교환횟수만큼 이미 교환한경우
        return
    else:
        f(i + 1, N, bat[i] - 1, c + 1)     # 교체
        f(i + 1, N, e - 1, c)             # 통과

T = int(input())
for tc in range(1, T+1):
    bat = list(map(int, input().split()))# 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi
    N = bat[0] # 정류장 수, 종점 번호

    min_v = N # 교환 횟수를 따져보자
    cnt = 0
    f(2, N, bat[1] -1, 0)
    print(f'#{tc} {min_v}')


