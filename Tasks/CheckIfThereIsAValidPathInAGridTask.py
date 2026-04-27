def hasValidPath(self, grid):
    if not grid or not grid[0]:
        return False

    m, n = len(grid), len(grid[0])

    street_connections = {
        1: [False, True, False, True],
        2: [True, False, True, False],
        3: [False, False, True, True],
        4: [False, True, True, False],
        5: [True, False, False, True],
        6: [True, True, False, False]
    }

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    opposite = {0: 2, 1: 3, 2: 0, 3: 1}

    visited = [[False] * n for _ in range(m)]

    def can_move(from_x, from_y, to_x, to_y, direction):


        if not (0 <= to_x < m and 0 <= to_y < n):
            return False

        street_from = grid[from_x][from_y]
        street_to = grid[to_x][to_y]

        # Czy ulica w bieżącej komórce łączy w tym kierunku?
        if not street_connections[street_from][direction]:
            return False

        opposite_dir = opposite[direction]

        return street_connections[street_to][opposite_dir]

    from collections import deque
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        if x == m - 1 and y == n - 1:
            return True

        for dir_idx, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy

            if not visited[nx][ny] if 0 <= nx < m and 0 <= ny < n else False:
                if can_move(x, y, nx, ny, dir_idx):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return visited[m - 1][n - 1]

#https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description/?envType=daily-question&envId=2026-04-27