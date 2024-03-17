#!/usr/bin/env python3
'''
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [a_i, b_i] indicates
that you must take course b_i first if you want to take course a_i.

For example, the pair [0, 1], indicates that to take course 0
you have to first take course 1.

Return the ordering of courses you should take to finish all
courses. If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take
course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
'''
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for course, dependency in prerequisites:
            adjacency[dependency][course] = 1
        
        doable_courses = set()
        for course in range(numCourses):
            incoming_edges = 0
            for other_course in range(numCourses):
                incoming_edges += adjacency[other_course][course]
            if incoming_edges == 0:
                doable_courses.add(course)
    
        order = []
        while doable_courses:
            next_course = doable_courses.pop()
            order.append(next_course)
            for other_course in range(numCourses):
                if next_course != other_course and adjacency[next_course][other_course] == 1:
                    adjacency[next_course][other_course] = 0
                    incoming_edges = 0
                    for other_course_neighbour in range(numCourses):
                        incoming_edges += adjacency[other_course_neighbour][other_course]
                    if incoming_edges == 0:
                        doable_courses.add(other_course)
        for row in adjacency:
            for col in row:
                if col == 1:
                    return []
        return order
