def nextGreNum(nums1,nums2):
    stack=[]
    nge={}
    for i in nums2:
        while stack and i > stack[-1]: #dec. stacl B->T
            nge[stack.pop()]=i #this maps to the actual nge
        stack.append(i)
    while stack:
        nge[stack.pop()]=-1
        
    return [nge[x] for x in nums1]