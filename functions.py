import numpy as np
import pandas as pd
import csv
import sys

koef = "/home/kristijan/github/FootballEvolcion/file.txt"
# functions

#function count number of rows for specific DateFrame
def NumberOfRows(datFrame):
    total_rows = len(datFrame)
    #print("Total rows : ", total_rows )
    return  total_rows

# functions_fore choose of season
def Input_season():
    while True:
        print("\n\t Enter a year of season   : ")
        value = input("\n\tValue between 2000 and 2018 :")
        try:
           value = int(value)
        except ValueError:
           print("\n\tValid number, please !!")
           continue
        if 2000 <= value <= 2018:
           return value
           break
        else:
           print("\n\tValue between 2000 and 2018 !!!")

# function for input years interval 2000 to 2018
def Input_year():
    while True:
        print("\n\t Enter a year of transaction to get \ n transaction data according to the current inflation rate : ")
        value = input("\n\tValue between 2000 and 2018 :")
        try:
           value = int(value)
        except ValueError:
           print("\n\tValid number, please !!")
           continue
        if 2000 <= value <= 2018:
           return value
           break
        else:
           print("\n\tValue between 2000 and 2018 !!!")

# print the txt file
def printFile(data):
    #read the file
    f = open(data, "r")
    print(f.read())
    f.close()

# function  count the length of lines for the required size allocation of the string
def file_lengthy(fname):
    with open(fname) as f:
        for i ,j in enumerate (f):
            pass
        return i +1

#function get Coefients for specific year
def GETCoefficients(files,year):
    lenght = file_lengthy(files) # count the length of lines for the required size allocation of the string

    with open(files, "r") as f: # open the file
        data = f.readlines()

    count = 0 # counter for arrays

    #reserving the number of elements in a row
    y = [0] * lenght
    k = [0] * lenght

    for line in data:
        words = line.split()

        y[count] = words[0] # years
        k[count] = words[1] # coefficient
        count += 1

    # conversion to numpy
    np_years = np.asarray(y, dtype='int64')
    np_koef = np.asarray(k, dtype='float64')

    # the intake part put a try catch between the 2000 and 2009 intervals and to index them with the 2019 index

    np_specific_coefficient = np_koef[np_years == year]
    #print("\n\t You have chosen a year :  ",i)

    return np_specific_coefficient

# uzmanje i baratanje sa podacima u smislu koeficjenta
def Coefficients(files):
    lenght = file_lengthy(files) # count the length of lines for the required size allocation of the string

    with open(files, "r") as f: # open the file
        data = f.readlines()

    count = 0 # counter for arrays

    #reserving the number of elements in a row
    y = [0] * lenght
    k = [0] * lenght

    for line in data:
        words = line.split()

        y[count] = words[0] # years
        k[count] = words[1] # coefficient
        count += 1

    # conversion to numpy
    np_years = np.asarray(y, dtype='int64')
    np_koef = np.asarray(k, dtype='float64')

    # the intake part put a try catch between the 2000 and 2009 intervals and to index them with the 2019 index
    i = Input_year()
    np_specific_coefficient = np_koef[np_years == i]
    #print("\n\t You have chosen a year :  ",i)
    return np_specific_coefficient

# takes data with pandas function DataFrame
def DataFrameFunc(filePath):
    colls = ["0","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]
    dat = pd.read_csv(filePath,header = None , names = colls)
    return dat

#get average League spending for each player
def GetAVGExpendFORpayer(DFrame):
    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Expend = [0] * count
    Arrival = [0] * count
    leauge = [0] * count
    CUT =  [0] * count



    # cast DataFrame rows to folat and int
    DFrame["Expenditures"].astype(np.float64)
    DFrame["Arrivals"].astype(np.int64)
    DFrame["Competition"].astype(np.str)
    DFrame["Season"].astype(np.int64)

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Expend[i] = DFrame["Expenditures"][i]
        Arrival[i] = DFrame["Arrivals"][i]
        leauge[i] = DFrame["Competition"][i]

    # conversion to numpy
    np_Expend = np.asarray(Expend, dtype='float64')
    np_Arrival = np.asarray(Arrival, dtype='int64')
    npLeauge = np.asarray(leauge, dtype='str')
    np_CUT = np.asarray(CUT, dtype='float64')

    if DFrame["Season"][1] == 2000:
        print(DFrame["Season"][1])
        print(type(DFrame["Season"][1]))

    k = DFrame["Season"][1]
    mult = GETCoefficients(koef,k)
    print("mult : ",mult)
    np_CUT = np_Expend/np_Arrival

    np_CUT_inflation = np_CUT*mult

    return np.stack((npLeauge,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)

#get average League brutto earnings for each player
def GetAVGIncomeFORpayer(Dframe):
    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Expend = [0] * count
    Arrival = [0] * count
    leauge = [0] * count
    CUT =  [0] * count

    # cast DataFrame rows to folat and int
    DFrame["Income"].astype(np.float64)
    DFrame["Arrivals"].astype(np.int64)
    DFrame["Competition"].astype(np.str)

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Expend[i] = DFrame["Income"][i]
        Arrival[i] = DFrame["Arrivals"][i]
        leauge[i] = DFrame["Competition"][i]

    # conversion to numpy
    np_Expend = np.asarray(Expend, dtype='float64')
    np_Arrival = np.asarray(Arrival, dtype='int64')
    npLeauge = np.asarray(leauge, dtype='str')
    np_CUT = np.asarray(CUT, dtype='float64')

    if DFrame["Season"][1] == 2000:
        print(DFrame["Season"][1])
        print(type(DFrame["Season"][1]))

    k = DFrame["Season"][1]
    mult = GETCoefficients(koef,k)
    print("mult : ",mult)
    np_CUT = np_Expend/np_Arrival

    np_CUT_inflation = np_CUT*mult

    return np.stack((npLeauge,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)


#get average League netto earnings for each player
def GetAVGBalanceFORpayer(Dframe):
    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Expend = [0] * count
    Arrival = [0] * count
    leauge = [0] * count
    CUT =  [0] * count

    # cast DataFrame rows to folat and int
    DFrame["Balance"].astype(np.float64)
    DFrame["Departures"].astype(np.int64)
    DFrame["Competition"].astype(np.str)

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Expend[i] = DFrame["Balance"][i]
        Arrival[i] = DFrame["Arrivals"][i]
        leauge[i] = DFrame["Competition"][i]

    # conversion to numpy
    np_Expend = np.asarray(Expend, dtype='float64')
    np_Arrival = np.asarray(Arrival, dtype='int64')
    npLeauge = np.asarray(leauge, dtype='str')
    np_CUT = np.asarray(CUT, dtype='float64')

    if DFrame["Season"][1] == 2000:
        print(DFrame["Season"][1])
        print(type(DFrame["Season"][1]))

    k = DFrame["Season"][1]
    mult = GETCoefficients(koef,k)
    print("mult : ",mult)
    np_CUT = np_Expend/np_Arrival

    np_CUT_inflation = np_CUT*mult

    return np.stack((npLeauge,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)


    return
