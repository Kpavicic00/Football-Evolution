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
data_csv = "income_data.csv"
koef = "/home/kristijan/github/FootballEvolcion/file.txt"
data = "/home/kristijan/github/FootballEvolcion/datas.txt"

# print(df1.index.tolist()) #print index


data = pd.read_csv(data_csv)
#print(data)

#t = df2.loc["Alaska":"Arkansas","2005":"2007"]
print("\n\t test : ")

print(data.head())
# Type_new = pd.Series([])
# data.insert(2, "Type New", Type_new) ### umetanje novih stupaca colums
usp = "Sta"
test = "jebemu"
i =1
t = input("Unesi : ")
if i == t:
    data [usp][0] = test
    print("Ipsis : ")
    print(data.head())


#print(data.head())

#print(data.head())
# t = input("pocija 1 : ")
# t = int(t)
# a =1
# if a == t:
#     b= "jebemu"
#     b = str(b)
#     if data.loc["Type New",0]  == b:
#         print(" Ispis : ",data.loc["Type New",0])

# df['proxyCity'].ix[myindex ] = new_name
# to
#
# df.loc[myindex, 'proxyCity'] = new_name
#unos = input("\n\t Unesit etesnu rijec : ")


#data["Type New"][1] = unos
# for i in range(len(data)):
#     if data["Type New"][i] == "NaN":
#         Type_new[i]="Green"
#
#     elif data["Type New"][i] == "NaN":
#         Type_new[i]="Orange"
#
#     elif data["Type New"][i] == "NaNr":
#         Type_new[i]="Blue"
#
#     else:
#         Type_new[i]= data["Type New"][i]
