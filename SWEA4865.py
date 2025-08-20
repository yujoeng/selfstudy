# 4865. 글자수

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    # 개수를 세기위한 변수 초기화
    cnt = 0
    max_v = 0

    for i in str1:  # 다음 문자 비교 위해 초기화
        for j in str2:  # str2에서 각 문자와 비교함
            if i == j:
                cnt += 1
        if cnt > max_v:
            max_v = cnt
        cnt = 0  # 다음 문자 i 비교를 위해 초기화

    print(f'#{tc} {max_v}')