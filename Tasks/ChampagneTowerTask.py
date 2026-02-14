def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    triangle = [[0.0] * (i + 1) for i in range(query_row + 1)]
    triangle[0][0] = poured

    for i in range(query_row):

        glass = i + 1

        for j in range(glass):
            if triangle[i][j] > 1:
                excess = max(0, triangle[i][j] - 1)
                triangle[i + 1][j] += excess / 2
                triangle[i + 1][j + 1] += excess / 2


    return min(1, triangle[query_row][query_glass])

#https://leetcode.com/problems/champagne-tower/description/?envType=daily-question&envId=2026-02-14