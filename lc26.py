def rem(nums:list[int]):
    if not nums:
        return 0
    slow=0
    for fast in range(1,len(nums)):
        if nums[slow]!=nums[fast]:
            nums[slow]=nums[fast]
            slow+=1
    return slow+1

result= rem([1,1,1,2,3])
print(result)