
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        space = self.spaces[carType - 1]
        if space <= 0:
            return False
        else:
            self.spaces[carType - 1] -= 1
            return True


obj = ParkingSystem(1, 1, 0)
results = [obj.addCar(param) for param in [1, 2, 3, 1]]
print(results)