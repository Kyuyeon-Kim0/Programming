import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n):
    # 스택이 비어있지 않고 / A의 인덱스 스택[-1] < A의 인덱스 i
    while stack and A[stack[-1]] < A[i]:  #stack이 비어있지않고 스택[-1]
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer)