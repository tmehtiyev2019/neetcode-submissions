class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if len(prerequisites) == 0:
            return True

        preq_dict = defaultdict(list)
        course_dict = defaultdict(list)
        q = deque()
        course_taken = 0

        for course, preq in prerequisites:
            
            preq_dict[course].append(preq)
            if preq not in preq_dict.keys():
                preq_dict[preq] = []

            course_dict[preq].append(course)
            if course not in course_dict.keys():
                course_dict[course] = []

        for course in preq_dict.keys():
            if len(preq_dict[course]) == 0:
                q.append(course)

        while q:
            course = q.popleft()
            course_taken += 1
            for preq in course_dict[course]:
                preq_dict[preq].remove(course)
                if len(preq_dict[preq]) == 0:
                    q.append(preq)


        return course_taken == len(course_dict)


# preq_dict

# {
# "1":[4],
# "2":[4],
# "3":[1,2],
# "4":[]
# }

# course_dict

# {
# "1":[3],
# "2":[3],
# "3":[],
# "4":[1,2]
# }






# preq_dict

# {
# "a":[b,d],
# "b":[c],
# "c":[],
# "d":[c]
# }

# course_dict

# {
# "a":[],
# "b":[a],
# "c":[d, b],
# "d":[a]
# }






# Goal: Is it possible to finsih all courses: If yes Ture, otherwise False

# Given: For a given course we have preq. 

# preq = [[a,b]] -- > course b is a preq of a --> order: b-->a
# Total: numCourse required to take in range(numCourse)

# Restrictions:
# 1. is ther a specific ordering of the preq array?
# 2. What if we dont ahev any preq. how is it given?


# Example:

# 1.
# preq = [[a,b], [b, c], [d,c], [a, d]]

# solution order: c --> d --> a -- > b
# True


# 2.
# preq = [[a,b], [b, c], [d,c], [a, d], [c, a]]
# cycle detection: if we reapeat the same element in preq --> Cycle detected
# False



# Steps:

# 1. Where to start?


# hashmap 1

# preq_dict

# {
# "a":[b,d],
# "b":[c],
# "c":[],
# "d":[c]
# }

# course_dict

# {
# "a":[],
# "b":[a],
# "c":[d, b],
# "d":[a]
# }


# hashmap 1

# {
# "a":[b,d],
# "b":[c],
# "c":[a],
# "d":[c]
# }

# 1. Answer: the course with no preq meaning len(preq_dict[course]) == 0

# Note: Basically if none of the preqs of the course is empty at any point it mean it is false and there is a cycle.

# 2. How to find len(preq_dict[course]) == 0 efficiently?

# maybe recursion or que?


# Warning: there might be a cycle, meaning False


# Code:

# preq_dict = defaultdict(list)
# course_dict = defaultdict(list)
# q = deque()

# for course, preq in prerequisites:
#     preq_dict[course].append(preq)
#     course_dict[preq].append(course)

# for course in preq_dict.keys():
#     if len(preq_dict[course]) == 0:
#         q.append(course)

# while q:
#     course = q.popleft()
#     for preq in course_dict[course]:
#         preq_dict[preq].remove(course)
#         if len(preq_dict[preq]) == 0:
#             q.append(preq)

# for course in preq_dict.keys():
#     if len(preq_dict[course]) != 0:
#         return False
# return True






        