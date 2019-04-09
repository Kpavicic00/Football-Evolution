from collections import Counter
from operator import itemgetter
import numpy as np
import pandas as pd
import csv
import sys
from functions import *


# sort Clubs Data for Arrivals by Name of leuge
def SortDataforCLUBS_by_Name_of_leuge (DFrame):
    print("Sort by the Name of League !!")
    d = DFrame
    test = GETDataClubs(DFrame)
    return test.sort_values(by=[' Name of  League |  '])# # function ~ 16.

# sort Clubs Data  by Depatrues
def SortDataforCLUBS_Depatrues (DFrame):
    print("Sort by Depatrues !!")
    d = DFrame
    test = GETDataClubs(DFrame)
    return test.sort_values(by=['    Depatrues |  '])# # function ~ 17.

# sort Clubs Data by Arrivals
def SortDataforCLUBS_Arrivals (DFrame):
    print("Sort by Arrivals !!")
    d = DFrame
    test = GETDataClubs(DFrame)
    return test.sort_values(by=['    Arrivals|  '])# # function ~ 17.
