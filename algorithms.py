from heapq import heappush, heappop

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path


def bfs(start, end, draw):
    from collections import deque

    queue = deque([start])
    came_from = {}
    visited = {start}

    while queue:
        current = queue.popleft()
        draw(current, "visited")

        if current == end:
            return reconstruct_path(came_from, end)

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
                draw(neighbor, "frontier")
    return []


def dfs(start, end, draw):
    stack = [start]
    came_from = {}
    visited = {start}

    while stack:
        current = stack.pop()
        draw(current, "visited")

        if current == end:
            return reconstruct_path(came_from, end)

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)
                draw(neighbor, "frontier")
    return []


def heuristic(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)


def astar(start, end, draw):
    open_set = []
    heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heappop(open_set)
        draw(current, "visited")

        if current == end:
            return reconstruct_path(came_from, end)

        for neighbor in current.neighbors:
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, end)
                heappush(open_set, (f_score, neighbor))
                draw(neighbor, "frontier")
    return []
