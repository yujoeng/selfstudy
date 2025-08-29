# 4864 문자열 비교 

T = int(input())
for tc in range(1, T+1):
    pat = input()
    txt = input()

    N = len(txt)
    M = len(pat)

    ans = 0 
    # for i in range(N-M+1): # 패턴 검색 기준 인덱스 
    #     for j in range(M): # 패턴 내부 인덱스 
    #         if txt[i+j] != pat[j]: # 비교 글자가 다른 경우 
    #             break # break 대상 = for j, 이유=검색 실패. 검색 기준 이동
    #     else:
    #         ans = 1
    #         break   #for i 더 이상 비교할 필요가 없음 


    for i in range(N-M+1):
        if pat == txt[i:i+M]:
            ans = 1

    print(f'#{tc} {ans}')




