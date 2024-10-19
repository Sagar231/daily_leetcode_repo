# find the kth bit of Sn tring 1545

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(s,cnt):
            if cnt==n:
                return s
            temps = ""
            for i in range(len(s)-1,-1,-1):
                if s[i]=="0":
                    temps +="1"
                else:
                    temps +="0"
            return helper(s+"1"+temps,cnt+1)
        s = helper("0",1)
        return s[k-1]