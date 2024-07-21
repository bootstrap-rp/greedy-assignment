def solve(bt):
      
        bt.sort()
        t = 0
        wt = 0
        for i in range(len(bt)):
            wt += t
            t += bt[i]
            
        return wt // len(bt)

print(solve([1,2,3,4]))