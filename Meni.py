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

# print(df1.index.tolist()) #print index




t = Coefficients(koef)
dat = DataFrameFunc(filePath)
a = dat["Expenditures"][1]
print("Ispis ",a,t)


p = a*t# TEMP:
rez = float(p)

print(" Izracun :::  : ",rez)
