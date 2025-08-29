"""
가로x세로 길이가 10x20, 20x20인 직사각형 종이를 잔뜩 준비

20xN 크기의 직사각형을 테이프로 표시하고 준비한 종이를 빈틈없이 붙이는 방법 찾기

N = 10의 배수  -> 종이를 붙이는 모든 경우를 찾기 위해 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지
                계산하는 프로그램 *직사각형 종이가 모자라는 경우는 x

<코드 생각해보기 >

"""

"""
T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())


    def paper(N):
        if N == 10:
            return 1
        elif N == 20:
            return 3
        else:
            return paper(N - 10) + 2 * paper(N - 20)


    ans = paper(N)
    print(f'#{test_case} {ans}')
"""

T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())

