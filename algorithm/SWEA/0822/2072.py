#2072 홀수만 더하기
'''
0개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.
'''
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    my_sum = 0
    for x in arr:
        if x % 2 == 1:
            my_sum += x

    print(f'#{tc} {my_sum}')


'''
코드정리 
T = int(input())
for tc in range(1, T+1):

    arr = list(map(int, input().split())) 
    
    my_sum = 0 
        -> 합계를 담기 위한 변수 
    for x in arr:
        -> for문 2가지 입력 및 출력 하는 방법 
            1. for i in 리스트명 
                print(i)
            
            2. for i in range(정수 값)
                print(변수명(i))
        if x % 2 == 1:
            -> 짝수,홀수 구분 방법
                x 를 2로 나눠서 나머지 값이 1인 경우 홀수 = x%2 ==1
                x 를 2로 나눠서 나머지 값이 0인 경우 짝수 = x%2 ==0 
            my_sum += x
                -> 홀수만 추려진 x값을 합계입력 함수에 담기
    print(f'#{tc} {my_sum}')

'''