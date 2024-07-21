def kItemsWithMaximumSum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums=[1]*numOnes+[0]*numZeros+[-1]*numNegOnes
        num=0
        for i in range(k):
            num+=nums[i]
        return num

numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2

print(kItemsWithMaximumSum(numOnes,numZeros,numNegOnes,k))