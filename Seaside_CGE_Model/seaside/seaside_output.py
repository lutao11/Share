"""
# After running a model, use solution dictionaries to replicate GAMS
# results with DataFrames
#
# NOTE:
# solution variables stored in "vars" and "soln" objects should
# be the primary source for model evaluation.
# This swas only created to assist those unfamiliar with python objects
"""

import pandas as pd

#CG0
CG0 = vars.get('CG', x=soln[0])

#CH0
CH0 = vars.get('CH', x=soln[0])

#CMI0
#CMI0 = vars.get('CMI', x=soln[0])

#CMO0
#CMO0 = vars.get('CMO', x=soln[0])

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
LAS0 = vars.get('LAS', x=soln[0])

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
LNFOR0 = vars.get('LNFOR', x=soln[0])

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

# DIFFERENCES
#writer = pd.ExcelWriter('test.xlsx',engine='xlsxwriter')
#workbook=writer.book

emplist = []
dsrlist = []
dsclist = []
hhinclist = []
miglist = []
simlist = []

for i in range(iNum):

    CGL = vars.get('CG', x=soln[i+1])
    CHL = vars.get('CH', x=soln[i+1])
    #CMIL = vars.get('CMI', x=soln[i+1])
    #CMOL = vars.get('CMO', x=soln[i+1])
    CNL = vars.get('CN', x=soln[i+1])
    CPIL = vars.get('CPI', x=soln[i+1])
    CXL = vars.get('CX', x=soln[i+1])
    DL = vars.get('D', x=soln[i+1])
    DDL = vars.get('DD', x=soln[i+1])
    DSL = vars.get('DS', x=soln[i+1])
    FDL = vars.get('FD', x=soln[i+1])
    IGTL = vars.get('IGT', x=soln[i+1])
    KSL = vars.get('KS', x=soln[i+1])
    LASL = vars.get('LAS', x=soln[i+1])
    HHL = vars.get('HH', x=soln[i+1])
    HNL = vars.get('HN', x=soln[i+1])
    HWL = vars.get('HW', x=soln[i+1])
    ML = vars.get('M', x=soln[i+1])
    NL = vars.get('N', x=soln[i+1])
    NKIL = vars.get('NKI', x=soln[i+1])
    LNFORL = vars.get('LNFOR', x=soln[i+1])
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
    DY = YL - Y0

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
    #DCMI = CMIL - CMI0

    #DCMO.L(CM)       = CMO.L(CM) - CMO0(CM);
    #DCMO = CMOL - CMO0

    DM = ML - M0

    DV = VL - V0

    DN = NL - N0

    s_name = 'Simulation ' + str(i+1)


    emp = DFFD[DFFD.index.isin(['L1','L2','L3','L4','L5'])].sum().sum()
    dsr = DDS[DDS.index.isin(['HS1','HS2', 'HS3'])].sum()
    dsc = DDS[DDS.index.isin(['CONST1', 'RETAIL1', 'SERV1', 'HC1', 'ACCOM1',
     'REST1', 'AG2', 'CONST2', 'MANUF2', 'RETAIL2', 'SERV2', 'HC2', 'ACCOM2',
     'REST2', 'AG3', 'UTIL', 'CONST3', 'RETAIL3', 'SERV3', 'HC3'])].sum()
    hhinc = DY[DY.index.isin(['HH1','HH2','HH3','HH4','HH5'])].sum()
    hhdiff = HHL-HH0
    mig = hhdiff.sum()

    emplist.append(emp)
    dsrlist.append(dsr)
    dsclist.append(dsc)
    hhinclist.append(hhinc)
    miglist.append(mig)
    simlist.append(s_name)



cols = {'dsc' : dsclist,
        'dsr' : dsrlist,
        'mig' : miglist,
        'emp' : emplist,
        'hhinc' : hhinclist}

#inpath = "C:/Users/lutao_000/Desktop"
df = pd.DataFrame.from_dict(cols)
df.to_csv('Seaside_Sims.csv')



#    worksheet=workbook.add_worksheet(s_name)
#    writer.sheets[s_name] = worksheet
#
#    to_output = [DFFD, DY, CPIL, HHL, DDS, KSL, DN]

#    row = 0
#   for df in to_output:
 #       df.to_excel(writer,sheet_name=s_name,startrow=row , startcol=0)
  #      row = row + len(df.index) + 2


#writer.save()
