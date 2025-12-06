def countCollisions(self, directions: str) -> int:

    i = 0
    while i < len(directions) and directions[i] == 'L':
        i += 1
    directions = directions[i:]

    i = len(directions) - 1
    while i >= 0 and directions[i] == 'R':
        i -= 1
    directions = directions[:i + 1]

    result = 0
    for ch in directions:
        if ch != 'S':
            result += 1

    return result

#https://leetcode.com/problems/count-collisions-on-a-road/