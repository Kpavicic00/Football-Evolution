# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
import sys
from pandas import ExcelWriter
from pandas import ExcelFile
from collections import Counter
from operator import itemgetter
from functions import *
from sort_functions import*






# csv , txt files for datas
clubs_KONACNA = '/home/kristijan/github/FootballEvolcion/Datas/sportska_kubska_statsitika_OBRDENO.csv' # ovaj za klubsku statistiku
fp_league = '/home/kristijan/github/FootballEvolcion/Datas/Ligaska_KONACAN_STAS.csv'# ovaj za ligasku statistiku
test = '/home/kristijan/github/FootballEvolcion/Datas/testni_podaci.csv'

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

clubs_DF = DataFrameFunc(fp_league)
BATCH_for_GetAVGExpendFORplayerArrivals(clubs_DF)
Delite_DataFrame_from_memory(clubs_DF)
