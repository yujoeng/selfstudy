def f(T):
    if T > N:  # 존재하지 않는 정점인 경우
        return 0
    if tree[T] == 0:  # 리프노드가 아닌 경우
        l = f(T * 2)
        r = f(T * 2 + 1)
        tree[T] = l + r
    return tree[T]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    f(1)
    print(f'#{tc} {tree[L]}')
