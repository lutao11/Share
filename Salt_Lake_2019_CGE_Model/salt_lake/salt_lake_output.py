"""
# After running a model, use solution dictionaries to replicate GAMS
# results with DataFrames.
#
# NOTE:
# Solution variables stored in "vars" and "soln" objects should
# be the primary source for model evaluation.
# This was only created to assist those unfamiliar with python objects.
"""

import pandas as pd

#CG0
CG0 = vars.get('CG', x=soln[0])

#CH0
CH0 = vars.get('CH', x=soln[0])

#CMI0
CMI0 = vars.get('CMI', x=soln[0])

#CMO0
CMO0 = vars.get('CMO', x=soln[0])

#CN0
CN0 = vars.get('CN', x=soln[0])

#CPI0
CPI0 = vars.get('CPI', x=soln[0])

#CX0
CX0 = vars.get('CX', x=soln[0])

#D0
D0 = vars.get('D', x=soln[0])

#DD0
DD0 = vars.get('DD', x=soln[0])

#DS0
DS0 = vars.get('DS', x=soln[0])

#FD
FD0 = vars.get('FD', x=soln[0])

#IGT
IGT0 = vars.get('IGT', x=soln[0])

#KS
KS0 = vars.get('KS', x=soln[0])

#LAS
#LAS0 = vars.get('LAS', x=soln[0])

#HH
HH0 = vars.get('HH', x=soln[0])

#HN
HN0 = vars.get('HN', x=soln[0])

#HW
HW0 = vars.get('HW', x=soln[0])

#M
M0 = vars.get('M', x=soln[0])

#N
N0 = vars.get('N', x=soln[0])

#NKI
NKI0 = vars.get('NKI', x=soln[0])

#LNFOR
#LNFOR0 = vars.get('LNFOR', x=soln[0])

#KPFOR
KPFOR0 = vars.get('KPFOR', x=soln[0])

#GVFOR
GVFOR0 = vars.get('GVFOR', x=soln[0])

#P
P0 = vars.get('P', x=soln[0])

#PD
PD0 = vars.get('PD', x=soln[0])

#PVA
PVA0 = vars.get('PVA', x=soln[0])

#RA
RA0 = vars.get('RA', x=soln[0])

#R
R0 = vars.get('R', x=soln[0])

#S
S0 = vars.get('S', x=soln[0])

#SPI
SPI0 = vars.get('SPI', x=soln[0])

#V
V0 = vars.get('V', x=soln[0])

#Y
Y0 = vars.get('Y', x=soln[0])

#Yd
YD0 = vars.get('YD', x=soln[0])

emplist = []
dsrlist = []
dsclist = []
hhinclist = []
miglist = []
simlist = []

