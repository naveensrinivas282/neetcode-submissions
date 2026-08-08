class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    num = board[i][j]

                    if num not in dic:
                        dic[num] = [(i, j)]
                    else:
                        dic[num].append((i, j))

        for num in dic:
            positions = dic[num]

            for x in range(len(positions)):
                for y in range(x + 1, len(positions)):
                    i1, j1 = positions[x]
                    i2, j2 = positions[y]

                    # Same row
                    if i1 == i2:
                        return False

                    # Same column
                    if j1 == j2:
                        return False

                    # Same 3x3 box
                    if i1 // 3 == i2 // 3 and j1 // 3 == j2 // 3:
                        return False

        return True