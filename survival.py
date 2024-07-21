def minimumDays( S, N, M):
        # code here
        total_food = S*M
        if N < M:
            return -1
        if (N-M)*6 < M and S > 6:
            return -1
        if total_food%N == 0 and N == M and S > 6:
            food = -1
        elif total_food%N == 0:
            food = total_food//N
        else:
            food = total_food//N + 1
        return food

print(minimumDays(10,16,2))