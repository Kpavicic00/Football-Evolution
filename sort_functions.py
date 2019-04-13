from collections import Counter
from operator import itemgetter
import numpy as np
import pandas as pd
import csv
import sys
from functions import *
from meni_for_functions import *



#functions meni unicate functions
def Chose_reverse_or():
    while True:
        print("\n\t Chose a option of sorting   : ")
        Meni_of_Chose_reverse_or()
        value = input("\n\tValue between 1 or  2  :")
        try:
           value = int(value)
        except ValueError:
           print("\n\tValid options, please !!")
           Meni_of_Chose_reverse_or()
           continue
        if value == 1:
           print(" Sorted by  Classical sort  !!! ")
           a =  False
           return a
           break
        elif value == 2:
           print(" Sorted by Reverse Sort  !!! ")
           a =  True
           return a
           break
        else:
           print("\n\tValue between 1 or  2  !!!") # function ~ 1.
###############################################################################################################################           


###############################################################################################################################
#functions sort
# for clubs Club_statstic for batch GETDataClubs_with_seasons
# take the chose of sort and return the sort of specific collum

def Input_chose_of_sort_CLUBS_GETDataClubs_with_seasons(new_niz):
    while True:
        print("\n\t Chose a option of sorting   : ")
        Meni_of_options_for_sorting_CLUBS_GETDataClubs_with_seasons()
        value = input("\n\tValue between 1 and 13 :")
        try:
           value = int(value)
        except ValueError:
           print("\n\tValid options, please !!")
           Meni_of_options_for_sorting_CLUBS_GETDataClubs_with_seasons()
           continue
        if value == 1:
           print(" Sorted by  Order  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: int(new_niz[0]),reverse = b) #  Order sort ,int
           return a
           break
        elif value == 2:
           print(" Sorted by Club  !!! ")
           b = Chose_reverse_or()
           print("False")
           a =  sorted(new_niz, key=lambda new_niz: str(new_niz[1]),reverse = b) # Club sort ,str
           return a
           break
        elif value == 3:
           print(" Sorted by State  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: str(new_niz[2]),reverse = b) # State sort , str
           return a
           break
        elif value == 4:
           print(" Sorted by Competition  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: str(new_niz[3]),reverse = b) # Competition sort , str
           return a
           break
        elif value == 5:
           print(" Sorted by Expenditures  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[4]),reverse = b) # Expenditures, float
           return a
           break
        elif value == 6:
           print(" Sorted by Arrivals  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: int(new_niz[5]),reverse = b) # Arrivals sort , int
           return a
           break
        elif value == 7:
           print(" Sorted by Income  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[6]),reverse = b) # Income sort , float
           return a
           break
        elif value == 8:
           print(" Sorted by Departures  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: int(new_niz[7]),reverse = b) # Departures sort , int
           return a
           break
        elif value == 9:
           print(" Sorted by Balance !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: int(new_niz[8]),reverse = b) # Balance sort ,int
           return a
        elif value == 10:
           print(" Sorted by Season  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: int(new_niz[9]),reverse = b) # Season sort ,int
           return a
           break
        elif value == 11:
           print(" Sorted by  Inflacion + Income  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[10]),reverse = b) #  Inflacion + Income sort ,float
           return a
        elif value == 12:
           print(" Sorted by  Inflacion + Expenditures  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[11]),reverse = b) #  Inflacion + Expenditures sort ,float
           return a
           break
        elif value == 13:
           print(" Sorted by  Inflacion + Balance  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[12]),reverse = b) #  Inflacion + Balance sort ,float
           return a
        else:
           print("\n\tValue between 1 and 13 !!!") # function ~ 2.
###############################################################################################################################

#functions sort
# for clubs Club_statstic for batch GetDate_for_Clubs_throught_all_seasons
# take the chose of sort and return the sort of specific collum

def Input_chose_of_sort_CLUBS(new_niz):
    while True:
        print("\n\t Chose a option of sorting   : ")
        Meni_of_options_for_sorting()
        value = input("\n\tValue between 1 and 12 :")
        try:
           value = int(value)
        except ValueError:
           print("\n\tValid options, please !!")
           Meni_of_options_for_sorting()
           continue
        if value == 1:
           print(" Sorted by Order of Expend  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: int(new_niz[0])) # Order of Expend sort , int
           return a
           break
        elif value == 2:
           print(" Sorted by Club sort  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: str(new_niz[1])) # Club sort , str
           return a
           break
        elif value == 3:
           print(" Sorted by State sort  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: str(new_niz[2])) # State sort , str
           return a
           break
        elif value == 4:
           print(" Sorted by State sort  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: str(new_niz[3])) # Competition sort , str
           return a
           break
        elif value == 5:
           print(" Sorted by Expenditures  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[4])) # Expenditures sort , float
           return a
           break
        elif value == 6:
           print(" Sorted by Income  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[5])) # Income sort , float
           return a
           break
        elif value == 7:
           print(" Sorted by Arrivals  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: int(new_niz[6])) # Arrivals sort , int
           return a
           break
        elif value == 8:
           print(" Sorted by Departures  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: int(new_niz[7])) # Departures sort , int
           return a
           break
        elif value == 9:
           print(" Sorted by Balance sort !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[8])) # Balance sort ,float
           return a
        elif value == 10:
           print(" Sorted by inflation calculate on Expenditure sort  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[9])) # inflation calculate on Expenditure sort ,float
           return a
           break
        elif value == 11:
           print(" Sorted by inflation calculate on Expenditure sort  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[10])) # inflation calculate on Income sort ,float
           return a
           break
        elif value == 12:
           print(" Sorted by inflation calculate on Balance sort  !!! ")
           b = Chose_reverse_or()
           a =  sorted(new_niz, key=lambda new_niz: float(new_niz[11])) # inflation calculate on Balance sort ,float
           return a
        else:
           print("\n\tValue between 1 and 12 !!!") # function ~ 3.
###############################################################################################################################
