import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            # 절댓값이 가장 작은 값 제거, 반환 (항상 루트에 위치)
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        # 절댓값, 입력값 push
        heapq.heappush(heap,(abs(x), x))
