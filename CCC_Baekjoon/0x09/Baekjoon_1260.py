# https://www.acmicpc.net/problem/1260
import sys

def dfs(index):
    global visited
    visited[index] = True
    print(index, end = ' ')

    for next in range(1, N + 1):
        # 다음 Node 인 next 에 대해 방문한 적이 없고 현재 index 에서 갈 수 있다면
        if not visited[next] and graph[index][next]:
            dfs(next)

def bfs():
    global q, visited
    # Queue 에 요소가 남아 있을 때까지 수행
    while q:
        current = q.pop(0)
        print(current, end = ' ')

        for next in range(1, N + 1):
            if not visited[next] and graph[current][next]:
                visited[next] = True
                q.append(next)

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

# 1. graph 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 2. dfs
dfs(V)
print()

# 3. visited Stack 초기화
visited = [False] * (N + 1)

# 4. bfs
# 큐에 초기 방문 노드 V 삽입, 방문한 V노드 체크
q = [V]
visited[V] = True
bfs()
