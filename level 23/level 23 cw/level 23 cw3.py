# make a list
nums = [2,4,8,9,5]

# insert number 3 at the index 1
nums.insert(1, 3)
# remove the number 9
nums.remove(9)
# make it count 8 times and the final number must be added at the index 0
nums.insert(0,nums.count(8))
# print the list
print(nums[3])