# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
import sys
from files_lib import *
from pandas import ExcelWriter
from pandas import ExcelFile
from collections import Counter
from operator import itemgetter
from functions import *
from sort_functions import*





clubs_DF = DataFrameFunc(fp_league)
a_batch = BATCH_for_GetAVGExpendFORplayerArrivals(clubs_DF)
a_batchE = BATCH_for_GetAVGIncomeFORplayerDepartures(clubs_DF)

WriteTOcsvFILE_mult_DATAFRAMES(save_csv_Expend,a_batch)
WriteTOcsvFILE_mult_DATAFRAMES(save_csv_Expend,a_batchE)

Delite_DataFrame_from_memory(clubs_DF)
Delite_DataFrame_from_memory(a_batch)
Delite_DataFrame_from_memory(a_batchE)
