T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 문제에서 이걸 입력으로 준다고 했음
    A = [i for i in range(1, 13)]     # 1부터 12까지의 집합

    count = 0

    # 부분집합을 전부 탐색
    for i in range(1 << 12):  
        subset = []
        for j in range(12):
            if i & (1 << j):  # j번째 비트가 켜져 있다면 A[j]를 포함
                subset.append(A[j])
        
        # 부분집합이 N개의 원소를 가지는지
        if len(subset) == N:
            # 부분집합의 합이 K인지
            if sum(subset) == K:
                count += 1

    print(f"#{tc} {count}")
