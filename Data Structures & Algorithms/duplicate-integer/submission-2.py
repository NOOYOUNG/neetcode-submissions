class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = False
        hashDict = {}
        for n in nums:
            hashDict[n] = hashDict.get(n, 0) + 1

        for n in nums:
            if(hashDict[n] > 1):
                answer = True

        return answer
        