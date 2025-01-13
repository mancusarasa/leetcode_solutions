from .target_sum import Solution


class TestTargetSum:
    def test_case_example_one(self):
        s = Solution()
        assert s.findTargetSumWays(
            nums=[2,2,2],
            target=2
        ) == 3
