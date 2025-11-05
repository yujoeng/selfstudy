'''
민철이의 수영장 이용 계획

tip : 두 가지 접근법
1. 완전탐색
2. DP
'''

# [완전탐색 방법]

import sys
sys.stdin = open("input.txt")

# 종료조건 : 12월을 모두 고려하였을 때
# 가지의 수 : 4가지(1일, 1달, 3달, 1년)
def recur(month, total_cost):
    global min_answer

    if min_answer < total_cost : return
    if month > 12:
        # Todo : 최소값 갱신
        min_answer = min(min_answer, total_cost)
        return

    # 1일권으로 다 사는 경우
    recur(month + 1, total_cost + (days[month] * cost_day))
    # 1달권으로 다 사는 경우
    recur(month + 1, total_cost + cost_month)
    # 3달권으로 다 사는 경우
    recur(month + 3,  total_cost + cost_month3)
    # 1년 이용권으로 다 사는 경우
    recur(month + 12, total_cost + cost_year)


T = int(input())
for tc in range(1, T +1):
    # 이용권 가격들(1일, 1달, 3달, 1년)
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12월 이용 계획 (1일부터 쓴다)
    days = [0] + list(map(int, input().split()))
    min_answer = 31 * 12 * 3000 #최대 금액 (31일 * 12개월# 3000
    recur()
    print(f'#{tc} {min_answer}')


# [DP 탐색법]
