# PROBLEM
# Given a array of intergers nums and an interger target, return indices of the two numbers such that they add uo to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice. 
# You can return the answer in any order. 
# 

nums = [1,25,4,5,6,8,3]
target = 6 

numMAp = {}
n = len(nums)

for i in range(n):
    numMAp[nums[i]] = i #assign each number in the num array into a dictionary whose key is the actual number and the value is their indice.

for i in range(n):
    complement = target - nums[i] #for each key in the numMap dict, calculate the complement value that makes target
    if complement in numMAp and numMAp[complement] != i: #if complement is also in numMAp and indice of complement is not indice of key, incase number is even so that there 2 similiar inside the numMap. 
        print(i, numMAp[complement])