# Sample maze:

# 0 0 0 0
# 1 1 1 0
# 0 0 0 0

# 起点：(0, 0)
# 终点：(2, 3)

# 期望输出：[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)] 或其他有效路径。

def bfs(maze, start, end):
    queue = [[start]]
    visited = set([start])

    while queue:
        path = queue.pop(0)
        x, y = path[-1]

        if (x, y) == end:
            return path
        
        for nextX, nextY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nextX < len(maze) and 0 <= nextY < len(maze[0]) and (nextX, nextY) not in visited and maze[nextX][nextY] == 0:
                #add (nextX, nextY) to visited and path + (nextX, nextY) to path
                newPath = path + [(nextX, nextY)]
                visited.add((nextX, nextY))
                queue.append(newPath)

    return None

maze = [
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
end = (2, 3)

path = bfs(maze, start, end)

print(path)