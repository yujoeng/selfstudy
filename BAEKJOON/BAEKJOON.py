
# n1 = int(input())
# n2 = input()

# print(n1 * (n2 %10))
# print(n1 * (n2 // 10)%10)
# print(n1 * (n2 // 100))

# print(n1 * n2)


#for 반복문을 사용하여 b의 자릿수를 뒤에서부터 하나씩 가져와서 a와 곱합니다. 
a = int(input())
b = input()

for i in range(3, 0, -1):
    print(a * int(b[i-1]))

print(a * int(b))