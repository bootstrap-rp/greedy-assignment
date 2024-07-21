def canJump(nums: list[int]) -> bool:

        a = 0
        for val in nums:
            if a < 0:
                return False
            a = max(a, val)
            a -= 1
        return True

print(canJump([2,3,1,1,4]))