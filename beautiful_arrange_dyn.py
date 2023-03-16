def beautifulArrangement(array):
    array.sort()
    n = len(array)
    l = 0
    r = n - 1

    arrangement = [0] * n
    for i in range(n):
        if i % 2 == 0:
            arrangement[l] = array[i]
            l += 1
        else:
            arrangement[r] = array[i]
            r -= 1

    return arrangement
def beautifulArrangement1(array):
    array.sort()
    n = len(array)

    # possible arrangements
    arrangements = [[] for _ in range(n+1)]
    arrangements[0] = [[]]

    for i in range(n):
        for j in range(1, n+1):
            if j % array[i] == 0 or array[i] % j == 0:
                for k in range(len(arrangements[j-1])):
                    arrangements[j].append(arrangements[j-1][k]+[array[i]])

    # Return the arrangement of length n
    return arrangements[n]

def beautifulArrangement_bystep(n):
    def backtrack(index, nums):
        if index == 0:
            arrangements.append(list(nums))
            return
        for i in range(index):
            if nums[i] % index == 0 or index % nums[i] == 0:
                nums[i], nums[index-1] = nums[index-1], nums[i]
                backtrack(index-1, nums)
                nums[i], nums[index-1] = nums[index-1], nums[i]

    arrangements = []
    nums = [i+1 for i in range(n)]
    backtrack(n, nums)
    return arrangements

#print(beautifulArrangement([15,10,33,12]))
print(beautifulArrangement1([12,20,2,21]))
#print(beautifulArrangement_bystep(6))