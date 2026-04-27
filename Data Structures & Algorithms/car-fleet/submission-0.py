from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = deque()

        cars = sorted(zip(position, speed), reverse=True)
        # [(7, 1), (4, 2), (1, 2), (0, 1)]

        for pos, spd in cars:
            time = (target - pos) / spd

            # if current time >= top of stack, its part of fleet, append to stack, else its next fleet
            if not stack:
                stack.append(time)

            if stack and time > stack[-1]:
                stack.append(time)

        return len(stack)