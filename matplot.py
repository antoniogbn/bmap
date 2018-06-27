import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

fig = plt.figure()
ax  = fig.add_subplot(111, polar=True)

angles   = [45,60,100,120,270,300]
angles_t = [0,0,0,0,0,0]
r = [0, 1]

for i in range(0,len(angles),2):
    init = angles[i]
    end  = angles[i+1]
    for j in range(init, end):
        ang = (j*(2*pi))/360
        theta=[ang,ang]
        ax.plot(theta,r,'r-')

ax.grid(True)
ax.set_theta_direction(-1)
ax.set_theta_offset(pi/2.0)    

plt.setp(ax.get_yticklabels(), visible=False)
plt.show()