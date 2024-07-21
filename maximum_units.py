def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:
        

        sort = sorted(boxTypes, key= lambda x: x[1], reverse = True)
        ans = 0
        box = 0
        for i in sort:

            ans += i[0] * i[1]
            box += i[0]

            if box > truckSize:

                diff = box - truckSize
                ans -= i[1] * diff
                break

        return ans

print(maximumUnits([[1,3],[2,2],[3,1]],4))