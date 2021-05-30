https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        

    def push(self, val: int) -> None:
        if self.s:
            self.s.append((val, min(val, self.s[-1][1])))
        else:
            self.s.append((val, val))

    def pop(self) -> None:
        self.s.pop(-1)

    def top(self) -> int:
        return self.s[-1][0]
        
    def getMin(self) -> int:
        return self.s[-1][1]
