from .network_delay_time import Solution


class TestNetworkDelayTime:
    def test_case_multiple_destinations(self):
        s = Solution()
        assert s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2

    def test_case_single_destination(self):
        s = Solution()
        assert s.networkDelayTime([[1,2,1]], 2, 1) == 1

    def test_case_two_destinations_one_edge_returns_not_possible(self):
        s = Solution()
        assert s.networkDelayTime([[1,2,1]], 2, 2) == -1
