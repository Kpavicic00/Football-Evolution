# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
import sys
from pandas import ExcelWriter
from pandas import ExcelFile
from functions import *
import sys




# txt FILES
filePath ='/home/kristijan/github/FootballEvolcion/TEST_CSV.csv'
koef = "/home/kristijan/github/FootballEvolcion/file.txt"
data = "/home/kristijan/github/FootballEvolcion/datas.txt"
podaci = "/home/kristijan/github/FootballEvolcion/podaci.txt"
save_csv = '/home/kristijan/github/FootballEvolcion/Save_csv_Parsing.csv'

# print(df1.index.tolist()) #print index




#t = Coefficients(koef)

DFrame = DataFrameFunc(filePath)
DF = DataFrameFunc(filePath)
DFr = DataFrameFunc(filePath)
print(DFrame)
print("\n")
print("ukupna ligaska potrošnja po igracu : ")
print(GetAVGExpendFORpayer(DFrame))
print("\n")
print("ukupna ligaska Bruto zarada po igracu :: ")
print(GetAVGIncomeFORpayer(DFr))
print("\n")
print("ukupna ligaska NETTO zarada po igracu :: ")
print(GetAVGIncomeFORpayer(DF))

# a = GetAVGExpendFORpayer(DFrame)
# b = GetAVGIncomeFORpayer(DFr)
# c = GetAVGIncomeFORpayer(DF)

#np.savetxt(save_csv, a, delimiter=",")
#a.tofile(save_csv,sep=',',format='%10.5f')
#np.savetxt(save_csv, a, fmt='%.18e,%.18e,%.18e ')
# numpy.savetxt(save_csv, b, delimiter=",")
# numpy.savetxt(save_csv, c, delimiter=",")
