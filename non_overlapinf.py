def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        countDeleted, currEnd = 0, intervals[0][1]
        for start, end in intervals[1:]:
            if (start >= currEnd):
                currEnd = end
            else:
                countDeleted += 1
        return countDeleted

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
