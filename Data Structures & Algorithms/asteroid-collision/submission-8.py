class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        
        def collide(a):
            if not res:
                res.append(a)
            elif abs(res[-1]) < abs(a + res[-1]) > abs(a):
                res.append(a)
            elif abs(res[-1]) > abs(a):
                if res[-1] < 0:
                    res.append(a)
            elif abs(res[-1]) == abs(a):
                if res[-1] > 0:
                    res.pop()
                else:
                    res.append(a)
            elif abs(res[-1]) < abs(a):
                if res[-1] > 0:
                    res.pop()
                    collide(a)
                else:
                    res.append(a)


        for a in asteroids:
            collide(a)
        
        return res

                    

