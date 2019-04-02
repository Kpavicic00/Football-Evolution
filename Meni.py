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



DFrame = DataFrameFunc(filePath)

## print datas and functions colls
print("Podaci:  : ")
print(DFrame)
print("\n")
print("koeficijenti : ")
printFile(koef)
print("\n")
print("ukupna ligaska potrošnja po igracu : ")
print(GetAVGExpendFORpayerArrivals(DFrame))
print("\n")
print("ukupna ligaska Bruto zarada po igracu :: ")
print(GetAVGIncomeFORpayerDepartures(DFrame))
print("\n")
print("ukupna ligaska NETTO zarada po igracu :: :")
print(GetAVGBalanceFORpayerDepartures(DFrame))

a = GetAVGBalanceFORpayerDepartures(DFrame)
b = GetAVGBalanceFORpayerDepartures(DFrame)
c = GetAVGBalanceFORpayerDepartures(DFrame)





# jedna od metoda
np.savetxt(save_csv, a, fmt='%s', delimiter=' ', newline='\n', header='', footer='')
