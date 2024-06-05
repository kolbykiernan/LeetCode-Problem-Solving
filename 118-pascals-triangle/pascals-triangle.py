class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        triangle = [[1]]

        for current_row in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1]

            for index in range(1, current_row):
                new_row.append(prev_row[index -1] + prev_row[index])
            new_row.append(1)
            triangle.append(new_row)

        return triangle