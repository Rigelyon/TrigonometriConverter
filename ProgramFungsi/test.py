import matplotlib.pyplot as plt
import numpy as np

plt.style.use("_mpl-gallery")

# make data
x = np.arange(0, 10)
y = np.sin(x)

plt.xlabel("x")
plt.ylabel("y = sin(x)")
plt.title("Grafik y = sin(x)")
plt.grid(False)

# plot
plt.plot(x, y)
plt.show()
