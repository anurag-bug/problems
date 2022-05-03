Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
https://leetcode.com/problems/maximum-subarray/

def kadanesAlgorithm(array):
    # Write your code here.
    max_so_far = array[0]
	max_ending_here = array[0]
	for i in range(1,len(array)):
		max_ending_here = max(array[i], max_ending_here+array[i])
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far
