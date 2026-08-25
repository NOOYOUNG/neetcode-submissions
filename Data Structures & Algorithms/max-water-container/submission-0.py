class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxA = 0

        while(left < right) : 
            width = right - left
            height = min(heights[left], heights[right])
            currentMax = width * height

            if(maxA < currentMax) :
                maxA = currentMax

            if(heights[left] < heights[right]):
                left += 1
            else :
                right -= 1

        return maxA