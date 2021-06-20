import numpy as np
import matplotlib.pyplot as plt

x = np.array([[0, 0], [1, 0], [2, 2], [0, 2], [-1, -1]])
plt.scatter(x[:, 0], x[:, 1])
for i in range(x.shape[0]):
    plt.text(x[i, 0]+0.1, x[i, 1], "%i"%i)
plt.axis('equal')
plt.grid()
plt.show()
