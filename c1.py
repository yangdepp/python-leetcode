# give an array of integers,return includes of two numbers such that they add up to a specific target.
# you may assume that each input would exactly one solution, and you may not use the same element twice.


# def twoSum(nums, target):
#     if len(nums) <= 1:
#         return False
#     buff_dict = {}
#     for i in range(len(nums)):
#         if nums[i] in buff_dict:
#             return [buff_dict[nums[i]], i]
#         else:
#             buff_dict[target - nums[i]] = i


# print(twoSum([1, 2, 3, 4, 5, 6, 7], 8))


# python3实现
def twoSum1(nums, target):
    looktable = {}
    # enumerate实现带下标的循环，i是下标
    for i, v in enumerate(nums):
        if target - v in looktable:
            return [looktable[target - v], i]
        looktable[v] = i


print(twoSum1([1,2,3,4,5,6,7],8))