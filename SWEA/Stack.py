# #append 메소드를 통해 리스트의 마지막에 데이터를 삽입
# def my_push(item) :
#     s.append(item)
#
# #인덱스 연산을 활용한 구현
# def my_push(item, size):
#     global top
#     top += 1
#     if top==size:
#         print('overflow!')
#     else:
#         stack[top] = item
#
#
# #크기가 정해진 리스트와 인덱스 연산을 활용
# size = 10
# stack = [0] * size
# top = -1
#
# push(10, size)
# top += 1         #push(20)
# stack[top] = 20
#
# #남은 데이터 중 가장 늦게 저장된 데이터를 삭제하는 연산
# def my_pop() :
#     if len(s) == 0 :
#         #underflow
#         return
#     else :
#         return s.pop( )  #리스트 s의 마지막 원소 삭제
#


##pop  예시

stack = [1, 2, 3, 4, 5]
print('스택', stack)

#스택에서 최상단 요소 제거 및 반환
popped_element = stack.pop()
print('제거된 요소', popped_element)
print('변경된 스택', stack)

popped_element = stack.pop()
print('제거된 요소:', popped_element)
print('변경된 스택:', stack)
