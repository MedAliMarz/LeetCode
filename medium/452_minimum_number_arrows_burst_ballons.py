class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # sorting the element by the sarting x position
        # O(nlogn)
        sorted_points = sorted(points, key=lambda limit: limit[0])
        common_ranges = []
        for point in sorted_points:
            if len(common_ranges) == 0:
                common_ranges.append(point)
            else:
                # find a range where the starting X can be inside it
                # then check if the ending X also can be inside it or expand the range
                found = False
                for crange in common_ranges:
                    if crange[1] >= point[0]:
                        if crange[0] < point[0]:
                            crange[0] = point[0]
                        if crange[1] > point[1]:
                            crange[1] = point[1]
                        found = True
                        break
                if not found:
                    common_ranges.append(point)

        return len(common_ranges)

