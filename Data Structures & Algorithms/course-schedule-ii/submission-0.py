from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_order = []
        preq_count = defaultdict(int)
        dependent_course = defaultdict(list)
        q = deque()

        #cna be optimized
        for i in range(numCourses):
            preq_count[i] = 0
            dependent_course[i] = []

        
        for course, preq in prerequisites:
            preq_count[course] = preq_count.get(course, 0) + 1
            dependent_course[preq].append(course)

        for course in preq_count.keys():
            if preq_count[course] == 0:
                q.append(course)
            
        while q:
            course = q.popleft()
            course_order.append(course)

            for dependent in dependent_course[course]:
                preq_count[dependent] -= 1
                if preq_count[dependent] == 0:
                    q.append(dependent)

        if len(course_order) == numCourses:
            return course_order
        else:
            return []



# Time comp:
# V (number of courses) + E (number of preq (edges))

# Space comp:
# V (number of courses) + E (number of preq (edges))

# Dry Run:

# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

# Output: []


            
# preq_count = {
#     0:0,
#     1:1,
#     2:0
# }

# dependent_course = {
#     0:[1],
#     1:[]
#     2:[]
# }
        