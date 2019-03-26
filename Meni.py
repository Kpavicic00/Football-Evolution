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
data_csv = "datas.csv"
koef = "/home/kristijan/github/FootballEvolcion/file.txt"
data = "/home/kristijan/github/FootballEvolcion/datas.txt"

# print("\n\t Ispis koeficeijanata : ")
# printFile(koef)
#
# print("\n\t Ispis podataka : ")
# printFile(data)

dat = "/home/kristijan/github/FootballEvolcion/datas.csv"

# data = pd.read_csv('/home/kristijan/github/FootballEvolcion/datas.csv', delimiter = ','
# ,names = ['poredak\t','Naziv lige','potrošeno','dolso ugraca','doslo igraca','otislo igraca'])
# print(data)
data = pd.read_csv(dat, names=['poredak', 'b', 'c','d','e','g','g'])
print(data)
shap = data.shape
print(shap)
data.loc['1':'2',['b','c','d']]
