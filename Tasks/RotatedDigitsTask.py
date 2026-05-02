def rotatedDigits(self, n: int) -> int:
    valid = {0, 1, 2, 5, 6, 8, 9}
    diff = {2, 5, 6, 9}

    result = 0
    for num in range(1, n + 1):
        num_str = str(num)
        if all(int(d) in valid for d in num_str) and any(int(d) in diff for d in num_str):
            result += 1

    return result

#https://leetcode.com/problems/rotated-digits/description/?envType=daily-question&envId=2026-05-02