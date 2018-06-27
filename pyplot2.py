import numpy as np
import matplotlib.pyplot as plt


r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

ax = plt.subplot(111, projection='polar')
#ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.set_theta_zero_location("N") #move 0 to north
ax.set_theta_direction('clockwise') #inverts direction to clockwise
ax.grid(True)

#for w in wind:
    #ax.plot(wind_speed, wind_direction, c = bar_colors, zorder = 3)
ax.plot(5, 100, c = '#333333', zorder = 3)


ax.set_title("Blockage Area", va='bottom')
plt.show()