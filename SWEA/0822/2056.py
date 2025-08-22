T = int(input())
date ={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for tc in range(1,T+1):
    N = str(input())
    yy = N[0:4]
    mm = N[4:6]
    dd = N[6:8]

    ans = ""
    if 0 < int(mm) < 13 and 0 < int(dd) <= date[int(mm)]:
        ans = yy + '/' + mm + '/' + dd
    else:
        ans += '-1'


'''
코드정리 
T = int(input())
    -> 테스트 케이스의 개수 T
date ={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    -> 달에 해당하는 날짜 딕셔너리로 입력 
for tc in range(1,T+1):
    -> 테스트 케이스  for문으로 돌림
    N = str(input())
        -> 입력값 
    yy = N[0:4]
    mm = N[4:6]
    dd = N[6:8]
        -> 입력값에서 문자열 슬라이싱을 활용하여 연/월/일 출력 

    ans = ""
        -> 0 이 아닌 ""을 입력하는 이유 =>
    if 0 < int(mm) < 13 and 0 < int(dd) <= date[int(mm)]:
        -> 0 < int(dd) <= date[int(mm)]   
            일(dd)이 0보다 크거나 date의 딕셔너리 값 을 초과하지 않아야함 
        ans = yy + '/' + mm + '/' + dd
    else:
        ans = '-1'
'''

