#A peak is defined as adjacent integers in the array that are strictly increasing 
#until they reach a tip at which they become strictly decreasing.
def longestPeak(array):
    # Write your code here.
    longestPeak = 0
	N = len(array)
	i = 1
	while i < N-1:
		isPeak = array[i-1] < array[i] and array[i] > array[i+1]
		if not isPeak:
			i+=1
			continue
		left = i-2
		right = i+2
		while left >=0:
			if array[left] < array[left+1]:
				left-=1
			else:
				break
		while right<N:
			if array[right] < array[right-1]:
				right+=1
			else:
				break
		currentLength = right-left-1
		longestPeak = max(currentLength, longestPeak)
		i = right
	return longestPeak
