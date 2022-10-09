import random
from matplotlib import pyplot as plt
import numpy as np

lst = []
n = random.randint(0, 100)
while n > 1:
    if n % 2 == 0:
        n = n / 2
        lst.append(n)
        print(n)



    elif n % 2 == 1:

        n = 3 * n + 1
        lst.append(n)
        print(n)
    else:
        pass

print(lst)

y = np.asarray(lst)
y1 = y.shape[0]
x = np.arange(0, y1)



plt.plot(x,y)
plt.show()
