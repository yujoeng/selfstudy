T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    if N > M:
        result = '>'
    elif N < M:
        result = '<'
    else:
        result = '='


    print(f'#{tc} {result}')

