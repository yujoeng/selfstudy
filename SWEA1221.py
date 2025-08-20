# 1221. GNS

T = int(input())

for _ in range(1, T+1):
    tc, num = input().split()
    num = int(num)
    str = input().split()
    dic = {'ZRO': 0,
           'ONE': 1,
           'TWO': 2,
           'THR': 3,
           'FOR': 4,
           'FIV': 5,
           'SIX': 6,
           'SVN': 7,
           'EGT': 8,
           'NIN': 9}
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_list = []
    for item in str:
        num_list.append(dic[item])
    num_list.sort()
    for i in range(num):
        num_list[i] = numbers[num_list[i]]
    # for i in dic:
    #    if dic[i] == num_list[]
    print(tc)
    # print(' '.join(num_list))
    print(*num_list)