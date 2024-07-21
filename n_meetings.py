def maximumMeetings(self,n,start,end):
   
        paired = list(zip(start, end))
        sorted_pairs = sorted(paired, key=lambda x: x[1])
        last_end = 0
        max_meetings = 0

        for s, e in sorted_pairs:
            if s > last_end:
                max_meetings += 1
                last_end = e

        return max_meetings

n = 6
start = [1,3,0,5,8,5]
end=  [2,4,6,7,9,9]
print(maximumMeetings(n,start,end))