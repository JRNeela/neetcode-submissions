# There are n cars traveling to the same destination on a one-lane highway.
# positions == integers, position of car list -- n
# speed == integers, speed of car list -- n 

# target --> number of miles needed to reach the desitination

# A car can not pass another car ahead of it. 
# It can only catch up to another car and then drive at 
# the same speed as the car ahead of it.
# --> once a car is at the same position it must adhere to the speed
# of the next car i+1 ==> car fleet

# If a car catches up to a car fleet the moment the fleet reaches the destination, 
# then the car is considered to be part of the fleet.
# (car hits destination at the same time as car 2 they are considered to be part of the same 
# fleet)

# Return the number of different car fleets that will arrive at the destination.


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for pos, s in zip(position, speed):
            pairs.append((pos, s))
        stack = []
        pairs.sort(reverse = True)
        for pos, s in pairs:
            time = (target - pos)/s
            stack.append(time)
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)