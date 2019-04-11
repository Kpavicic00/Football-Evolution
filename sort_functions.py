from collections import Counter
from operator import itemgetter
import numpy as np
import pandas as pd
import csv
import sys
from functions import *

#functions sort
# for clubs Club_statstic

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


#functions sort
# for clubs Championship and leagues by YEARRRRR

# sort YEARS data for all leauges by Expend
def SortDataforYEAR_by_EXPEND (DFrame):
    print("Sort YEARS data for all leauges by Expend !!")
    d = DFrame
    test = GetBYyear(DFrame)
    return test.sort_values(by=['    Expend |  '])
    print("Sort YEARS data for all leauges by Expend!!")# # function sort ~ 8.

# sort YEARS data for all leauges by Income
def SortDataforYEAR_by_INCOME (DFrame):
    print("Sort YEARS data for all leauges by Income !!")
    d = DFrame
    test = GetBYyear(DFrame)
    return test.sort_values(by=['    Income |  '])
    print("Sort YEARS data for all leauges by Income!!")# # function sort ~ 9.

# sort YEARS data for all leauges by number  of Arrivlas
def SortDataforYEAR_by_Arrivlas (DFrame):
    print("Sort YEARS data for all leauges by Arrivlas !!")
    d = DFrame
    test = GetBYyear(DFrame)
    return test.sort_values(by=['    sum of Arrivlas |  '])
    print("Sort YEARS data for all leauges by Arrivlas!!")# # function sort ~ 10.

# sort YEARS data for all leauges by number  of Depatrues
def SortDataforYEAR_by_Depatrues (DFrame):
    print("Sort YEARS data for all leauges by Depatrues !!")
    d = DFrame
    test = GetBYyear(DFrame)
    return test.sort_values(by=['    sum of Depatrues |  ',])
    print("Sort YEARS data for all leauges by Depatrues!!")# # function sort ~ 10.

# sort YEARS data for all leauges by number  of avg Expend/Season
def SortDataforYEAR_by_avg_Expend_Season (DFrame):
    print("Sort YEARS data for all leauges avg Expend/Season !!")
    d = DFrame
    test = GetBYyear(d)
    return test.sort_values(by=['    avg Expend/Season |  '])
    print("Sort YEARS data for all leauges avg Expend/Season!!")# # function sort ~ 12.

# sort YEARS data for all leauges by number  by  avg Income/Season
def SortDataforYEAR_by_avg_Income_Season (DFrame):
    print("Sort YEARS data for all leauges by  avg Income/Seasons !!")
    d = DFrame
    test = GetBYyear(d)
    return test.sort_values(by=['    avg Income/Season |  '],ascending=True)
    print("Sort YEARS data for all leauges by  avg Income/Season!!")# # function sort ~ 13.

#functions sort
# for GETDataClubs  Leauge statsitic by LEAUGES

# sort YEARS data for all leauges by number  by  ExpendFORpayerArrivals
def SortDataforLEAUGES_byExpendFORpayerArrivals (DFrame):
    print("Sort YEARS data for all leauges by   Expend + Inflation by player !! XXXX")
    d = DFrame
    test = GetAVGExpendFORpayerArrivals(d)
    #a = test.sort_values(test.columns[4])
    #a = sorted(test,key=lambda test: float(test[3]))
    #test = np.asarray(test[3], dtype=np.float64, order='C')

    return test
    print("Sort YEARS data for all leauges by    Expend + Inflation by player !!")# # function sort ~ 14.

# sort YEARS data for all leauges by number  by  IncomeFORpayerDeparture
def SortDataforLEAUGES_IncomeFORpayerDeparture (DFrame):
    print("Sort YEARS data for all leauges by  Income + Inflation by player  !!")
    d = DFrame
    test = GetAVGIncomeFORpayerDepartures(DFrame)
    return test.sort_values(by=['  Income + Inflation by player|  '])
    print("Sort YEARS data for all leauges by  Income + Inflation by player !!")# # function sort ~ 15.

# sort YEARS data for all leauges by number  by  BalanceFORpayerDepartures
def SortDataforLEAUGES_BalanceFORpayerDepartures (DFrame):
    print("Sort YEARS data for all leauges by  Income + Balance + Inflation by player  !!")
    d = DFrame
    test = GetAVGBalanceFORpayerDepartures(d)
    return test.sort_values(by=['  Balance + Inflation by player|  '])
    print("Sort YEARS data for all leauges by  Balance + Inflation by player !!")# # function sort ~ 16.
