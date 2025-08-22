T = int(input())
for tc in range(1, T+1):
    num1 = list(map(int, input().split()))
    num_max = 0
    for i in num1:
        if num_max < i:
            num_max = i
    print(f'#{tc} {num_max}')
