from collections import deque
n = int(input())
q = deque([i + 1 for i in range(n)])

while len(q) > 1:
    q.popleft()             # 맨 위 카드 버림
    q.append(q.popleft())   # 맨 위 카드를 가장 아래로

print(q[0])