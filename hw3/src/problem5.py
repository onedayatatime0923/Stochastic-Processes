import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(10,10))
plt.gca().set_aspect(aspect='equal')
plt.gca().add_patch(plt.Circle((0,0), 1, fill=False))


numpoints = np.random.poisson(100)
#  numpoints = 3

alpha = 2 * np.pi * np.random.random(numpoints)
# random radius
r = np.sqrt(np.random.random(numpoints))
# calculating coordinates
xcoods = r * np.cos(alpha)
ycoods = r * np.sin(alpha)
colors = np.linspace(0,1, num = numpoints, endpoint = True)

plt.scatter(xcoods, ycoods, c=colors, marker='o', s = 36)
plt.savefig("result.png")
#  plt.show()
