def merge(intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort()
        
        output = list()
        lastStart, lastEnd = intervals[0]

        for interval in intervals[1:]:

            if interval[0]<= lastEnd:
                lastEnd = max(interval[1], lastEnd)

            else:
                output.append([lastStart, lastEnd])
                lastStart, lastEnd = interval


        output.append([lastStart, lastEnd])

        return output
intervals = [[1,4],[4,5]]
print(merge(intervals))