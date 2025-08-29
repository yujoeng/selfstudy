def enq(n):
    global last
    last += 1 # 마지막 정점 추가 : 완전이진트리 유지
    heap[last] = n
    c = last    # 새로 추가된 자식 정점 번호
    p = c // 2 # 완전이진트리의 부모 정점 번호
    while p and heap[p] > heap[c]:# 부모가 있고, 최소힙의 조건을 만족하지 않으면
        heap[p], heap[c] = heap[c], heap[p] # 교환
        c = p # 방금 전 부모를 새로운 자식으로 
        p = c // 2 # 새로운 부모번호
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    
    heap = [0] * (N + 1) # heap 생성, 1번 ~N번 정점 준비
    last = 0
    for x in arr:
        enq(x)

    # c = last # 조상을 찾을 정점
    p = last // 2   # c // 2
    ans = 0
    while p:  # 부모가 있으면
        ans += heap[p]
        p //= 2

    print(f'#{tc} {ans}')