# -*- coding:utf-8 -*-
#=====================
#
# POVERTY TRAP HETERO MACRO
# with Sawada Masayuki
#
#=====================
from numpy import *
from tauchen import tauchen

# ===Settings===
tcapital = ***
nagent = ***
simt = 1100
dropt = 100


# ===Parameters===


# ===Grid===
nthe = 3 # of theta_i (inidividual prod)
neta = 3 # of theta (aggeregate prod)
na = 3 # of asset (non-productive)
nk = 3 # of productive capital
npa = 3 # of asset price
npk = 3 # of capital price

# ===Model Functions===

def u(c):
    return log(c)

def f_h():
    return
def f_l():
    return

# ===Functions===

#get argmax from 2-dim matrix
def get2argmax(m):
    return [a,b]

#Value iteration
def itervalue():
    retargset = zeros((nthe,neta,na,nk,npa,npk))
    #calc value in each asset and capital
    bufmat = zeros((nthe,neta,na,nk,npa,npk,na,nk))
    for the_i in xrange(nthe):
        for eta_i in xrange(neta):
            for a_i in xrange(na):
                for k_i in xrange(nk):
                    for a_j in xrange(na):
                        for k_j in xrange(nk):
                            #Should he choose production?
                            consp = ***
                            next_ev = *** #there is the transition
                            bufmat[the_i,eta_i,a_i,k_i,a_j,k_j] = u(consp) + beta * next_ev
    #decide amount of asset and capital
    for the_i in xrange(nthe):
        for eta_i in xrange(neta):
            for a_i in xrange(na):
                for k_i in xrange(nk):
                    retargset[the_i,eta_i,a_i,k_i] = get2argmax(bufmat[the_i,eta_i,a_i,k_i,:,:])
    return retargset

#Simulation

def getprice(priceset):
    pa,pc = priceset
    paarg = find_nearest(pagrid,pa)
    pkarg = find_nearest(pkgrid,pk)

    #check market clearing conditions of asset and capital hold
    difasset = 0.0
    difcapital = 0.0
    for i in xrange(nagent):
        aarg, karg = retargset[thetaset[i],eta,assetset[i],capitalset[i],paarg,pkarg]
        difasset += agrid[aarg]
        difcapital += kgrid[karg]
    difcapital -= tcapital

    return difasset,difcapital
    
#Outer iteration



# ===Main===

# Containers (with initial)
#every data contains its index
thetaset = zeros(nagent)
assetset = zeros(nagent)
capitalset = zeros(nagent) + tcapital / nagent #CAUTION!!!THIS SHOULD BE INDEX

# initial aggregate info
eta = ***
paarg = ***
pkarg = ***

# initial value function
retargset = itervalue()

for i in xrange(simt):
    # get price
    paarg,pkarg = fsolve(getprice,[paarg,pkarg])
    for j in xrange(nagent):
        # get asset and capital of each agents
        aarg, karg = retargset[thetaset[i],eta,assetset[i],capitalset[i],paarg,pkarg]
        assetset[j] = aarg
        capitalset[j] = karg
        if i > dropt:
            writecsv(***)
    # transition of 
    eta = transeta(eta)
    for j in xrange(nagent):
        thetaset[j] = transtheta(thetaset[j])








