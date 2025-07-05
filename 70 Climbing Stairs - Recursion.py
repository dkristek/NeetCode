#recursion is too slow for this problem but I solved it this way first
#to practice recursion
#link: https://leetcode.com/problems/climbing-stairs/description/
#Asked how many ways you can climb stairs by taking either 1 or 2 steps
class Solution:
    def climbStairs(self, n: int) -> int:
        def recur(i):
            if i >= n:
                return i == n
            return recur(i+1) + recur(i+2)
        return recur(0)
