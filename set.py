# Synatx for creating a Set
my_set = {1,2,3,4,5}
print(my_set)

# ----OR----
nums = set((1,2,3,4,5))
print(nums)

# Check the legth of a set
print(len(nums))

# Check the if a vaule exits
print(3 in nums)

# No duplicate is allowed in set
another_nums = {1,2,4,5,6,4,2,2,2,3}
print(another_nums)

# Add a new value to a set
nums.add(10)
print(nums)

# Merge two sets
more_nums = {11,22,12,23,13}
nums.update(more_nums)
print(nums)

# ----Merge toe sets to create a new one-----
new_set = nums.union(more_nums)
print(new_set)

# Print the duplicates
one = {1,2,3,4}
two = {4,2,3,5}

one.intersection_update(two)
print(one)

# Print everything except the duplicates
one = {1,2,3,4,7}
two = {4,2,3,5,6}

one.symmetric_difference_update(two)
print(one)