'''
    T = int(input())
for tc in range(1, T+1):
    N, num16 = input().split()
 
    ans = ''
    for i in range(int(N)):
        num2 = bin(int(num16[i], 16))[2:]
        if len(num2) == 4:
            ans += num2
        elif len(num2) == 3:
            ans += ('0' + num2)
        elif len(num2) == 2:
            ans += ('00' + num2)
        elif len(num2) == 1:
            ans += ('000' + num2)
 
    print(f'#{tc} {ans}')
 '''


dict_16 = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
 
T = int(input())
for tc in range(1, T+1):
    n, num = map(str, input().split())
    N = int(n)
    arr = [0]*N
    for i in range(len(num)):
        arr[i] = dict_16[num[i]]
 
    print(f'#{tc} {"".join(arr)}')
   