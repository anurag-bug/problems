#Two Pointers
Given two sorted arrays of distinct integers, A and B, and an integer C, find and return the pair whose sum is closest to C and the pair has one element from each array.

More formally, find A[i] and B[j] such that abs((A[i] + B[j]) - C) has minimum value.

If there are multiple solutions find the one with minimum i and even if there are multiple values of j for the same i then return the one with minimum j.

Return an array with two elements {A[i], B[j]}.

The first argument given is the integer array A.
The second argument given is the integer array B.
The third argument given is integer C.

 A = [5, 10, 20]
 B = [1, 2, 30]
 C = 13
 
 [10, 2]
 
 A = [1, 2, 3, 4, 5]
 B = [2, 4, 6, 8]
 C = 9
 
 [1, 8]
 
 
 class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        # print(self.mergeTwoSortedArrays(A,B))
        # finalArray = self.mergeTwoSortedArrays(A,B)
        low = 0
        high = len(B)-1
        n = len(A)
        ans = []
        lowIndex = 9999999999999999
        highIndex = 999999999999999
        currDiff = 9999999999999999
        while low < n and high >= 0:
            if abs(A[low] + B[high] - C) < currDiff:
                lowIndex = low
                highIndex = high
                currDiff = abs(A[low] + B[high] - C)
            elif currDiff == abs(A[low] + B[high] - C):
                if low == lowIndex and high < highIndex:
                    highIndex = high
            if A[low] + B[high] > C:
                high-=1
            else:
                low+=1
        return [A[lowIndex], B[highIndex]]
