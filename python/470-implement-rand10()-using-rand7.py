import random
from matplotlib import pyplot as plt

"https://blog.csdn.net/fuxuemingzhu/article/details/81809478"

def rand1_7():
    " ~unif(1, 2, 3, 4, 5, 6, 7) "
    return random.randint(1, 7)

def rand0_6():
    " ~unif(0, 1, 2, 3, 4, 5, 6) "
    return rand1_7() - 1
def rand0_48():
    " ~unif(0, 1, 2, 3, ..., 48) "
    num1 = rand0_6() # ~unif(0, 1, 2, 3, 4, 5, 6)
    num2 = rand0_6() * 7  # ~unif(0, 7, 14, 21, 28, 35, 42)
    num3 = num1 + num2 # ~unif(0, 1, 2, 3, ..., 48)
    return num3
def rand0_39():
    " use rejection sampling to return ~unif(0, 1, 2, 3, ..., 39) "
    num = rand0_48() # ~unif(0, 1, 2, 3, ..., 48)
    if num > 39:
        return rand0_39()
    return num
def rand0_9():
    " ~unif(0, 1, 2, 3, 4, 5, 6, 7, 8, 9) "
    return rand0_39() % 10
def rand1_10():
    " ~unif(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) "
    return rand0_9() + 1


# plt.hist([rand7() for _ in range(10000)], bins=7)
# plt.hist([rand0_6() for _ in range(10000)], bins=7)
# plt.hist([rand0_48() for _ in range(100000)], bins=49)
# plt.hist([rand0_39() for _ in range(100000)], bins=40)
# plt.hist([rand0_9() for _ in range(10000)], bins=10)
plt.hist([rand1_10() for _ in range(10000)], bins=10)
plt.show()