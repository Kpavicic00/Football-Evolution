from collections import Counter
from operator import itemgetter
import numpy as np
import pandas as pd
import csv
import sys

coef = "/home/kristijan/github/FootballEvolcion/Datas/file.txt"
# functions

# write to file
def WriteTOcsvFILE(csv_file,dat,head):
    np.savetxt(csv_file, dat, fmt='%s', delimiter=' ', newline='\n', header=head, footer='     => End of file <=')

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

# picking up and dealing with the data in terms of coefficients
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
    colls = ["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]
    dat = pd.read_csv(filePath,header = None , names = colls)
    return dat

#get average League spending for each player
def GetAVGExpendFORpayerArrivals(DFrame):

    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Nationality = [0] * count
    Expend = [0] * count
    Arrival = [0] * count
    leauge = [0] * count
    Season = [0] * count
    koef = [0] * count
    CUT =  [0] * count
    interception = [0] * count

    # cast DataFrame rows to folat and int
    DFrame["Expenditures"].astype(np.float64)
    DFrame["Arrivals"].astype(np.int64)
    DFrame["Competition"].astype(np.str)
    DFrame["Nationality"].astype(np.str)
    DFrame["Season"].astype(np.int64)

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Expend[i] = DFrame["Expenditures"][i]
        Arrival[i] = DFrame["Arrivals"][i]
        leauge[i] = DFrame["Competition"][i]
        Season[i] = DFrame["Season"][i]
        Nationality[i] = DFrame["Nationality"][i]

    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a

    for i in range(0,count):
        interception[i] = round((Expend[i]*koef[i]),2)

    # conversion to numpy
    np_Expend = np.asarray(Expend, dtype='float64')
    np_Arrival = np.asarray(Arrival, dtype='int64')
    np_Season = np.asarray(Season, dtype='int64')
    npNationality = np.asarray(Nationality, dtype='str')
    npLeauge = np.asarray(leauge, dtype='str')
    np_CUT = np.asarray(CUT, dtype='float64')
    np_Interception = np.asarray(interception, dtype='float64')

    np_CUT = np_Expend/np_Arrival
    np_CUT_inflation = np_Interception/np_Arrival

    return np.stack((npLeauge,np_Season,npNationality,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)

#get average League brutto earnings for each player
def GetAVGIncomeFORpayerDepartures(DFrame):

    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Nationality = [0] * count
    Income = [0] * count
    Departures = [0] * count
    leauge = [0] * count
    Season = [0] * count
    koef = [0] * count
    CUT =  [0] * count
    interception = [0] * count

    # cast DataFrame rows to folat and int
    DFrame["Income"].astype(np.float64)
    DFrame["Departures"].astype(np.int64)
    DFrame["Nationality"].astype(np.str)
    DFrame["Competition"].astype(np.str)
    DFrame["Season"].astype(np.int64)

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Income[i] = DFrame["Income"][i]
        Departures[i] = DFrame["Departures"][i]
        leauge[i] = DFrame["Competition"][i]
        Season[i] = DFrame["Season"][i]
        Nationality[i] = DFrame["Nationality"][i]

    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a

    for i in range(0,count):
        interception[i] = round((Income[i]*koef[i]),2)

    # conversion to numpy
    np_Income = np.asarray(Income, dtype='float64')
    np_Departures = np.asarray(Departures, dtype='int64')
    npNationality = np.asarray(Nationality, dtype='str')
    np_Season = np.asarray(Season, dtype='int64')
    npLeauge = np.asarray(leauge, dtype='str')
    np_CUT = np.asarray(CUT, dtype='float64')
    np_Interception = np.asarray(interception, dtype='float64')

    np_CUT = np_Income/np_Departures
    np_CUT_inflation = np_Interception/np_Departures

    return np.stack((npLeauge,np_Season,npNationality,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)

#get average League netto earnings for each player
def GetAVGBalanceFORpayerDepartures(DFrame):

        #count number of rows in date frame
        count = NumberOfRows(DFrame)

        #reserving the number of elements in a row
        Nationality = [0] * count
        Balance = [0] * count
        Departures = [0] * count
        leauge = [0] * count
        Season = [0] * count
        koef = [0] * count
        CUT =  [0] * count
        interception = [0] * count

        # cast DataFrame rows to folat and int
        DFrame["Balance"].astype(np.float64)
        DFrame["Departures"].astype(np.int64)
        DFrame["Competition"].astype(np.str)
        DFrame["Nationality"].astype(np.str)
        DFrame["Season"].astype(np.int64)

        #save values from the dateframe to a string
        i = 0
        for i in range(0,count):
            Balance[i] = DFrame["Balance"][i]
            Departures[i] = DFrame["Departures"][i]
            leauge[i] = DFrame["Competition"][i]
            Season[i] = DFrame["Season"][i]
            Nationality[i] = DFrame["Nationality"][i]

        for i in range(0,count):
            temp = Season[i]
            a = GETCoefficients(coef,temp)
            koef[i] = a

        for i in range(0,count):
            interception[i] = round((Balance[i]*koef[i]),2)

        # conversion to numpy
        np_Balance = np.asarray(Balance, dtype='float64')
        np_Departures = np.asarray(Departures, dtype='int64')
        npNationality = np.asarray(Nationality, dtype='str')
        np_Season = np.asarray(Season, dtype='int64')
        npLeauge = np.asarray(leauge, dtype='str')
        np_CUT = np.asarray(CUT, dtype='float64')
        np_Interception = np.asarray(interception, dtype='float64')

        np_CUT = np_Balance/np_Departures
        np_CUT_inflation = np_Interception/np_Departures

        return np.stack((npLeauge,np_Season,npNationality,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)

# get Data for every year avg expending for player
def GetDataForLeauge_AVG_Seasons(DFrame):

    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row

    Nationality = [0] * count
    Arrivals = [0] * count
    leauge = [0] * count
    niz1 = [0] *count
    niz2 = [0] *count
    niz3 = [0] * count


    # cast DataFrame rows to folat and int
    DFrame["Arrivals"].astype(np.int64)

    DFrame["Competition"].astype(np.str)
    i = 0
    for i in range(0,count):
        Arrivals[i] = DFrame["Arrivals"][i]
        leauge[i] = DFrame["Competition"][i]

    npLeauge = np.asarray(leauge, dtype='str')
    np_Arrival = np.asarray(Arrivals, dtype='int64')
    np_niz1 = np.asarray(niz1,dtype='str')
    np_niz2 = np.asarray(niz2, dtype='int64')
    np_niz3 = np.asarray(niz3, dtype='int64')



    niz = np.stack((np_niz1,np_niz2,np_niz3), axis = -1)
    a = np.stack((np_Arrival,npLeauge), axis = -1)

    # Function
    n = count
    t = 0
    visited = [False for i in range(n)]
    # Traverse through array elements
    # and count frequencies
    for i in range(n):
        # Skip this element if already
        # processed
        if (visited[i] == True):
            continue
        count = 1
        suma = int(a[i][0])
        for j in range(i + 1, n, 1):
            if (a[i][1] == a[j][1]):
                suma += int(a[j][0])
                #print("suma 2 : ",suma)
                visited[j] = True
                count += 1

        if a[i][1] != 0 :

            niz[t][1] = a[i][1]
            niz[t][0] = suma
            niz[t][2] =  count
            t +=1
            suma = 0



    print("##################################")
    print("TEST  nosadndsaondondso")
    for p in niz:
        print(p)
    print("##################################")
    N =0
    for i in range(0,len(niz)):
        #print("niz[i][0]",niz[i][0],"i : ",i)
        if int(niz[i][0]) != 0:
            N +=1
            #print(" != niz[i][0]",niz[i][0],"i : ",i)

    print("N : ",N)

    #inicijalizacija novog niza ::
    niz_1 = [0] * N
    niz_2 = [0] * N
    niz_3 = [0] * N

    np_niz_1 = np.asarray(niz_1,dtype='str')
    np_niz_2 = np.asarray(niz_2, dtype='int64')
    b = np.asarray(niz_2, dtype='int64')
    np_niz_3 = np.asarray(niz_3, dtype='int64')

    new_niz = np.stack((np_niz_1,np_niz_2,np_niz_3), axis = -1)

    for i in range(0,N):
        #print("int(niz[i][0])",int(niz[i][0]))
        if int(niz[i][0]) != 0:
            #print(" drugi ispis int(niz[i][0])",int(niz[i][0]))
            int(niz[i][0]) != 0
            new_niz[i][0] = niz[i][1]
            new_niz[i][1] = niz[i][0]
            new_niz[i][2] = niz[i][2]
    print("NEW NIZZZ")
    for p in  new_niz:
        print(p)

    #outputlist = sorted(new_niz, key=itemgetter(2), reverse=False) # sortiranje po elemnetima i po stupcima
    print("***********************************************************")
    print("Sortirano")

    a =  sorted(new_niz, key=lambda new_niz: int(new_niz[1]))
    for i in  a:
        print(i)
    print("***********************************************************")
    #return np.stack((np_Arrival,npLeauge), axis = -1)
    print("***********************************************************")
