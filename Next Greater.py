Next Greater
Problem Description

Given an array A, find the next greater element G[i] for every element A[i] in the array. 
The Next greater Element for 
an element A[i] is the first greater element on the right side of A[i] in array, A.

More formally:

G[i] for an element A[i] = an element A[j] such that 
    j is minimum possible AND 
    j > i AND
    A[j] > A[i]
Elements for which no greater element exists, consider the next greater element as -1.




class Solution:
  def nextGreater(self, A):
    myStack = []
    N = len(A)
    ans = []
    for i in range(N-1,-1,-1):
      if not myStack:
        myStack.append(A[i])
        ans.append(-1)
      else:
        if A[i] >= myStack[-1]:
          while myStack and myStack[-1] <= A[i]:
            myStack.pop()
          if not myStack:
            ans.append(-1)
          else:
            ans.append(myStack[-1])
          myStack.append(A[i])
        else:
          ans.append(myStack[-1])
          myStack.append(A[i])
    return ans[::-1]
