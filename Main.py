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
fp = '/home/kristijan/github/FootballEvolcion/Datas/testni_podaci.csv'
filePath ='/home/kristijan/github/FootballEvolcion/Datas/TEST_CSV.csv'
koef = "/home/kristijan/github/FootballEvolcion/Datas/file.txt"
data = "/home/kristijan/github/FootballEvolcion/Datas/datas.txt"
podaci = "/home/kristijan/github/FootballEvolcion/Datas/podaci.txt"
save_csv_a = '/home/kristijan/github/FootballEvolcion/Datas/Save_csv_Parsing_a.csv'
save_csv_b = '/home/kristijan/github/FootballEvolcion/Datas/Save_csv_Parsing_b.csv'
save_csv_c = '/home/kristijan/github/FootballEvolcion/Datas/Save_csv_Parsing_c.csv'
