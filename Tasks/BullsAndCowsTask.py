def getHint(self, secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    bulls = 0
    cows = 0
    secret_numbers = list(secret)

    for b in range(len(secret)):
        if secret[b] == guess[b]:
            bulls += 1
            secret_numbers.remove(secret[b])

    for c in range(len(guess)):

        if secret[c] != guess[c] and guess[c] in secret_numbers:
            cows += 1
            secret_numbers.remove(guess[c])



    return f"{bulls}A{cows}B"

#https://leetcode.com/problems/bulls-and-cows/description/