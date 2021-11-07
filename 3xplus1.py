import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
from itertools import count
import time


result = []
def threexplusone(x):
    # to stop infinite recursion
    if x == 1:
        # result.append(x)
        animate(x)
        return 0
    elif x % 2 !=0 :
        y = 3 * x + 1
        animate(y)
        # result.append(y)
    else:
        y = x / 2
        animate(y)
        # result.append(y)

    return threexplusone(y)
idx = count()
def animate(val):
    print(val)
    result.append(val)
    print(result)
    # plt.cla()
    plt.plot([i for i in range(len(result))], result)
    time.sleep(0.5)
    if result[-1] == 1:
        ani.event_source.stop()


ani = FuncAnimation(plt.gcf(), animate, interval=100, repeat=False)
# threexplusone(11)

plt.tight_layout()
plt.show()