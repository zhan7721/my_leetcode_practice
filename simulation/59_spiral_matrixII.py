class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0]*n for i in range(n)]
        x, y = 0, 0
        i = 1
        loop, mid = n // 2, n // 2

        for l in range(1, loop+1):
            for top in range(x, n-l):
                result[x][top] = i
                i += 1
            for right in range(y, n-l):
                result[right][n-l] = i
                i += 1
            for down in range(n-l, x, -1):
                result[n-l][down] = i
                i += 1
            for left in range(n-l, y, -1):
                result[left][y] = i
                i += 1
            x += 1
            y += 1

        if n % 2 != 0:
            result[mid][mid] = i

        return result

class Solution2:
    def generateMatrix(self, n: int) -> list[list[int]]:
        output = [[0]*n for _ in range(n)]
        top, right, bottom, left = 0, n-1, n-1, 0       # define boundaries
        num = 1

        while bottom >= top and right >= left:
            # draw the top tier from left to right
            for t in range(left, right+1):
                output[top][t] = num
                num += 1
            top += 1

            # draw the right tier from top to bottom
            for r in range(top, bottom+1):
                output[r][right] = num
                num += 1
            right -= 1

            # draw the bottom tier reversely from right to left
            for b in range(right, left-1, -1):
                output[bottom][b] = num
                num += 1
            bottom -= 1

            # draw the left tier reversely from bottom to top
            for l in range(bottom, top-1, -1):
                output[l][left] = num
                num += 1
            left += 1

        return output

