from collections import deque

def bfs_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    distance = 0

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if (r, c) == end:
                return distance

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        distance += 1

    return -1  # If no path found

# Usage
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
]
start = (0, 0)
end = (3, 4)
print("Shortest path length:", bfs_maze(maze, start, end))
