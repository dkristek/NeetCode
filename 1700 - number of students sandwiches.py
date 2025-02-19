#problem 1700: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
#we use a hashmap to keep track of how many students want each snadwich type
#then we go through the sandwich stack and decrement the corresponding student count for each sandwich
#when we reach a sandwich that has no remaining students (or we run out sandwiches) we return the res variable
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res
        return res