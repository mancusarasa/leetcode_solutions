from .course_schedule_ii import Solution


class TestCourseSchedule:
    def test_case_one(self):
        s = Solution()
        assert s.findOrder(2, [[1, 0]]) == [0,1]

    def test_case_two(self):
        s = Solution()
        assert s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3]

    def test_case_three(self):
        s = Solution()
        assert s.findOrder(1, []) == [0]
