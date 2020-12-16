#Given eight integers A, B, C, D, E, F, G and H which represent two rectangles in a 2D plane.
#For the first rectangle it's bottom left corner is (A, B) and top right corner is (C, D) and for 
#the second rectangle it's bottom left corner is (E, F) and top right corner is (G, H).
#Find and return whether the two rectangles overlap or not.




class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @param G : integer
    # @param H : integer
    # @return an integer
    def solve(self, A, B, C, D, E, F, G, H):
        if B>=H or F>=D:
            return 0
        if G <= A or C<=E:
            return 0
        return 1
