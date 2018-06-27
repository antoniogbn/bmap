#EXTERNALS
import re
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

#CLASSES AND METHODS DEFINITIONS
class AntennaController(object):

    def __init__(self):
        self.dump=""

        #Blockage limits array - equipment supports up to 3 ranges
        #Array setup = [l1_start,l1_end,l2_start,l2_end,l3_start,l3_end]
        self.limit_angles = [ 0, 0, 0, 0, 0, 0]
        
        #Regular expressions array to be used to find blockage limites values on config string
        #Needs to have the same size of limit_angles
        self.limit_string = ["mT.{1,36}","mV.{1,36}","mZ.{1,36}","m\\\.{1,36}","m\^.{1,36}","m`.{1,36}"]

        #Antenna azimuth poiting, default = not set (-1)
        self.pointing_azimuth = -1

    def __str__(self):
        saida = '=================================================== \n'
        saida = saida + 'Blockage Area Ranges \n'
        saida = saida + '=================================================== \n'
        j=0 
        for i in range(0,len(self.limit_angles),2):
            j+=1
            saida = saida + 'Range {} starts at {} degress and ends at {} degress \n'.format(j,self.limit_angles[i], self.limit_angles[i+1])
        saida = saida + '\nAntenna pointing azimuth equals to  {} \n'.format(self.pointing_azimuth)
        saida = saida + '=================================================== \n'
        return saida

    def OpenDumpFile(self,file):
        with open(file, 'r') as dumpfile:
            self.dump=dumpfile.read().replace('\n', '')

    def GetBlockageMap(self):
        for i in range(0,len(self.limit_angles),2):
            strre = re.compile('{}'.format(self.limit_string[i]))
            line = strre.findall(self.dump)
            line = line[0]
            if line:
                lim1 = int(line[34:38])
            strre = re.compile('{}'.format(self.limit_string[i+1]))
            line2 = strre.findall(self.dump)
            line2 = line2[0]
            if line:
                lim2 = int(line2[34:38])
            if lim1 > lim2:
                self.limit_angles[i]   = int(lim2/10)
                self.limit_angles[i+1] = int(lim1/10)
            else:
                self.limit_angles[i]   = int(lim1/10)
                self.limit_angles[i+1] = int(lim2/10)

    def SetAntennaAzimuth(self,az):
        if (az < 0) or (az > 360):
            print("Wrong azimuth value !")
        else:
            self.pointing_azimuth = az

    def ShowBlockageMap(self):
        angles   = self.limit_angles
        angles_t = [0,0,0,0,0,0]
        r = [0, 1]
        fig = plt.figure()
        ax  = fig.add_subplot(111, polar=True)
        for i in range(0,len(angles),2):
            init = angles[i]
            end  = angles[i+1]
            for j in range(init, end):
                ang = (j*(2*pi))/360
                theta=[ang,ang]
                ax.plot(theta,r,'r-')
        
        if (self.pointing_azimuth >- 1):
            ang=(self.pointing_azimuth*(2*pi))/360
            theta=[ang,ang]
            ax.plot(theta,r,'b-')

        ax.grid(True)
        ax.set_theta_direction(-1)
        ax.set_theta_offset(pi/2.0)
        ax.set_title("Blockage Area Mapper ", va='bottom')    

        plt.setp(ax.get_yticklabels(), visible=False)
        plt.show()

#RUN THE PROGRAM

#Creates a new Antenna Controller Object
MyAntennaController = AntennaController()

#Opens the dump file containing the Antenna controller configuration
MyAntennaController.OpenDumpFile('antenna.dump') 

#Extract blockage from configuration string
MyAntennaController.GetBlockageMap()

#Sets antenna pointing azimuth direction
MyAntennaController.SetAntennaAzimuth(235)

#Print outs the class created
print(MyAntennaController)

#Plots Blockage Map
MyAntennaController.ShowBlockageMap()


