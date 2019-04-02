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
printFile(koef)
print("\n")
print("ukupna ligaska potrošnja po igracu : ")
print(GetAVGExpendFORpayer(DFrame))
print("\n")
# print("ukupna ligaska Bruto zarada po igracu :: ")
# print(GetAVGIncomeFORpayer(DFr))
# print("\n")
# print("ukupna ligaska NETTO zarada po igracu :: :")
# print(GetAVGIncomeFORpayer(DF))

#a = GetAVGExpendFORpayer(DFrame)
# b = GetAVGIncomeFORpayer(DFr)
# c = GetAVGIncomeFORpayer(DF)
#np_array = np.stack((a,b,c),axis = -1)

#list_of_labels = ['Liga','Vrijednost bez inflacije ','vriejdnost sa inflacijom']




# jedna od metoda
#np.savetxt(save_csv, a, fmt='%s', delimiter=' ', newline='\n', header='Liga','Vrijednost bez inflacije ','vriejdnost sa inflacijom', footer='')
#np.loadtxt(save_csv,b,fmt='%s', delimiter=' ',newline =' ')