for i in range(iNum):

    CGL = vars.get('CG', x=soln[i+1])
    CHL = vars.get('CH', x=soln[i+1])
    CMIL = vars.get('CMI', x=soln[i+1])
    CMOL = vars.get('CMO', x=soln[i+1])
    CNL = vars.get('CN', x=soln[i+1])
    CPIL = vars.get('CPI', x=soln[i+1])
    CXL = vars.get('CX', x=soln[i+1])
    DL = vars.get('D', x=soln[i+1])
    DDL = vars.get('DD', x=soln[i+1])
    DSL = vars.get('DS', x=soln[i+1])
    FDL = vars.get('FD', x=soln[i+1])
    IGTL = vars.get('IGT', x=soln[i+1])
    KSL = vars.get('KS', x=soln[i+1])
    #LASL = vars.get('LAS', x=soln[i+1])
    HHL = vars.get('HH', x=soln[i+1])
    HNL = vars.get('HN', x=soln[i+1])
    HWL = vars.get('HW', x=soln[i+1])
    ML = vars.get('M', x=soln[i+1])
    NL = vars.get('N', x=soln[i+1])
    NKIL = vars.get('NKI', x=soln[i+1])
    #LNFORL = vars.get('LNFOR', x=soln[i+1])
    KPFORL = vars.get('KPFOR', x=soln[i+1])
    GVFORL = vars.get('GVFOR', x=soln[i+1])
    PL = vars.get('P', x=soln[i+1])
    PDL = vars.get('PD', x=soln[i+1])
    PVAL = vars.get('PVA', x=soln[i+1])
    RAL = vars.get('RA', x=soln[i+1])
    RL = vars.get('R', x=soln[i+1])
    SL = vars.get('S', x=soln[i+1])
    SPIL = vars.get('SPI', x=soln[i+1])
    VL = vars.get('V', x=soln[i+1])
    YL = vars.get('Y', x=soln[i+1])
    YDL = vars.get('YD', x=soln[i+1])

    #DFCG.L(I,G)      = CG.L(I,G)-CG0(I,G);
    DFCG = CGL - CG0

    #DFFD.L(F,Z)      = FD.L(F,Z)-FD0(F,Z);
    DFFD = FDL - FD0

    #DK.L(K,Z)        = FD.L(K,Z)-FD0(K,Z);
    DK = KSL - KS0

    #DY.L(Z)          = Y.L(Z)-Y0(Z);
    #DY = YL - Y0
    DY = (YL/CPIL) - Y0

    #DDS.L(I)         = DS.L(I)-DS0(I);
    DDS = DSL - DS0

    #DDD.L(I)         = DD.L(I) - DD0(I);
    DDD = DDL - DD0

    #DCX.L(I)         = CX.L(I) -CX0(I);
    DCX = CXL - CX0

    #DCH.L(I,H)       = CH.L(I,H) - CH0(I,H);
    DCH = CHL - CH0

    #DRR.L(F,Z)       = R.L(F,Z)-R0(F,Z);
    DR = RL - R0

    #DCMI.L(L)        = CMI.L(L) - CMI0(L);
    DCMI = CMIL - CMI0

    #DCMO.L(CM)       = CMO.L(CM) - CMO0(CM);
    DCMO = CMOL - CMO0

    DM = ML - M0

    DV = VL - V0

    DN = NL - N0

    s_name = 'Simulation ' + str(i+1)


    emp = DFFD[DFFD.index.isin(['L1W_R1', 'L2W_R1', 'L3W_R1', 'L4W_R1', 'L1W_R2', 'L2W_R2', 'L3W_R2', 'L4W_R2', 'L1W_R3', 'L2W_R3', 'L3W_R3', 'L4W_R3',
     'L1W_R4', 'L2W_R4', 'L3W_R4', 'L4W_R4', 'L1W_R5', 'L2W_R5', 'L3W_R5', 'L4W_R5', 'L1W_R6', 'L2W_R6', 'L3W_R6', 'L4W_R6',
     'L1W_R7', 'L2W_R7', 'L3W_R7', 'L4W_R7'])].sum().sum()
    dsr = DDS[DDS.index.isin(['HS1_R1', 'HS2_R1', 'HS1_R2', 'HS2_R2', 'HS1_R3', 'HS2_R3', 'HS1_R4', 'HS2_R4', 'HS1_R5', 'HS2_R5', 'HS1_R6', 'HS2_R6', 'HS1_R7', 'HS2_R7'])].sum()
    dsc = DDS[DDS.index.isin(['AG_MI_R1', 'UTIL_R1', 'CONS_R1', 'MANU_R1', 'COMMER_R1', 'EDU_R1', 'HEALTH_R1', 'ART_ACC_R1', 'RELIG_R1', 
     'AG_MI_R2', 'UTIL_R2', 'CONS_R2', 'MANU_R2', 'COMMER_R2', 'EDU_R2', 'HEALTH_R2', 'ART_ACC_R2', 'RELIG_R2',
     'AG_MI_R3', 'UTIL_R3', 'CONS_R3', 'MANU_R3', 'COMMER_R3', 'EDU_R3', 'HEALTH_R3', 'ART_ACC_R3', 'RELIG_R3',
     'AG_MI_R4', 'UTIL_R4', 'CONS_R4', 'MANU_R4', 'COMMER_R4', 'EDU_R4', 'HEALTH_R4', 'ART_ACC_R4', 'RELIG_R4',
     'AG_MI_R5', 'UTIL_R5', 'CONS_R5', 'MANU_R5', 'COMMER_R5', 'EDU_R5', 'HEALTH_R5', 'ART_ACC_R5', 'RELIG_R5',
     'AG_MI_R6', 'UTIL_R6', 'CONS_R6', 'MANU_R6', 'COMMER_R6', 'EDU_R6', 'HEALTH_R6', 'ART_ACC_R6', 'RELIG_R6',
     'AG_MI_R7', 'UTIL_R7', 'CONS_R7', 'MANU_R7', 'COMMER_R7', 'EDU_R7', 'HEALTH_R7', 'ART_ACC_R7', 'RELIG_R7'])].sum()
    hhinc = DY[DY.index.isin(['HH1_R1', 'HH2_R1', 'HH3_R1', 'HH4_R1', 'HH1_R2', 'HH2_R2', 'HH3_R2', 'HH4_R2', 'HH1_R3', 'HH2_R3', 'HH3_R3', 'HH4_R3', 'HH1_R4', 'HH2_R4', 'HH3_R4', 'HH4_R4',
     'HH1_R5', 'HH2_R5', 'HH3_R5', 'HH4_R5', 'HH1_R6', 'HH2_R6', 'HH3_R6', 'HH4_R6', 'HH1_R7', 'HH2_R7', 'HH3_R7', 'HH4_R7'])].sum()
    hhdiff = HHL-HH0
    mig = hhdiff.sum()

    emplist.append(emp)
    dsrlist.append(dsr)
    dsclist.append(dsc)
    hhinclist.append(hhinc)
    miglist.append(mig)
    simlist.append(s_name)

cols = {'DSC' : dsclist,
        'DSR' : dsrlist,
        'MIG' : miglist,
        'EMP' : emplist,
        'HHINC' : hhinclist}

df = pd.DataFrame.from_dict(cols)
df.to_csv('Salt_Lake_Results.csv')