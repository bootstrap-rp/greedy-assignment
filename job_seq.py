def JobScheduling(Jobs,n):
        st=set()
        resp=0
        Jobs.sort(key=lambda job: job.profit, reverse=True)
        for job in Jobs:
            d=job.deadline
            p=job.profit
            while d in st:
                d-=1
            if d>0:
                st.add(d)
                resp+=p
        return len(st), resp

N = 4
Jobs = [[1,4,20],[2,1,10],[3,1,40],[4,1,30]]

print(JobScheduling(Jobs,N))