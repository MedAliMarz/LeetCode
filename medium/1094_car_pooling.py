class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stations = [0 for _ in range(1000)]


        for trip in trips:
            num, fromI, toI = trip
            for index in range(fromI, toI):
                stations[index] += num
                if stations[index] > capacity:
                    return False
        return True
