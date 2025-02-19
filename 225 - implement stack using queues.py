#problem: https://leetcode.com/problems/implement-stack-using-queues/description/
#deque from collections library
#make a last in first out stack using basic queue functions
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        #append adds to end of stack
        #but need to get it to front of stack to complete LIFO
        #so we loop through the list popping and appending until the given int is at the front
        for i in range(len(self.q)-1):
            x = self.q.popleft()
            self.q.append(x)
        

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()