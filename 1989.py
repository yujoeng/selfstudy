# 1989 초심자의 회문 검사 

T = int(input())
for tc in range(1, T+1):
    txt = input()
    N = len(txt)
    cnt = 0 
    for i in range(N//2):
        if txt[i] == txt[N-1-i]:
            cnt += 1
    
        # print(f'#{tc} 1') {cnt==N//2}




    r_txt = txt[::-1]
    if txt == r_txt:
        print(f'#{tc} 1')

    else: 
        print(f'#{tc} 0')