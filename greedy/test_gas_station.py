from .gas_station import Solution


class TestGasStation:
    def test_case_solution_is_possible(self):
        s = Solution()
        assert s.canCompleteCircuit(
            gas=[1,2,3,4],
            cost=[2,2,4,1]
        ) == 3

    def test_case_solution_is_not_possible(self):
        s = Solution()
        assert s.canCompleteCircuit(
            gas=[1,2,3],
            cost=[2,3,2]
        ) == -1
