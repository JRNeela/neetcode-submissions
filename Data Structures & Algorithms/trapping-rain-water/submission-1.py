# Return the maximum area of water that can be trapped between the bars.

# if there is a space --> you know by a 0
# after that --> height in that space is determined by the smaller of the outside
# two points


class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1 
        maxLeft = 0
        maxRight = 0
        count = 0
        while l < r:
            if height[l] <= height[r]:
                maxLeft = max(height[l], maxLeft)
                count += maxLeft - height[l]
                l += 1
            else:
                maxRight = max(height[r], maxRight)
                count += maxRight - height[r]
                r -= 1
        return count


        