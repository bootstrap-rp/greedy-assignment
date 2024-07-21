
def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        
        if(M>N): return -1
        prev=0
        ans=float('inf')
        for i in range(M-1,N):
            ans=min(ans,A[i]-A[prev])
            prev+=1
        return ans

N = 7
M = 3
A = {7, 3, 2, 4, 9, 12, 56}


print(findMinDiff(A,N,M))