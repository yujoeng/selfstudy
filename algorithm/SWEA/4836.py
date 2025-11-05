#[입력]
#첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
#다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
#다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

#color = 1 (빨강), color = 2 (파랑)

#질문1 r1, r2 / r1 c1 
#질문2
T=int(input())

for tc in range(1, T+1):
    N=int(input())
    arr = list(map(int, input().split()))
               
    blank = [[0]*10 for _ in range(10)] # 10*10 전체 0으로 넣기 '


#color1 = 1 / color2 = 2 색깔값을 정의할 필요가 있나......? 
# -> 입력된 1(빨강) or 2(파랑)를 해당 인덱스 범위에 값을 넣으면 될듯

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split()) 
        for i in range(r1, c1+1): # 왼쪽 위 모서리 인덱스 
            for j in range(r2,c2+1): # 오른쪽 아래 모서리 
                [i][j] # 모서리 범위 해당 인덱스 값 1 or 2 입력하기 

        cnt = 0 # 중복범위 값 순환하기 위한 정의

        #격자판 전체 반복하면서 입력 값 파악 후 값이 3인 경우 수 뽑아내기
        for i in range(10): 
            for j in range(10): 
                if arr[i][j] == 3:
                    cnt += 1  
                    
    # 순회하는 횟수, 특정 조건에 맞는 경우의 갯수를 구하고 싶을 때 cnt +=1 를 입력해야 함
                         
            #cnt 
                #프린트
                


                





