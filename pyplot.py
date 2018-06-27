from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

#angles = 2*pi*np.random.randint(0,864000,100)/86400
angles = 2*pi*np.arange(1)/86400

print(angles)
#angles = 
ax = plt.subplot(111, polar=True)
ax.scatter(angles, np.ones(1)*1)

# suppress the radial labels
plt.setp(ax.get_yticklabels(), visible=False)

# set the circumference labels
##ax.set_xticks(np.linspace(0, 2*pi, 360, endpoint=False))
##ax.set_xticklabels(range(8))

# make the labels go clockwise
ax.set_theta_direction(-1)

# place 0 at the top
ax.set_theta_offset(pi/2.0)    

# plt.grid('off')
ax.bar(angles, np.full(1, 0.9), width=0.1, bottom=0.0, color='r', linewidth=0)
# put the points on the circumference
plt.ylim(0,1)

plt.show()