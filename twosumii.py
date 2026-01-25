def maxsum( nums:list[int],k:int)-> int:
    w_sum=sum(nums[:k])
    m_sum=w_sum
    for i in range (k,len(nums)):
        w_sum+=nums[i]
        w_sum -=nums[i-k]
        m_sum=max(m_sum,w_sum)
    return m_sum

result= maxsum([1,2,3,4,5,6],3)
print(result)