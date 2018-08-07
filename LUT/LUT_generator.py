# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:16:16 2018

@author: Ivan
"""
import numpy as np
import math

#---------------------CONFIGURATION-------------------------------
#=====FUNCTION=====
def function(R,G,B):
    index = 2*G - R - B    
    return index

#=====Variables=====
step = 5
infLimit = 0
supLimit = 255
norm_method = "clip"
#norm_method = "adjust"

#---------------------PROGRAM-------------------------------
print ("=========LUT table generator v1.0=========")
print ("->Parameters set to: ")
print ("\tStep =",step)
print ("\tLowest value =",infLimit)
print ("\tHighest value =",supLimit)

#=====Initialization=====
size = math.ceil(supLimit/step)*math.ceil(supLimit/step)*math.ceil(supLimit/step)
LUT = np.zeros(size)

print ("->Generating table with", size, "positions")
#=====Calculation=====
pos = 0
for iR in range (infLimit,supLimit,step):
   for iG in range (infLimit,supLimit,step):
       for iB in range (infLimit,supLimit,step):           
           LUT[pos]=function(iR,iG,iB)
           pos = pos + 1

max = np.max(LUT)
min = np.min(LUT)

#If values are out of range the results are normalized
if (max>supLimit or min < infLimit):
    print ("->Values out of specified range:")
    print ("\tLowest value =",min)
    print ("\tHighest value =",max)    
    
    if(norm_method == "adjust"):
        print ("->Adjusting values...")
        LUT = LUT - min #Offset adjust
        LUT = (LUT/(max-min))*supLimit #Scale adjust
        
    if(norm_method == "clip"):
        print ("->Clipping values...")
        for ipos in range (0,size):           
            if(LUT[ipos]<infLimit):
                LUT[ipos]=infLimit              
            if(LUT[ipos]>supLimit):
                LUT[ipos]=supLimit 

#=====Exporting Results=====           
print ("->Saving results at LUT.txt file")

with open('LUT.txt','w') as file:
    for i in range(0,size-1):     
        file.write(str(LUT[i]) +"\n")
    file.write(str(LUT[size-1]))        

print ("->LUT generated!")