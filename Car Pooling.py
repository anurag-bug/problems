https://leetcode.com/problems/car-pooling/
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

  
import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        drops = []
        curr_cap = capacity
        for trip in trips:
            no_of_pass, pickup, curr_drop = trip
            while drops and drops[0][0] <= pickup:
                drop = heapq.heappop(drops)
                curr_cap += drop[1]
            curr_cap -= no_of_pass
            if curr_cap < 0:
                return False
            heapq.heappush(drops, (curr_drop, no_of_pass))
        return True
      
