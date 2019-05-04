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
BATCH_for_GetAVGExpendFORplayerArrivals(clubs_DF)
Delite_DataFrame_from_memory(clubs_DF)
