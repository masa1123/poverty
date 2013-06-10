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
#asset a is a numeraire then replaced with consumption goods price
#npa = 3 # of asset price
npc = 3 # of consumption goods price
npk = 3 # of capital price
ntech = 2 # of production technologies

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
def itervalue(next_ev):
    retargset = zeros((nthe,neta,na,nk,npc,npk,ntech))
    #calc value in each asset and capital
    bufmat = zeros((nthe,neta,na,nk,npc,npk,ntech,na,nk))
    for the_i in xrange(nthe):
        for eta_i in xrange(neta):
            for a_i in xrange(na):
                for k_i in xrange(nk):
                    for pc_i in xrange(npc):
                        for pk_i in xrange(npk):
                            for a_j in xrange(na):
                                for k_j in xrange(nk):
                                    #Should he choose production?: NO
                                    consp_h = eta_i * f_h() + (1 - delta)*(1/pc_i)*a_i \
                                        - (1/pc_i)*a_j - (pk_i/pc_i)*k_j
                                    consp_l = eta_i * f_l() + (1 - delta)*(1/pc_i)*a_i \
                                        - (1/pc_i)*a_j - (pk_i/pc_i)*k_j
                                    #next_ev = *** #there is the transition
                                    #given from previous iteration
                                    bufmat[the_i,eta_i,a_i,k_i,pc_i,pk_i,0,a_j,k_j] =\
                                        u(consp_h) + beta * getexp(next_ev,
                                    bufmat[the_i,eta_i,a_i,k_i,pc_i,pk_i,1,a_j,k_j] =\
                                        u(consp_l) + beta * next_ev
    #decide amount of asset and capital
    for the_i in xrange(nthe):
        for eta_i in xrange(neta):
            for a_i in xrange(na):
                for k_i in xrange(nk):
                    for pc_i in xrange(npc):
                        for pk_i in xrange(npk):
                            retargset[the_i,eta_i,a_i,k_i,pc_i,pk_i,0] = \
                                get2argmax(bufmat[the_i,eta_i,a_i,k_i,pc_i,pk_i,0,:,:])
                            retargset[the_i,eta_i,a_i,k_i,pc_i,pk_i,1] = \
                                get2argmax(bufmat[the_i,eta_i,a_i,k_i,pc_i,pk_i,1,:,:])
    return retargset

#Doesn't the future value depend upon the futer prices?
def getexp(vmat,the,eta,a,k,pc,pk,a,k

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
