'''
[문제]
1보다 크거나 같고 12보다 작거나 같은 자연수 n이 주어졌을 때, 합이 n이 되는 두 자연수의 쌍을 찾는 프로그램을 작성하시오.
예를 들어, 5가 주어진 경우 가능한 쌍은 1,4와 2,3이 있다. 두 수는 항상 달라야 한다. 즉, 3,3은 올바른 쌍이 아니다.
또, 첫 번째 수가 두 번째 수보다 작아야 한다.
출력하는 쌍은 항상 사전순으로 출력해야 한다. 즉, 각 쌍의 작은 수로 비교를 해야 한다. 예를 들어 1,5는 2,4보다 사전순으로 앞선다.

[입력]
첫째 줄에 테스트 케이스의 수 (< 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다.
4
2
3
4
5

[출력]
각 테스트 케이스마다 n을 만드는 쌍을 사전순으로 출력한다. n을 만드는 쌍이 없는 경우에는 아무것도 출력하지 않는다.
Pairs for 2:
Pairs for 3: 1 2
Pairs for 4: 1 3
Pairs for 5: 1 4, 2 3
'''

def numsum(n): #합이 n이 되는 두 자연수의 쌍을 찾는 함수
    pairs = []

    for i in range(1, n//2 + 1): # 중복된 쌍을 피하기 위해서 i 는 1부터 n//2까지만 반복
        j = n - i
        if i < j:  # i, j가 둘 다 자연수인지 확인
            pairs.append((i, j))
    return pairs


T = int(input())
for _ in range(T):
    n = int(input())
    pairs = numsum(n)
    print(f'Pairs for {n}:', end=' ')

    if pairs: # 쌍이 있을 때만 출력
        # 각 쌍을 'i j ' 형태의 문자열로 변환
        pair_strings = [f"{a} {b}" for a, b in pairs]
        print(", ".join(pair_strings))
    else:
        print() #쌍이 없으면 빈 줄