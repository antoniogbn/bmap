import re
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt


class AntennaController(object):

    def __init__(self,d):
        self.dump=d
        self.limit_angles = [ 0, 0, 0, 0, 0, 0]
        self.limit_string = ['mT.{1,36}','mV.{1,36}']

    def __str__(self):
        saida = 'Blockage Area Ranges \n' 
        for i in range(0,len(self.limit_angles),2):
            saida = saida + 'Range {} starts at {} and ends at {}\n'.format(i,self.limit_angles[i], self.limit_angles[i+1])
        return saida

    def ProcessaDump(self):
        # RANGE INTERVAL 1
        for i in range(0,len(self.limit_angles),2):
        strre = re.compile(r'mT.{1,36}')
        line = strre.findall(self.dump)
        line = line[0]
        if line:
            print(line)
            lim1 = int(line[34:38])
        strre = re.compile(r'mV.{1,36}')
        line = strre.findall(self.dump)
        line = line[0]
        if line:
            print(line)
            lim2 = int(line[34:38])
        if lim1 > lim2:
            self.brange1s = lim2/10
            self.brange1e = lim1/10
        else:
            self.brange1s = lim1/10
            self.brange1e = lim2/10

        # RANGE INTERVAL 2
        strre = re.compile(r'mZ.{1,36}')
        line = strre.findall(self.dump)
        line = line[0]
        if line:
            print(line)
            lim1 = int(line[34:38])
        strre = re.compile(r'm\\.{1,36}')
        line = strre.findall(self.dump)
        line = line[0]
        if line:
            print(line)
            lim2 = int(line[34:38])
        if lim1 > lim2:
            self.brange2s = lim2/10
            self.brange2e = lim1/10
        else:
            self.brange2s = lim1/10
            self.brange2e = lim2/10
        # RANGE INTERVAL 3
        strre = re.compile(r'm\^.{1,36}')
        line = strre.findall(self.dump)
        line = line[0]
        if line:
            print(line)
            lim1 = int(line[34:38])
        strre = re.compile(r'm\\.{1,36}')
        line = strre.findall(self.dump)
        line = line[0]
        if line:
            print(line)
            lim2 = int(line[34:38])
        if lim1 > lim2:
            self.brange3s = lim2/10
            self.brange3e = lim1/10
        else:
            self.brange3s = lim1/10
            self.brange3e = lim2/10


#####################################################

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


#####################################################

with open('antenna.dump', 'r') as dumpfile:
    dumpdata=dumpfile.read().replace('\n', '')

MyAntenna = Antenna(dumpdata)

MyAntenna.ProcessaDump()

print(MyAntenna)
