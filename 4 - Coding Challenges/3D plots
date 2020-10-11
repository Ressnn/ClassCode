#plot this function from -2 to 2 on both x, y, and treat
# f(x,y) as your z
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x,y):
    return x**2 + y**2

points = np.mgrid[-2:2:.01,-2:2:.01]
z = f(points[0],points[1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.tri_surf(points[0], points[1], z, cmap="magma")
