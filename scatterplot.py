import matplotlib.pyplot as plt

import numpy as np

x = np.random.randint(1,10,50)
y = np.random.randint(10,100,50)
color  = np.random.randint(10,100,50)
plt.scatter(x,y,marker="*",cmap="plasma", c= color )#Sequential colormaps (for ordered data):

# 'viridis'
# 'plasma'
# 'inferno'
# 'magma'
# 'cividis'
# Diverging colormaps (for data that has a natural midpoint):

# 'coolwarm'
# 'seismic'
# 'PiYG'
# 'RdBu'
# Qualitative colormaps (for categorical data):

# 'Pastel1'
# 'Set1'
# # 'Paired'
plt.colorbar()
plt.show()