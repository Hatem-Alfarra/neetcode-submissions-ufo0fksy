class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        stack = []
        n = len(position)
        k = 0

        for i in range(n):
            fleets.append([position[i], speed[i]])
        
        fleets = sorted(fleets, reverse=True)

        fleetI = 0
        while fleetI < n:
            p = fleets[fleetI][0]
            s = fleets[fleetI][1]
            stack.append((target - p)/ s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            fleetI += 1
        return len(stack)

       