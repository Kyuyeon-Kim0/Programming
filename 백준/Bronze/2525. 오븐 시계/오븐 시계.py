h, m = map(int, input().split())
c = int(input())

if m + c >= 60:
    n = (m + c)//60
    h = h + n
    m = (m + c) % 60
    if h >= 24 :
        h = h - 24
else:
    m = m + c

print(h, m)