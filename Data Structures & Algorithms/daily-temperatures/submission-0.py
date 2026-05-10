class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [30,38,30,36,35,40,28]
        [(38, 1), (36, 3), (40, 5) ]
        [1, 0, 1, 0, 1, 0]
        '''

        output = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        return output
