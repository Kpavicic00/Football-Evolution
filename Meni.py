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
podaci = "/home/kristijan/github/FootballEvolcion/TEST_CSV.csv"
koef = "/home/kristijan/github/FootballEvolcion/file.txt"
data = "/home/kristijan/github/FootballEvolcion/datas.txt"
podaci = "/home/kristijan/github/FootballEvolcion/podaci.txt"

# print(df1.index.tolist()) #print index


dat = pd.read_csv(podaci)
print(dat)
