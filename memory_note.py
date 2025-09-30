def f(idx, total):
    global min_answer
    if total >= b:
        min_answer = min(min_answer, total)
        return
    if idx == n:
        return
    f(idx + 1, total + height[idx])
    f(idx + 1, total)

t = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    min_answer = 21e8
    f(0,0)
    print(f'#{tc} {min_answer - b}')