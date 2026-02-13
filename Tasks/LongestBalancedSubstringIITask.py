def longestBalanced(self, s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    result = 1

    # ----------------------
    # Case: 1 distinct letter
    # ----------------------
    same_letter = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            same_letter += 1
        else:
            same_letter = 1
        if same_letter > result:
            result = same_letter

    # ----------------------
    # Case: 3 distinct letters (a=b=c)
    # ----------------------
    a = b = c = 0
    status = {(0, 0): -1}
    for i in range(n):
        if s[i] == 'a':
            a += 1
        elif s[i] == 'b':
            b += 1
        else:
            c += 1

        actual_status = (a - b, a - c)

        if actual_status in status:
            longest_sub = i - status[actual_status]
            if longest_sub > result:
                result = longest_sub
        else:
            status[actual_status] = i

    # ----------------------
    # Case: exactly 2 distinct letters (x=y, third=0)

    # ----------------------

    result = max(result, best_two_letters('a', 'b', 'c', s))
    result = max(result, best_two_letters('a', 'c', 'b', s))
    result = max(result, best_two_letters('b', 'c', 'a', s))

    return result

def best_two_letters(x: str, y: str, barrier: str, s: str) -> int:
    diff = 0
    best = 0
    first = {0: -1}

    for i, ch in enumerate(s):
        if ch == barrier:
            diff = 0
            first = {0: i}
            continue

        if ch == x:
            diff += 1
        elif ch == y:
            diff -= 1

        if diff in first:
            best = max(best, i - first[diff])
        else:
            first[diff] = i

    return best

#https://leetcode.com/problems/longest-balanced-substring-ii/description/?envType=daily-question&envId=2026-02-13