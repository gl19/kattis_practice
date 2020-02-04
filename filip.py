nums = list(input().split())
print(nums[0][::-1]) if int(nums[0][::-1]) > int(nums[1][::-1]) else print(nums[1][::-1])