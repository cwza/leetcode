from typing import List
from collections import deque

'''
Hint:
Say a row of asteroids is stable. What happens when a new asteroid is added on the right?
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        "Stack, Time: O(n), Space: O(n)"
        results = deque([-2000])
        for asteroid in asteroids:
            while True:
                if results[-1] > 0 and asteroid < 1: # Collision
                    if abs(asteroid) > abs(results[-1]):
                        results.pop()
                    elif abs(asteroid) < abs(results[-1]):
                        break
                    else:
                        results.pop()
                        break
                else:
                    results.append(asteroid)
                    break
        results.popleft()
        return list(results)

asteroids = [5,10,-5]
result = Solution().asteroidCollision(asteroids)
assert result == [5,10]

asteroids = [8,-8]
result = Solution().asteroidCollision(asteroids)
assert result == []

asteroids = [10,2,-5]
result = Solution().asteroidCollision(asteroids)
assert result == [10]

asteroids = [-2,-1,1,2]
result = Solution().asteroidCollision(asteroids)
assert result == [-2,-1,1,2]
