class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix=0
        ans=0
        seen={}
        for i in range(len(hours)):
            if hours[i]>8:
                prefix+=1
            else:
                prefix-=1
            if prefix>0:
                ans=i+1
            else:

                if prefix-1 in seen:
                    ans = max(ans, i - seen[prefix - 1])
            if prefix not in seen:
                
                seen[prefix] = i
        return ans

        