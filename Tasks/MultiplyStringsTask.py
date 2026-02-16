def multiply(self, num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            pos = i + j + 1
            product = int(num1[i]) * int(num2[j])
            total = result[pos] + product

            result[pos] = total % 10
            result[pos - 1] += total // 10

    result_str = ''.join(map(str, result))
    return result_str.lstrip('0') or '0'

#https://leetcode.com/problems/multiply-strings/description/