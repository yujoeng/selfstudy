def f(v):
    if tree[v] in '+-*/': # 정점이 연산자면
        l = f(left[v])      # 왼쪽 자식의 리턴값
        r = f(right[v])     # 오른쪽
        if tree[v] == '+':
            return l + r
        elif tree[v] == '-':
            return l - r
        elif tree[v] == '*':
            return l * r
    else:
        return int(tree[v])
T = 10
for tc in range(1, T+1):
    N = int(input()) # 1≤N≤1000

    tree = [] * (N + 1)   #
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        n, *arr = input().split()
        tree[int(n)] = arr[0] # 정점의 연산자/피연산자 저장
        if arr[0] in '+-*/': # 연산자인 경우
            left[int(n)] = int(arr[1])
            right[int(n)] = int(arr[2])
    ans = f(1)

    print(f'#{tc} {int(ans)}')