from typing import List
from dataclasses import dataclass
from enum import IntEnum

'''
Greedy + Sort: O(nlogn)
'''

class Action(IntEnum):
    DOWN = 1
    UP = 2

@dataclass
class State:
    pos: int
    action: Action
    num_passenger: int


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        states = []
        for num_passenger, start_pos, end_pos in trips:
            states.append(State(start_pos, Action.UP, num_passenger))
            states.append(State(end_pos, Action.DOWN, num_passenger))
        states.sort(key=lambda state: (state.pos, state.action))

        cur_num_passenger = 0
        for state in states:
            action = state.action
            num_passenger = state.num_passenger
            if action == Action.DOWN:
                cur_num_passenger -= num_passenger
            elif action == Action.UP:
                cur_num_passenger += num_passenger
            else:
                raise Exception('Suck!!!')
            if cur_num_passenger > capacity:
                return False
            elif cur_num_passenger < 0:
                raise Exception('Suck!!!')
        return True

trips = [[2,1,5],[3,3,7]]
capacity = 4
result = Solution().carPooling(trips, capacity)
assert result == False

trips = [[2,1,5],[3,3,7]]
capacity = 5
result = Solution().carPooling(trips, capacity)
assert result == True

trips = [[2,1,5],[3,5,7]]
capacity = 3
result = Solution().carPooling(trips, capacity)
assert result == True

trips = [[3,2,7],[3,7,9],[8,3,9]]
capacity = 11
result = Solution().carPooling(trips, capacity)
assert result == True