# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
import sys
from pandas import ExcelWriter
from pandas import ExcelFile
from functions import *
from sort_functions import*
import sys




# txt FILES
fp_clubs = '/home/kristijan/github/FootballEvolcion/Datas/Club_statstic.csv'
fp = '/home/kristijan/github/FootballEvolcion/Datas/testni_podaci.csv'
filePath ='/home/kristijan/github/FootballEvolcion/Datas/TEST_CSV.csv'
koef = "/home/kristijan/github/FootballEvolcion/Datas/file.txt"
data = "/home/kristijan/github/FootballEvolcion/Datas/datas.txt"
podaci = "/home/kristijan/github/FootballEvolcion/Datas/podaci.txt"
save_csv_a = '/home/kristijan/github/FootballEvolcion/Datas/Save_csv_Parsing_a.csv'
save_csv_b = '/home/kristijan/github/FootballEvolcion/Datas/Save_csv_Parsing_b.csv'
save_csv_c = '/home/kristijan/github/FootballEvolcion/Datas/Save_csv_Parsing_c.csv'




print("Test podaci liga za sezone 2018 i 2011 : ")
datFrame = DataFrameFunc(fp)
dt_clubs = DataFrameFuncClubs(fp_clubs)
#print(fp)
# print("GetAVGExpendFORpayerArrivals ")
# GetAVGExpendFORpayerArrivals(datFrame)
#
# print("GetAVGIncomeFORpayerDepartures ")
# GetAVGIncomeFORpayerDepartures(datFrame)
#
# print("GetAVGBalanceFORpayerDepartures ")
# GetAVGBalanceFORpayerDepartures(datFrame)
#
# print("\n\n")
# print("GetBYyear : ")
# GetBYyear(datFrame)
#
# print("SortDataforYEAR_by_avg_Income_Season : ")
# SortDataforYEAR_by_avg_Income_Season(datFrame)

print("GETDataClubs : ")
GETDataClubs(dt_clubs)
GetDate_for_Clubs_throught_all_seasons
print("GetDate_for_Clubs_throught_all_seasons : ")
GetDate_for_Clubs_throught_all_seasons(dt_clubs)


#DataF = DataFrameFuncClubs(fp_clubs)
## print datas and functions colls
# print("Podaci:  : ")
# print(DFrame)
# print("\n")
# print("koeficijenti : ")
# printFile(koef)
# print("\n")
#print("DataF CLubs")
#print(DataF)
# print("test 1 ")
# print("GetAVGExpendFORpayerArrivals(DFrame)")
# print(GetAVGExpendFORpayerArrivals(DFrame))
# print("test 1  radiiiiiii")
# print("###########################################")
# print("test 2 ")
# print("GetAVGIncomeFORpayerDepartures(DFrame)")
# print(GetAVGIncomeFORpayerDepartures(DFrame))
# print("test 2  radiiiiiii")
# print("###########################################")
# print("test 3 ")
# print("GetAVGBalanceFORpayerDepartures(DFrame)")
# print(GetAVGBalanceFORpayerDepartures(DFrame))
# print("test 3  radiiiiiii")
# print("###########################################")
# print("test 4 ")
# print("GetDataForLeauge_AVG_Seasons(DFrame)")
# print(GetDataForLeauge_AVG_Seasons(DFrame))
# print("test 4  radiiiiiii")
# #a = DataFrameFuncClubs(fp_clubs)
#
# # print(a)
# # print("test 1: ")
# # print(GETDataClubs(a))
# # print(GetAVGIncinterception[i] = (Expenditures[i]*koef[i])omeFORpayerDepartures(DFrame))
# # print(GetDataForLeauge_AVG_Seasons(DFrame))
# # print("test 2: ")
# #print(GetBYyear(DFrame))
# #print(GetInflationBYclubs(DataF))
# #test
# #print(GetDataForLeauge_AVG_Seasons(DFrame))
#
#
# #print("ukupna ligaska potrošnja po igracu : ")
# #print(GetAVGExpendFORpayerArrivals(DFrame))
# # print("\n")
# # print("ukupna ligaska Bruto zarada po igracu :: ")
# # print(GetAVGIncomeFORpayerDepartures(DFrame))
# # print("\n")
# # print("ukupna ligaska NETTO zarada po igracu :: :")
# # print(GetAVGBalanceFORpayerDepartures(DFrame))
# #
# a = GetAVGExpendFORpayerArrivals(DFrame)
# b = GetAVGIncomeFORpayerDepartures(DFrame)
# c = GetAVGBalanceFORpayerDepartures(DFrame)
# #
# #
# #
# # # Write to file
# head = 'Name_of_leauge Season Nationality AvgExpend +INFLACION'
# WriteTOcsvFILE(save_csv_a,a,head)
# print("Write into   file !!!")
# WriteTOcsvFILE(save_csv_b,b,head)
# WriteTOcsvFILE(save_csv_c,c,head)

# DFrame = DataFrameFunc(fp)
# DFrame_Clubs = DataFrameFuncClubs(fp_clubs)
# print("###################################################")
# # DFrame_Clubs = DataFrameFuncClubs(fp_clubs)
# # a = SortDataforCLUBS_by_Name_of_leuge(DFrame_Clubs)
# # print(a)
# print(GetBYyear(DFrame))
#
# print("###################################################")
