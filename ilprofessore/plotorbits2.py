import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 8

# reuse the code in orbita2

from orbita2 import main as compute_orbit


# one figure 4 subplots
fig, axes = plt.subplots(2, 2)

# flatten the tuples
listax = axes.flatten()

# enumerate aggiunge un contatore al ciclo

fig.suptitle("Comparision of orbit for different integration steps\n",fontsize=12)
listdt = [ 0.01, 0.001, 0.0001, 0.00001 ]
for i,dt in enumerate(listdt):
    px,py = compute_orbit(listdt[i],False)
    listax[i].set_aspect('equal')
    listax[i].plot(px,py)
    listax[i].plot([0],[0],'o',color='red', alpha=0.9, markersize=6)
    listax[i].plot(px[-1],py[-1],'o',color='blue', alpha=0.9, markersize=4)
    listax[i].set(title="dt = {:.5f}".format(listdt[i]).rstrip('0'))
    listax[i].grid()
fig.tight_layout(pad=3)
fig.savefig("comparedt.pdf",dpi=400)
# plt.show()