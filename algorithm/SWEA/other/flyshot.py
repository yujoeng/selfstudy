T = int(input())
for tc in range(1, T + 1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]

    max_v = 0


    for i in range(N-M+1):
        for j in range(N-M+1):
            S = 0
            for p in range(M):
                for q in range(M):





    print(f'#{tc} {max_v}')