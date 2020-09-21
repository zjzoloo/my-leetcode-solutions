# You are driving a vehicle that has capacity empty seats initially available for passengers.  
# The vehicle only drives east (ie. it cannot turn around and drive west.)

# Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: 
# the number of passengers that must be picked up, and the locations to pick them up and drop them off.  
# The locations are given as the number of kilometers due east from your vehicle's initial location.

# Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true

# Input: trips = [[2,1,5],[3,5,7]], capacity = 3
# Output: true

# Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
# Output: true

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans = []
        for people, start_idx, end_idx in trips:
            ans.append((start_idx, people))
            ans.append((end_idx, -people))
        ans.sort()
        for _, people in ans:
            capacity -= people
            if capacity < 0:
                return False
        return True