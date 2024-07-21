def candyStore(self, candies,N,K):
        
        candies.sort()
        minn = 0
        maxx = 0
        buy = 0
        free = N-1
        while buy <= free:
            minn += candies[buy]
            buy += 1
            free -= K
        
        buy = N-1
        free = 0
        while buy >= free:
            maxx += candies[buy]
            buy -= 1
            free += K
        return minn,maxx

N = 4
K = 2
candies= [3, 2, 1, 4]
print(candyStore(N,K,candies))