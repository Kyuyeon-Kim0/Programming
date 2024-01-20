n = int(input())
sub = list(map(int, input().split()))
sum = 0

m = max(sub)
for i in sub :
    s = i
    sum += s / m * 100

print(sum / n)