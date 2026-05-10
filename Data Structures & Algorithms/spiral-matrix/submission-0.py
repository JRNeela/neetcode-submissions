'''
[1,2,3], [4,5,6], [7,8,9]

**tranformation in how we store the data so we can read it better**

[1,2,3] [3, 6, 9] [9, 8, 7]
 1 2 3 4 
 5 6 7 8
 9 10 11 12
 13 14 15 16
4 change of direction for 2x2
5 change of direction for 3x3

We need to accouny for 4 different directions:
left to right
top to down
right to left
down to top

at the end of each iteration, we edit out variables top down left and right

left, right, top, and down are markers as to where the start of each direction is and where it should end for that particular iteration

** we continue while these bounds are true, left < right and top < down
--> if the above is violated, that means we no longer have a rectangle

key: the right and bottom markers serve as walls, whereas the left and top markers represent starts or actual markers

--> this is because of the way the loop logic works, the iterator l and t start and iterate until they've hit the index r or b which they stop (0-index logic)

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        #initialize markers
        left, top = 0, 0
        right, bottom = len(matrix[0]), len(matrix)
        #while we still have a rectangle to enforce our four directions
        while left < right and top < bottom:
            #run l -> r
            for j in range(left, right):
                ret.append(matrix[top][j])
            top += 1
            #run top to bottom
            for i in range(top, bottom):
                ret.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            #run right to left
            for j in range(right - 1, left - 1, -1):
                ret.append(matrix[bottom - 1][j])
            bottom -= 1
            #run bottom to top
            for i in range(bottom - 1, top - 1, -1):
                ret.append(matrix[i][left])
            left += 1
        return ret
        
