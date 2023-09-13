# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 최소 힙인 heapq를 사용해서 n 칸 이동해서 이동이 가능한 좌표들을 최소힙에 push 하면 순서대로 정렬할 수 있음
import heapq
def solution(maps):
    answer = 0
    maxY, maxX = len(maps), len(maps[0]) # 이동 가능한 Y, X의 Maximum

    # 주어진 maps 를 이동이 가능하면 무한대로 이동이 불가능하면 0으로 설정
    maps = [[float("inf") if maps[y][x] else 0 for x in range(maxX)] for y in range(maxY)]

    maps[0][0] = 1 # 초기값은 1칸을 이동할 수 있다.
    QUEUE = []
    heapq.heappush(QUEUE, (1, 0, 0)) # 현재 지나온칸, 시작 칸 -> 몇칸 이동, 현재 좌표

    while QUEUE:
        currentCount, currentY, currentX = heapq.heappop(QUEUE)

        # 이동할 좌표값 상우하좌
        for goY, goX in ((-1, 0), (0, 1), (1, 0), (0, -1)):

            # 상우하좌 중 이동이 가능한 좌표 탐색
            movedY, movedX = currentY + goY, currentX + goX

            # 이동이 가능한 좌표일 때 새로운 경로다
            if movedY in range(maxY) and movedX in range(maxX) and maps[movedY][movedX] != 0:
                # 새로운 경로에 이동한 칸 수 가 현재 가지고 있는 경로중 최소 이동 칸수 보다 적은 횟수인 경우에
                if currentCount + 1 < maps[movedY][movedX]:
                    # 해당 좌표에 현재까지 해당 좌표로 이동하기 위한 이동 횟수 저장
                    maps[movedY][movedX] = currentCount + 1
                    # Queue 에 기록
                    heapq.heappush(QUEUE, (maps[movedY][movedX], movedY, movedX))

    if maps[maxY-1][maxX-1] == float("inf"):
        return -1
    else:
        answer = maps[maxY-1][maxX-1]
        return answer