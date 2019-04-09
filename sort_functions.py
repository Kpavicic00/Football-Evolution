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
    return test.sort_values(by=[' Name of  League |  '])
    print("Sort by the Name of League !!") # # function sort ~ 1.

# sort Clubs Data  by Depatrues
def SortDataforCLUBS_Depatrues (DFrame):
    print("Sort by Depatrues !!")
    d = DFrame
    test = GETDataClubs(DFrame)
    return test.sort_values(by=['    Depatrues |  '])
    print("Sort by Depatrues !!") # # function sort ~ 2.

# sort Clubs Data by Arrivals
def SortDataforCLUBS_Arrivals (DFrame):
    print("Sort by Arrivals !!")
    d = DFrame
    test = GETDataClubs(DFrame)
    return test.sort_values(by=['    Arrivals|  '])
    print("Sort by Arrivals !!")# # function sort ~ 3.

# sort Clubs Data by Balance with Inflacion
def SortDataforCLUBS_Balance_with_Inflacion (DFrame):
    print("Sort by Balance + Inflation !!")
    d = DFrame
    test = GETDataClubs(DFrame)
    return test.sort_values(by=['    Balance + Inflation |  '])
    print("Sort by Balance + Inflation !!")# # function sort ~ 4.

# sort Clubs Data by Income with Inflacion
def SortDataforCLUBS_Income_Inflation (DFrame):
    print("Sort by Income + Inflation !!")
    d = DFrame
    test = GETDataClubs(DFrame)
    return test.sort_values(by=['    Income + Inflation |  '])
    print("Sort by Income + Inflation !!")# # function sort ~ 5.

# sort Clubs Data by Expend with Inflacion
def SortDataforCLUBS_Expend_Inflation (DFrame):
    print("Sort by Expend + Inflation !!")
    d = DFrame
    test = GETDataClubs(DFrame)
    return test.sort_values(by=['    Expend + Inflation |  '])
    print("Sort by Expend + Inflation !!")# # function sort ~ 6.

# sort Clubs Data by year of Season
def SortDataforCLUBS_year_of_Season (DFrame):
    print("Sort by year of Season !!")
    d = DFrame
    test = GETDataClubs(DFrame)
    return test.sort_values(by=['    year of Season |  '])
    print("Sort by year of Season!!")# # function sort ~ 7.
