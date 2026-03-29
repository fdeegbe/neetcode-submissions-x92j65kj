class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # (index, number, len)
        ans = 1
        q = deque()
        q.append((0,nums[0], 1))
        K = len(nums)
        while q:
            # print(q)
            idx, num, res = q.popleft()
            if idx+1 < K:
                if nums[idx+1] > num:
                    q.append((idx+1,nums[idx+1],res+1)) #take it 
                else:
                    q.append((idx+1,nums[idx+1],1)) # possible reset
                q.append((idx+1,num,res)) # don't take it but continue for possible gaps
            ans = max(ans, res)
        return ans
            

