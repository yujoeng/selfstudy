'''
인치(inch)를 센티미터(cm)으로 변환하는 프로그램을 작성하십시오.
이 때 1 인치는 2.54 센티미터입니다.
'''

n = float(input())
ans = n * 2.54
print(f'{n:.2f} inch => {ans} cm')

'''
코드분석 
n = float(input()) 
-> 실수로 입력받는 float 
ans = n * 2.54 
-> 입력값 * inch 값 곱하기 
print(f'{n:.2f} inch => {ans} cm')
f'' 으로 문자열 입력 / {n:.2f} n.00으로 출력하는 법/ 
'''