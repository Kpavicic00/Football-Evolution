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




# csv , txt files for datas
fail_pathclubs = '/home/kristijan/github/FootballEvolcion/Datas/test_podaci_klubovi.csv'
fp_clubs = '/home/kristijan/github/FootballEvolcion/Datas/Club_statstic.csv'
fp_league = '/home/kristijan/github/FootballEvolcion/Datas/testni_podaci.csv'
filePath ='/home/kristijan/github/FootballEvolcion/Datas/TEST_CSV.csv'
koef = "/home/kristijan/github/FootballEvolcion/Datas/file.txt"
data = "/home/kristijan/github/FootballEvolcion/Datas/datas.txt"
podaci = "/home/kristijan/github/FootballEvolcion/Datas/podaci.txt"

# csv file for save of processed data
save_csv_a = '/home/kristijan/github/FootballEvolcion/Datas/SaveData/Save_csv_Parsing_a.csv'
save_csv_b = '/home/kristijan/github/FootballEvolcion/Datas/SaveData/Save_csv_Parsing_b.csv'
save_csv_c = '/home/kristijan/github/FootballEvolcion/Datas/SaveData/Save_csv_Parsing_c.csv'
save_csv_d = '/home/kristijan/github/FootballEvolcion/Datas/SaveData/Save_csv_Parsing_d.csv'
save_csv_e = '/home/kristijan/github/FootballEvolcion/Datas/SaveData/Save_csv_Parsing_e.csv'
save_csv_f = '/home/kristijan/github/FootballEvolcion/Datas/SaveData/Save_csv_Parsing_f.csv'
save_csv_g = '/home/kristijan/github/FootballEvolcion/Datas/SaveData/Save_csv_Parsing_g.csv'
save_csv_h = '/home/kristijan/github/FootballEvolcion/Datas/SaveData/Save_csv_Parsing_h.csv'

dt_lg = DataFrameFunc(fp_league)
a = BATCH_for_GetAVGExpendFORplayerArrivals(dt_lg)
b = BATCH_for_GetAVGIncomeFORplayerDepartures(dt_lg)

pars = [a,b]
with open(save_csv_a, 'w') as f:
     pd.concat([a, b], axis=0).to_csv(f)

# pd.concat([
#     pd.concat([a], axis=1),
#     pd.concat([b], axis=0)]).to_csv(save_csv_a)
# pd.DataFrame([a],[b]).to_csv(save_csv_b, index=True ,delimiter=',', newline='/n',header="/n")
#pd.DataFrame([b]).to_csv(save_csv_b, index=True ,delimiter=',',header="/n")
#pd.concat([pd.concat([a], axis=1),pd.concat([b], axis=0 )]).to_csv(save_csv_a)
#df.to_csv(save_csv_a, index=False, header=False, mode='a')
# with open(save_csv_a, 'w') as f:
#      pd.concat([a], axis=1).to_csv(f)
# with open(save_csv_a, 'a') as f:
#      pd.concat([a], axis=1).to_csv(f, header=False)
#ReadCSV_file(save_csv_b)
#pd.concat([pars], axis=1).to_csv(save_csv_a)

# dt_Clubs = DataFrameFuncClubs(fail_pathclubs)
#
# BATCH_for_GetDate_for_Clubs_throught_all_seasons(dt_Clubs)
