def findRepeatedDnaSequences(self, s):
    """
    :type s: str
    :rtype: List[str]
    """

    frequency = {}

    for i in range(len(s)):
        subsequence = s[i:i+10]

        if subsequence in frequency:
            frequency[subsequence] += 1
        else:
            frequency[subsequence] = 1

        if i + 10 == len(s):
            break

    result = [seq for seq, cnt in frequency.items() if cnt >= 2]

    return result



#https://leetcode.com/problems/repeated-dna-sequences/