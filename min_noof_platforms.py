def findPlatform(arr, dep, n):
    plat_needed = 1
    result = 1
    for i in range(n):
        plat_needed = 1

        for j in range(n):
            if i != j:
                if (arr[i] >= arr[j] and dep[j] >= arr[i]):
                    plat_needed += 1

        result = max(result, plat_needed)

    return result

