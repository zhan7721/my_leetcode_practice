class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0

        while bottom >= top or right >= left:
            if top <= bottom:
                # print(top, right, left, bottom)
                for t in range(left, right+1):
                    output.append(matrix[top][t])
                    # print('top', matrix[top][t])
                top += 1

            if right >= left:
                # print(top, right, left, bottom)
                for r in range(top, bottom+1):
                    output.append(matrix[r][right])
                    # print('right', matrix[r][right])
                right -= 1

            if top <= bottom:
                # print(top, right, left, bottom)
                for b in range(right, left-1, -1):
                    output.append(matrix[bottom][b])
                    # print('bot', matrix[bottom][b])
                bottom -= 1
            
            if right >= left:
                # print(top, right, left, bottom)
                for l in range(bottom, top-1, -1):
                    output.append(matrix[l][left])
                    # print('left', matrix[l][left])
                left += 1

        return output