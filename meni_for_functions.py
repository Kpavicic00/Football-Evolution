from collections import Counter
from operator import itemgetter
import numpy as np
import pandas as pd
import csv
import sys
from functions import *


# meni of options for sort for function Input_chose_of_sort
def Meni_of_options_for_sorting_CLUBS_GETDataClubs_with_seasons():
    print("======> Sort for Clubs with year of seasons   <======")
    print(" 1 =>  Sort data BY Order") # 0
    print(" 2 =>  Sort data BY Club") # 1
    print(" 3 =>  Sort data BY State") # 2
    print(" 4 =>  Sort data BY Competition") # 3
    print(" 5 =>  Sort data BY Expenditures") # 4
    print(" 6 =>  Sort data BY Arrivals") # 5
    print(" 7 =>  Sort data BY Income") # 6
    print(" 8 =>  Sort data BY Departures") # 7
    print(" 9 =>  Sort data BY Balance") # 8
    print(" 10 =>  Sort data BY Season") # 9
    print(" 11 =>  Sort data BY Inflacion + Income") # 11
    print(" 12 =>  Sort data BY Inflacion + Expenditures") # 12
    print(" 13 =>  Sort data BY Inflacion + Balance") # 13 ,
    print("======> Sort for Clubs with year of seasons   <======")  # function ~ 1.
########################################################################################################################################################################################################

# meni of options for sort for function Input_chose_of_sort
def Meni_of_options_for_sorting():
    print("======> Sort  for Clubs throught all seasons   <======")
    print(" 1 =>  Sort data BY Order of Expend") # 0
    print(" 2 =>  Sort data BY Club") # 1
    print(" 3 =>  Sort data BY State") # 2
    print(" 4 =>  Sort data BY Competition") # 3
    print(" 5 =>  Sort data BY Expenditures") # 4
    print(" 6 =>  Sort data BY Income") # 5
    print(" 7 =>  Sort data BY Arrivals") # 6
    print(" 8 =>  Sort data BY Departures") # 7
    print(" 9 =>  Sort data BY Balance") # 8
    print(" 10 =>  Sort data BY inflation calculate on Expenditure") # 9
    print(" 11 =>  Sort data BY inflation calculate on Income") # 10
    print(" 12 =>  Sort data BY inflation calculate on Balance") # 11
    print("======> Sort  for Clubs throught all seasons   <======")  # function ~ 2.
########################################################################################################################################################################################################

# meni for Chose_reverse_or functions
def Meni_of_Chose_reverse_or():
    print("======> Options for sorting   <======")
    print(" 1 =>  Sort data BY Clasic sort  ")
    print(" 2 =>  Sort data BY Reverse sort ")
    print("======> Options for sorting   <======")  # function ~ 2.
########################################################################################################################################################################################################

# meni for GetBYyea
def Meni_of_GetBYyear():
    print("======> Sort  for LAUGES by year   <======")
    print(" 1 =>  Sort data BY Year") # 0
    print(" 2 =>  Sort data BY Expend") # 1
    print(" 3 =>  Sort data BY Income") # 2
    print(" 4 =>  Sort data BY Balance") # 3
    print(" 5 =>  Sort data BY number of Season") # 4
    print(" 6 =>  Sort data BY sum of Arrivlas") # 5
    print(" 7 =>  Sort data BY sum of Depatrues") # 6
    print(" 8 =>  Sort data BY avg Expend of Arrivlas") # 7
    print(" 9 =>  Sort data BY avg Income of Depatrues ") # 8
    print(" 10 =>  Sort data BY  avg Balance of Depatrues ") # 9
    print(" 11 =>  Sort data BY avg Expend/Season ") # 10
    print(" 12 =>  Sort data BY avg Income/Season") # 11
    print(" 12 =>  Sort data BY avg Balance/Season") # 12
    print("======>Sort  for LAUGES by year   <======")  # function ~ 4.
########################################################################################################################################################################################################

# meni for GetDataForLeauge_AVG_Seasons
def Meni_of_GetDataForLeauge_AVG_Seasons():
    print(" 1 =>  Sort data BY Name of leauge") # 1
    print(" 2 =>  Sort data BY Expend") # 1
    print(" 3 =>  Sort data BY Income") # 2
    print(" 4 =>  Sort data BY Balance") # 3
    print(" 5 =>  Sort data BY number of Season") # 4
    print(" 6 =>  Sort data BY sum of Arrivlas") # 5
    print(" 7 =>  Sort data BY sum of Depatrues") # 6
    print(" 8 =>  Sort data BY avg Expend of Arrivlas") # 7
    print(" 9 =>  Sort data BY avg Income of Depatrues ") # 8
    print(" 10 =>  Sort data BY  avg Balance of Depatrues ") # 9
    print(" 11 =>  Sort data BY avg Expend/Season ") # 10
    print(" 12=>  Sort data BY avg Income/Season") # 11
    print(" 13 =>  Sort data BY avg Balance/Season") # 12
    print("======>Sort  for LAUGES by year   <======")  # function ~ 4.
########################################################################################################################################################################################################
