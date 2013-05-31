#=================================#
#module for law of motion process #
# coding: utf-8                   #
#=================================#

import numpy as np

def regression(KT,LT,KTT,k0,k1,k2):
#find regression coefficients:coef = [ks0,ks1,ks2]
    KT = np.asarray(KT)
    LT = np.asarray(LT)
    KTT = np.asarray(KTT)
    X  = np.vstack([KT,LT])
    trX = np.transpose(X)
    XX = np.dot(X,trX)
    YX = np.transpose(np.dot(KTT,trX))
    invXX = np.linalg.inv(XX)
    EKT = np.mean(KT)
    ELT = np.mean(LT)
    EKTT = np.mean(KTT)

    V = np.cov(KTT)

    [ks1,ks2] = np.dot(invXX,YX)
    ks0 = EKTT - EKT*ks1 - ELT*ks2
    coef = [ks0,ks1,ks2]

#calculate R2 with current coef:cR2
    cR2 = 0
    for x in range(np.size(KT)):
        cR2 = cR2 + (k0 + k1*KT[0,x] + k2*LT[0,x] - KTT[0,x])**2  
    cR2 = 1 - (cR2/np.size(KT))/V

#calculate R2 with regressed coef:sR2
    sR2 = 0
    for x in range(np.size(KT)):
        sR2 = sR2 + (coef[0] + coef[1]*KT[0,x] + coef[2]*LT[0,x] - KTT[0,x])**2
    sR2 = 1 - (sR2/np.size(KT))/V

#loop exit flag = 1 if regressed one is closer to 1
    exit_flag = 0
    coef_report = [k0,k1]
    if abs(abs(sR2) - abs(cR2)) < 10**(-6):
        exit_flag = 1
        coef_report = coef
    
    return coef,exit_flag,sR2
