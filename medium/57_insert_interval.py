class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if intervals == []:
            return [newInterval]

        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break
        else:
            intervals.append(newInterval)
            
        newIntervals = [intervals[0]]
        i = 1
        for x in range(1, len(intervals)):
            curr = intervals[x]
            prev = newIntervals[i - 1]

            if (curr[0] >= prev[0] and curr[0] <= prev[1]) or (curr[1] >= prev[0] and curr[1] <= prev[1]):
                newIntervals[i - 1][1] = max(curr[1], prev[1])
            else:
                newIntervals.append(curr)
                i += 1

        return newIntervals