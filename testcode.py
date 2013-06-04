#=================================#
#Test code for lom.py             #
# coding: utf-8                   #
#=================================#

#test2

import lom
import numpy as np
import time

def st_time():
   return time.clock()

def en_time(sttime):
   entime = time.clock()
   return (entime - sttime)

#set initial variables
N = 10**4
KT = np.random.rand(1,N)
LT = np.random.rand(1,N)
KTT = 0.1 + 1.2*KT + 0.2*LT + (1 - 2*np.random.rand(1,N))*0.05
k0 = np.random.rand(1)
k1 = np.random.rand(1)
k2 = np.random.rand(1)

sttime = st_time()
[coef,exit_flag,sR2] = lom.regression(KT,LT,KTT,k0,k1,k2)
print "coef:",coef[0],coef[1],coef[2]
print "exit_flag:",exit_flag
print "R2:",sR2
time_spnt = en_time(sttime)
print "time:",time_spnt
