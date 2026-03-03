
# binary search
# sorted arr
def binary_search(array, x, low, high):
    while low <= high:
        mid = low + high // 2 # floor division
        if array[mid] == x: # found
            return mid

        elif array[mid] < x: # target in upper half
            low = mid + 1

        else: # target in lower half
            high = mid - 1

    return -1

# Kadane's Algorithm
def max_subarr_sum(my_arr):
    # my_arr =  [-2,1,-3,4,-1,2,1,-5,4]

    res = my_arr[0]
    max_ending = my_arr[0]

    for item in my_arr[1:]:
        max_ending = max(max_ending + item, item)

        res = max(max_ending, res)

    return res

def max_subarray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]

    curr_start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(nums[1:])):
        x = nums[i]
        # check if we need to extend or restart
        if x > x + curr_sum:
            curr_sum = x
            curr_start = i
        else:
            curr_sum += x

        # check if we have a better array sum
        if curr_sum > max_sum:
            max_sum = curr_sum
            best_start = curr_start
            best_end = i

    return max_sum, nums[best_start: best_end + 1]

def min_jumps(nums):
    """
    Calculates the minimum number of jumps to reach the end of the array.
    """
    # nums = [2, 3, 1, 1, 4]
    max_end = 0
    curr_end = nums[0]
    jumps = 0
    for index, item in enumerate(nums):
        max_end = max(index + item, max_end)
        if index == curr_end:
            curr_end = max_end
            jumps += 1
        if curr_end >= len(nums):
            return jumps

def longest_increasing_subsequence_len(arr):
    """
    return the length of the longest increasing sequence of an integer array
    does not work for retrieving the actual array itself
    """
    from bisect import bisect_left
    print(arr)
    ans = []
    if not arr:
        return
    for num in arr:
        idx = bisect_left(ans, num)
        if idx == len(ans):
            ans.append(num)
        else:
            ans[idx] = num
    print(ans)
    return len(ans)
