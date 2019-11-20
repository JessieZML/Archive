"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例：
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


"""
关于字典：
可以使用get方法来获取字典中的数据
如：
A = {"a":1, "b":2}
如果取A["c"]则会报错
此时如果想在函数内部进行判断的话，可以使用
result = A.get("c")
避免报错
"""      


# 字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤
# 通过哈希来求解，这里通过字典来模拟哈希查询的过程
def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]

