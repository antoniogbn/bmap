import math
angle=[0.,5.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,65.,70.,75.,\
       80.,85.,90.,95.,100.,105.,110.,115.,120.,125.]

angle = [math.radians(a) for a in angle]


lux=[12.67,12.97,12.49,14.58,12.46,12.59,11.26,10.71,17.74,25.95,\
     15.07,7.43,6.30,6.39,7.70,9.19,11.30,13.30,14.07,15.92,14.70,\
     10.70,6.27,2.69,1.29,0.81]

import matplotlib.pyplot as P
import matplotlib
P.clf()
sp = P.subplot(1, 1, 1, projection='polar')
sp.set_theta_zero_location('N')
sp.set_theta_direction(-1)
P.plot(angle, lux)
P.show()