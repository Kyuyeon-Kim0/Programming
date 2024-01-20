import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split())) # 원본 수열 저장
S = [0] * n     # 합배열
C = [0] * m     # 같은 나머지 인덱스 카운트
answer = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    reminder = S[i] % m
    if reminder == 0:
        answer += 1
    C[reminder] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1 ) // 2)

print(answer)