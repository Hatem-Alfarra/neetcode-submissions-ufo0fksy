class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        def collide(a):    
            if not res:
                res.append(a)
            elif res[-1] < 0:
                res.append(a)
            elif res[-1] > 0 and a > 0:
                res.append(a)
            elif res[-1] > 0 and a < 0:
                if abs(res[-1]) == abs(a):
                    res.pop()
                elif res and res[-1] > 0 and a < 0 and abs(res[-1]) < abs(a):
                    res.pop()
                    collide(a)
        
        for a in asteroids:
            collide(a)    

        return res
                    
                    