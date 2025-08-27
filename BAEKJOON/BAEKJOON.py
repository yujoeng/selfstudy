# n, m = map(int, input().split())
# |n-m| 을 구하라는 문제의 문구는 절대값을 입히라는 뜻이었다.
# 절대값을 입히는 함수는 abs()임
# print(abs(n-m))


n = int(input())s

for i in range(1,n+1):
    #range 문법 : start를 1로 준다. 이때 1은 인덱스가 아닌 문자열 그 자체이다.
    #인덱스를 입력할지 값을 입력할지 감이 안 잡힐 경우 for문 하단에 어떤 내용으로 채울건지 생각해보기
    # n+1인 이유 : 변동되는 입력값과 range는 stop 끝 값을 다 주지않기 때문에 n+1로 마지막 값까지 출력
    print(i)
