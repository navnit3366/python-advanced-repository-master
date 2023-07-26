def fix_calendar(nums):
    while True:
        counter = 0
        for i in range(len(nums)):
            if i < len(nums) - 1:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    break
                else:
                    counter += 1
                    if counter == len(nums):
                        return nums
            else:
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                else:
                    counter += 1
                    if counter == len(nums):
                        return nums
