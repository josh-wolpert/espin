import numpy as np
import matplotlib.pyplot as plt
# get_ipython().magic(u'matplotlib inline')

topo = np.loadtxt('data/topo.asc', delimiter=',')

plt.figure(0)
plt.plot(topo[0,:], label='North')

plt.figure(1)
plt.plot(topo[-1,:], 'r--', label='South')

plt.figure(2)
plt.plot(topo[int(len(topo)/2),:], 'g:', linewidth=3, label='Mid')

plt.title('Topographic profiles')
plt.ylabel('Elevation (m)')
plt.xlabel('<-- West    East -->')
plt.legend(loc = 'lower left')

plt.show()
#plt.savefig('media/Your_profiles.png')