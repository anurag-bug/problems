#User function Template for python3
class Solution:
    def nextPermutation(self, N, arr):
        if N == 0:
            return []
        # code here
        i = N-1
        prev = None
        index = None
        // find first element that is smaller i.e. breaks the ascending order
        while i>=0:
            if prev != None and prev > arr[i]:
                index = i
                break
            prev = arr[i]
            i-=1
        if index == None:
            return sorted(arr)
        else:
          // find first greater element than the element found above and swap them 
            for i in range(N-1, -1, -1):
                if arr[i] > arr[index]:
                    arr[i],arr[index] = arr[index], arr[i]
                    break
            newArr = sorted(arr[index+1::])
            # print(newArr)
            arr = arr[0:index+1] + newArr
        return arr
