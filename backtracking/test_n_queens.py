from .n_queens import Solution


class TestNQueens:
    def test_one_queen(self):
        s = Solution()
        assert s.solveNQueens(1) == [["Q"]]

    def test_four_queens(self):
        s = Solution()
        assert s.solveNQueens(4) == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
