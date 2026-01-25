def re(nums:list[int],val)-> int:
    i=0
    for j in range(len(nums)):
        if nums[j]!=val:
            nums[i]=nums[j]
    