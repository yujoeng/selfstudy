# SWEA 5249번 최소 신장 트리
'''
[문제]
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다.

1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''


def union(a, b):
    p[find_set(b)] = find_set(a)

def find_set(a):
    while a != p[a]: # 대표원소가 아니면
        a = p[a]
    return  a

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V, E : 0번부터 V번까지의 노드와 E개의 간선
    edge = [list(map(int, input().split())) for _ in range(E)]

    # Kruskal
    edge.sort(key = lambda x:x[2]) # 가중치 기준 오름차순 정렬

    # 사이클 제거를 위한 서로 소 집합 생성
    p = [i for i in range(V+1)]

    cnt = 0
    ans = 0
    for u, v, w in edge:
        if find_set(u) != find_set(v): # 서로 다르면 사이클이 없는 경우
            cnt += 1
            ans += w
            union(u, v)
            if cnt == V: # MST는 V+1개의 정점, V개의 간선
                break

    print(f'#{tc} {ans}')
