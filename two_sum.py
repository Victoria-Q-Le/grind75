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
print(numMAp)