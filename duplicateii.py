class solutions:
    def duplicate(self,nums:list[int],k:int) ->int:
        seen=dict()
        for id, val in nums:
            if val in seen and id -seen[val] <=k:
                return True
            seen[val]=id
        return False