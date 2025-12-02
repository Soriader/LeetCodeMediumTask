alphabet = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26
}


def numDecodings(self, s):
    if not s or s[0] == '0':
        return 0

    n = len(s)

    prev2 = 1
    prev1 = 1

    for i in range(2, n + 1):
        current = 0

        if s[i - 1] != '0':
            current += prev1

        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            current += prev2

        prev2, prev1 = prev1, current

    return prev1

#https://leetcode.com/problems/decode-ways/description/