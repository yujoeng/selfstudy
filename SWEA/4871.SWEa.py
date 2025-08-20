"""
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V개 이내의 노드, E개의 간선
            # 노드 번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
    adj_lis = [[] for _ in range(V+1)] #인접 리스트 =adj_lis /V+1개의 비어있는 행을 가진 2차원 리스트
    for _ in range(E) : # E개의 줄에 걸쳐, 출발 도착 노드
        a, b = map(int, input().split())
        adj_lis[a].append(b)
        # adj_lis[b].append(a) # 방향이 없는 경우
    S, G = map(int, input().split())

    stack = [] # 스택생성
    visited = [0] * (V+1) # visited 생성
    v = S          # 시작점 V
    visited[v] = 1              # 시작점 V 방문표시
    while True:                 # 이후 과정 반복
        for w in adj_lis[v]:    # v에 인접하고 방문 안 한 w가 있으면(1)
            if visited[w] == 0:
                stack.append(v)    # push(v)
                v = w              # w 방문
                visited[w] = 1      # w에 방문표시
                break                # for w, 새로 이동한 v에서 인접한 w를 찾으러 이동
        else:        # (1)에서 없으면
            if stack:     # 스택에 지나온 정점이 남아있으면 pop()해서 v로 만들고 다시 탐색
                v = stack.pop
            else:
                break   # while True, 스택이 비어있으면 중지
    # S에서 출발해서 G에 방문한 적이 있으면 visited[G]가 True


    print(f'#{tc} {visited[G]}')
"""
# 4871. 그래프 경로

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V개 이내의 노드 번호, E개의 간선
    # 노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
    adj_list = [[] for _ in range(V + 1)]  # V+1개의 비어있는 행을 가진 2차원 리스트
    for _ in range(E):  # E개의 줄에 걸쳐 출발 도착 노드
        a, b = map(int, input().split())
        adj_list[a].append(b)
        # adj_list[b].append(a)   # 방항이 없는 경우

    S, G = map(int, input().split())

    stack = []  # 스택 생성
    visited = [0] * (V + 1)  # visited 생성
    v = S  # 시작점 v
    visited[V] = 1  # 시작점 V 방문 표시
    while True:  # 이후 과정 반복
        for w in adj_list[v]:  # V에 인접하고 방문 안 한 W가 있으면 (1)
            if visited[w] == 0:
                stack.append(v)  # push(v)
                v = w  # W 방문
                visited[w] = 1  # w에 방문 표시
                break  # for w, 새로 이동한 V에서 인접한 w를 찾으러 이동
        else:  # (1)에서 없으면
            if stack:  # 스택에 지나온 정점이 남아있느면 pop()해서 V로 만들고 다시 탐색
                v = stack.pop()
            else:
                break  # while True, 스택이 비어있으면 중지
    # S에서 출발해서 G에 방문한 적이 있으면 visited[G]가 True
    print(f'#{tc} {visited[G]}')



"""

"""