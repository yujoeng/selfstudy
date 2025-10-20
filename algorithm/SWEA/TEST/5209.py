def f(i, N, money): # i 상품, N 전체 상품 수, s i-1 상품까지의 누적 생산비용
    global min_v
    global cnt   # 호출 횟수를 비교하기 위한 cnt
    cnt += 1
    if i == N:
        if min_v > money:
            min_v = money

    elif min_v <= money: # 모든 상품에 대한 결정이 된 것은 아니지만
        return
    else:
        for j in range(N): # i 상품을 만들 공장 후보 j
            if used[j] == 0 : # 아직 상품이 결정되지 않은 공장이면
                # p[i]= j
                used[j] = 1
                f(i + 1, N, money + cost[i][j])
                used[j] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    min_v = 1500   # 최소 생산 비용
    p = [0] * N # p[i] i번 물건을 생산하는 공장(없어도 됨)
    used = [0] * N  # used[j]  j번 공장의 결정 여부
    cnt = 0
    f(0, N, 0)
    print(f'#{tc} {min_v}')