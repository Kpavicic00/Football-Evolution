# -*- coding: utf-8 -*-
from collections import Counter
from operator import itemgetter
from sort_functions import*
import numpy as np
import pandas as pd
import csv
import sys

coef = "/home/kristijan/github/FootballEvolcion/Datas/file.txt"
# functions

# with open(filename, 'a') as f:  # Use append mode.
#     df.to_csv(f, index=False, header=False)

# write to file
def Write_multiple_DF(csv_file,dat):
    with open(csv_file, 'a') as f:  # Use append mode.
        dat.to_csv(f, index=False,header=False)
#######################################################################################################################################

# write to file
def WriteTOcsvFILE_one_DATAFRAMES(csv_file,dat):

    np.savetxt(csv_file, dat, fmt='%s', delimiter=' ', newline='\n', header=None, footer='     => End of file <=')
    print("Write into   file !!!"+ csv_file+" end ") # function ~ 1.
#######################################################################################################################################

# write to file
def WriteTOcsvFILE_mult_DATAFRAMES(csv_file,datFRAME):

    with open(csv_file, 'w') as f:
         pd.concat([datFRAME], axis=1).to_csv(f) # function ~ 2.
#######################################################################################################################################

#   read csv file
def ReadCSV_file(file):

    with open(file, 'r') as csvFile:

        reader = csv.reader(csvFile)
        for row in reader:
            print(row)

    csvFile.close()

#function count number of rows for specific DateFrame
def NumberOfRows(datFrame):

    total_rows = len(datFrame)
    return  total_rows # function ~ 3.
#######################################################################################################################################

# functions_fore choose of season
def Input_order():

    while True:

        print("\n\t Enter a year of season   : ")
        value = input("\n\tValue between 1 and 7 :")

        try:
           value = int(value)
        except ValueError:
           print("\n\tValid number, please !!")
           continue
        if 1 <= value <= 7:
           return value
           break
        else:
           print("\n\tValue between 1 and 7 !!!") # function ~ 4.
#######################################################################################################################################

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
           print("\n\tValue between 2000 and 2018 !!!") # function ~ 5.
#######################################################################################################################################

# print the txt file
def printFile(data):

    #read the file
    f = open(data, "r")
    print(f.read())
    f.close() # function ~ 6
#######################################################################################################################################

# function  count the length of lines for the required size allocation of the string
def file_lengthy(fname):

    with open(fname) as f:
        for i ,j in enumerate (f):
            pass
        return i +1 # function ~ 7.
#######################################################################################################################################

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

    return np_specific_coefficient # function ~ 8.
#######################################################################################################################################

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

    return np_specific_coefficient # function ~ 9.
#######################################################################################################################################

# takes data with pandas function DataFrame
def DataFrameFunc(filePath):

    colls = ["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]
    dat = pd.read_csv(filePath,header = None , names = colls)
    return dat # function ~ 10.
#######################################################################################################################################

# takes data with pandas function DataFrame for Clubs datas
def DataFrameFuncClubs(filePath):

    colls = ["Order","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]
    dat = pd.read_csv(filePath,header = None , names = colls)
    return dat # function ~ 11.
#######################################################################################################################################

#get average League spending for each player
#  --> for League datas
def GetAVGExpendFORplayerArrivals(DFrame):

    # count number of rows in date frame
    count = NumberOfRows(DFrame)

    # reserving arraya for cast
    Name_of_leauge = [0] * count
    Year_of_Season = [0] * count
    arrivals_players = [0] * count
    Nationality_leuge = [0] * count
    expenditures = [0] * count

    koef = [0] * count
    int_koef = [0] * count
    expend_inflation = [0] * count
    ###############################################################################

    # cast data from Data to float, int and str
    DFrame["Competition"].astype(np.str) # ind 0
    DFrame["Year"].astype(np.int64) # ind 1
    DFrame["Arrivals"].astype(np.int64) # ind 2
    DFrame["Nationality"].astype(np.str) # ind 3
    DFrame["Expenditures"].astype(np.int64) # ind 4
    ###############################################################################

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Name_of_leauge[i] = DFrame["Competition"][i] # ind 0
        Year_of_Season[i] = DFrame["Year"][i] # ind 1
        arrivals_players[i] = DFrame["Arrivals"][i] # ind 2
        Nationality_leuge[i] = DFrame["Nationality"][i] # ind 3
        expenditures[i] = DFrame["Expenditures"][i] # ind 4

    # the inflation calculation coefficient operatorion
    for i in range(0,count):
        temp = Year_of_Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a
        ###############################################################################

    # save coefficient to specific array
    for i in range(0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp
        ###############################################################################

    # operation of inflation
    for i in range(0,count):
        a = float(expenditures[i])*int_koef[i]
        expend_inflation[i] = round(a,2)
        ###############################################################################

    # conversion to numpy
    np_Expend = np.asarray(expenditures, dtype='float64') # ind 0
    np_arrivals_players = np.asarray(arrivals_players, dtype='int64') # ind 1
    np_Year_of_Season = np.asarray(Year_of_Season, dtype='int64') # ind 2
    npNationality_leuge = np.asarray(Nationality_leuge, dtype='str') # ind 3
    np_Name_of_leauge = np.asarray(Name_of_leauge, dtype='str') # ind 4
    np_expend_inflation = np.asarray(expend_inflation, dtype='float64') # ind 5
    ###############################################################################



    niz = np.stack((np_Name_of_leauge,np_Year_of_Season,npNationality_leuge,np.round((np_Expend/np_arrivals_players),2)
    ,np.round((np_expend_inflation/np_arrivals_players),2)), axis = -1)
    ###############################################################################

    a = Input_chose_of_GetAVGExpendFORplayerArrivals(niz)
    # convert from stack with values to data for dataFrame
    data = np.array(a)
    # set to DataFrame
    df = pd.DataFrame(data)
    # name of labels for head or names of collums
    df.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Expend by player|  ', '  Expend + Inflation by player|  ']
    ###############################################################################
    # return DataFrame with head an names of collums
    print(df)
    return df  # function FULL -> BATCH optimized ~ 12.
#######################################################################################################################################

# BATCH for  specific filtring data from estraction data from function GetAVGIncomeFORplayerDepartures
#  --> for League datas
def BATCH_for_GetAVGExpendFORplayerArrivals(DFrame):

    # DataFrame to ecstract data
    nDFRAME = GetAVGExpendFORplayerArrivals(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)


    #reserving the number of elements in a row
    Name_of_leauge  = [0] * count # indx 0
    Year_of_Season = [0] * count # indx 1
    Nationality = [0] * count # indx 2
    Expend_by_player = [0] * count # indx 3
    Expend_Inflation_by_player = [0] * count # indx 4

    # cast from DataFrame to str int an float
    nDFRAME["    Name of League |  "].astype(np.str)# ind 0
    nDFRAME["   Year of Season |  "].astype(np.int64)# ind 1
    nDFRAME["    Nationality |  "].astype(np.str)# ind 2
    nDFRAME["    Expend by player|  "].astype(np.float64)# ind 3
    nDFRAME["  Expend + Inflation by player|  "].astype(np.float64)# ind 4
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):
        Name_of_leauge[i] =  nDFRAME["    Name of League |  "][i] # indx 0
        Year_of_Season[i] = nDFRAME["   Year of Season |  "][i] # indx 1
        Nationality[i] = nDFRAME["    Nationality |  "][i] # indx 2
        Expend_by_player[i] = nDFRAME["    Expend by player|  "][i] # indx 3
        Expend_Inflation_by_player[i] = nDFRAME["  Expend + Inflation by player|  "][i] # indx 4
        ###############################################################################

    # conversion to numpy
    np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
    np_Year_of_Season = np.asarray(Year_of_Season,dtype='int64')# indx 1
    np_Nationality = np.asarray(Nationality,dtype='str')# indx 2
    np_Expend_by_player= np.asarray(Expend_by_player, dtype = 'float64') # indx 3
    np_Expend_Inflation_by_player = np.asarray(Expend_Inflation_by_player,dtype='float64') # indx 4
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Name_of_leauge,np_Year_of_Season,np_Nationality,np_Expend_by_player,np_Expend_Inflation_by_player),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Expend by player|  ', '  Expend + Inflation by player|  ']
    ###############################################################################

    print("################################################################################################################")
    print(df_a)
    print("################################################################################################################")

    # convert data from numpay ndarray to list and remove   duplicates elemtes of list for LEAUGE
    listLEAUGE = np_Name_of_leauge.tolist()
    listLEAUGE = remove_duplicates(listLEAUGE)
    listLEAUGE.sort()
    ###############################################################################

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Year_of_Season
    listYear_of_Season = np_Year_of_Season.tolist()
    listYear_of_Season = remove_duplicates(listYear_of_Season)
    listYear_of_Season.sort()
    ###############################################################################

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Nationality
    listNationality = np_Nationality.tolist()
    listNationality = remove_duplicates(listNationality)
    listNationality.sort()
    ###############################################################################
    #######################################################################################################################################


    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'

    while True:

        print("\n")
        print("\n\t Chose a option of proces data by LEAUGE,Year_of_Season or Nationality  : ")
        print("\t 1 -> LEAUGE statistic ! ")
        print("\t 2 -> Year_of_Season statistic ! ")
        print("\t 3 -> Nationality statistic ! ")
        value = raw_input("\n\tValue between 1 and 3    : ")
        if value.isdigit() == True:

            value = int(value)
            if value == 1:

                flag = 1
                ###############################################################################
                cont_LEAUGE = 0
                print("###############################################################################")
                print("\t Meni  LEAUGE statistic  !!!")
                for i in range(0,len(listLEAUGE)):
                    print(i+1,". : ",listLEAUGE[i])
                    cont_LEAUGE += 1
                print("###############################################################################")
                while True:

                    print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_LEAUGE:
                            print("You Chose : ",listLEAUGE[value])
                            flagTemp =  str(listLEAUGE[value])
                            break

                        else:
                           print("\n\tValue between bounds :")

                    elif value.isdigit() != True:
                         print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
                         continue
                break
                ###############################################################################
            elif value == 2:
                flag = 2
                ###############################################################################
                cont_Year_of_Season = 0
                print("###############################################################################")
                print("\t Meni  Year_of_Season statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listYear_of_Season)):
                    print(i+1,". : ",listYear_of_Season[i])
                    cont_Year_of_Season += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter Year_of_Season   between 1 and ",cont_Year_of_Season," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_Year_of_Season:

                            print("You Chose : ",listYear_of_Season[value])
                            flagTemp =  int(listYear_of_Season[value])
                            break
                        else:
                           print("\n\tValue between bounds :")

                    elif value.isdigit() != True:

                         print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
                         continue

                break
                ###############################################################################
            elif value == 3:

                flag = 3
                ###############################################################################
                cont_Nationality = 0
                print("###############################################################################")
                print("\t Meni  Competition statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listNationality)):
                    print(i+1,". : ",listNationality[i])
                    cont_Nationality += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
                    value = raw_input("\n\tValue : " )

                    if value.isdigit() == True:
                        value = int(value)
                        value =value -1

                        if 0 <= value < cont_Nationality:
                            print("You Chose : ",listNationality[value])
                            flagTemp =  str(listNationality[value])
                            break
                        else:

                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\tValue between 1 or  2  !!!")
                         continue
                break
                ###############################################################################

            else:
                print("\n\tValue between 1 and  4  !!!")

        elif value.isdigit() != True:

             print("\n\tValue between 1 and  4  !!!")
             continue
    #######################################################################################################################################


    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    # name of LEAUGE
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                bro +=1
    ###############################################################################

    # count number of rows in date frame
    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][1]) == flagTemp :
                bro +=1
    ###############################################################################

    # count number of rows in date frame
    # Nationality
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                bro +=1
    ###############################################################################

    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from State user chose options

    # name of LEAUGE
    y = 0
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################

    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][1]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################

    # Nationality
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################

    # reserving the number of elements in a row
    niz_N1 = [0]*bro

    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz1,np_niz2,np_niz1,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        y+=1
    ###############################################################################

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Expend by player|  ', '  Expend + Inflation by player|  ']
    print("###################################################################################################################################################")
    print(df_new)
    print("###################################################################################################################################################")

    return df_new # function FULL optimized ~ 13.
#######################################################################################################################################

#get average League brutto earnings for each player
#  --> for League datas
def GetAVGIncomeFORplayerDepartures(DFrame):

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
    int_koef = [0] * count
    ###############################################################################

    # cast DataFrame rows to folat and int
    DFrame["Income"].astype(np.int64)
    DFrame["Departures"].astype(np.int64)
    DFrame["Nationality"].astype(np.str)
    DFrame["Competition"].astype(np.str)
    DFrame["Year"].astype(np.int64)
    ###############################################################################

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Income[i] = DFrame["Income"][i]
        Departures[i] = DFrame["Departures"][i]
        leauge[i] = DFrame["Competition"][i]
        Season[i] = DFrame["Year"][i]
        Nationality[i] = DFrame["Nationality"][i]
        ###############################################################################

    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a
        ###############################################################################

    for i in range(0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp
        ###############################################################################

    for i in range(0,count):
        a = float(Income[i])*int_koef[i]
        interception[i] = round(a,2)
        ###############################################################################


    # conversion to numpy
    np_Income = np.asarray(Income, dtype='float64')
    np_Departures = np.asarray(Departures, dtype='int64')
    npNationality = np.asarray(Nationality, dtype='str')
    np_Season = np.asarray(Season, dtype='int64')
    npLeauge = np.asarray(leauge, dtype='str')
    np_CUT = np.asarray(CUT, dtype='float64')
    np_Interception = np.asarray(interception, dtype='float64')
    ###############################################################################

    np_CUT = np_Income/np_Departures
    np_CUT_inflation = np_Interception/np_Departures

    niz = np.stack((npLeauge,np_Season,npNationality,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)

    ###############################################################################
    a = Input_chose_of_GetAVGIncomeFORplayerDepartures(niz)
    # convert from stack with values to data for dataFrame
    data = np.array(a)
    # set to DataFrame
    df = pd.DataFrame(data)
    # name of labels for head or names of collums
    df.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Income by player|  ', '  Income + Inflation by player|  ']
    ###############################################################################
    # return DataFrame with head an names of collums
    print(df)
    return df# function FULL -> BATCH optimized ~ 14.
#######################################################################################################################################

# BATCH for  specific filtring data from estraction data from function GetAVGIncomeFORplayerDepartures
#  --> for League datas
def BATCH_for_GetAVGIncomeFORplayerDepartures(DFrame):

    # DataFrame to ecstract data
    nDFRAME = GetAVGIncomeFORplayerDepartures(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)


    #reserving the number of elements in a row
    Name_of_leauge  = [0] * count # indx 0
    Year_of_Season = [0] * count # indx 1
    Nationality = [0] * count # indx 2
    Income_by_player = [0] * count # indx 3
    Income_Inflation_by_player = [0] * count # indx 4

    # '    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Income by player|  ', '  Income + Inflation by player|  '
    # cast DataFrame rows to folat and int
    nDFRAME["    Name of League |  "].astype(np.str)# ind 0
    nDFRAME["   Year of Season |  "].astype(np.int64)# ind 1
    nDFRAME["    Nationality |  "].astype(np.str)# ind 2
    nDFRAME["    Income by player|  "].astype(np.float64)# ind 3
    nDFRAME["  Income + Inflation by player|  "].astype(np.float64)# ind 4
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):
        Name_of_leauge[i] =  nDFRAME["    Name of League |  "][i] # indx 0
        Year_of_Season[i] = nDFRAME["   Year of Season |  "][i] # indx 1
        Nationality[i] = nDFRAME["    Nationality |  "][i] # indx 2
        Income_by_player[i] = nDFRAME["    Income by player|  "][i] # indx 3
        Income_Inflation_by_player[i] = nDFRAME["  Income + Inflation by player|  "][i] # indx 4
        ###############################################################################

    # conversion to numpy
    np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
    np_Year_of_Season = np.asarray(Year_of_Season,dtype='int64')# indx 1
    np_Nationality = np.asarray(Nationality,dtype='str')# indx 2
    np_Income_by_player = np.asarray(Income_by_player, dtype = 'float64') # indx 3
    np_Income_Inflation_by_player = np.asarray(Income_Inflation_by_player,dtype='float64') # indx 4
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Name_of_leauge,np_Year_of_Season,np_Nationality,np_Income_by_player,np_Income_Inflation_by_player),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Income by player|  ', '  Income + Inflation by player|  ']
    ###############################################################################

    print("################################################################################################################")
    print(df_a)
    print("################################################################################################################")

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for LEAUGE
    listLEAUGE = np_Name_of_leauge.tolist()
    listLEAUGE = remove_duplicates(listLEAUGE)
    listLEAUGE.sort()
    ###############################################################################

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Year_of_Season
    listYear_of_Season = np_Year_of_Season.tolist()
    listYear_of_Season = remove_duplicates(listYear_of_Season)
    listYear_of_Season.sort()
    ###############################################################################

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Nationality
    listNationality = np_Nationality.tolist()
    listNationality = remove_duplicates(listNationality)
    listNationality.sort()
    ###############################################################################
    #######################################################################################################################################

    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'

    while True:

        print("\n")
        print("\n\t Chose a option of proces data by LEAUGE,Year_of_Season or Nationality  : ")
        print("\t 1 -> LEAUGE statistic ! ")
        print("\t 2 -> Year_of_Season statistic ! ")
        print("\t 3 -> Nationality statistic ! ")
        value = raw_input("\n\tValue between 1 and 3    : ")
        print("\n")
        if value.isdigit() == True:

            value = int(value)
            if value == 1:

                flag = 1
                ###############################################################################
                cont_LEAUGE = 0
                print("###############################################################################")
                print("\t Meni  LEAUGE statistic  !!!")
                for i in range(0,len(listLEAUGE)):
                    print(i+1,". : ",listLEAUGE[i])
                    cont_LEAUGE += 1
                print("###############################################################################")
                while True:

                    print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_LEAUGE:

                            print("You Chose : ",listLEAUGE[value])
                            flagTemp =  str(listLEAUGE[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
                         continue
                break
                ###############################################################################
            elif value == 2:

                flag = 2
                ###############################################################################
                cont_Year_of_Season = 0
                print("###############################################################################")
                print("\t Meni  State statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listYear_of_Season)):
                    print(i+1,". : ",listYear_of_Season[i])
                    cont_Year_of_Season += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_Year_of_Season:
                            print("You Chose : ",listYear_of_Season[value])
                            flagTemp =  int(listYear_of_Season[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
                         continue
                break
                ###############################################################################
            elif value == 3:
                flag = 3
                ###############################################################################
                cont_Nationality = 0
                print("###############################################################################")
                print("\t Meni  Competition statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listNationality)):
                    print(i+1,". : ",listNationality[i])
                    cont_Nationality += 1
                print("###############################################################################")

                while True:
                    print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_Nationality:

                            print("You Chose : ",listNationality[value])
                            flagTemp =  str(listNationality[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
                         continue
                break
                ###############################################################################
            else:
                print("\n\tValue between 1 or  4  !!!")
        elif value.isdigit() != True:

             print("\n\tValue between 1 and 3  !!!")
             continue
    #######################################################################################################################################


    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    # name of LEAUGE
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                bro +=1
    ###############################################################################

    # count number of rows in date frame
    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][1]) == flagTemp :
                bro +=1
    ###############################################################################

    # count number of rows in date frame
    # Nationality
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                bro +=1
    ###############################################################################
    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from State user chose options

    # name of LEAUGE
    y = 0
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################
    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][1]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################
    # Nationality
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################

    # reserving the number of elements in a row
    niz_N1 = [0]*bro
    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz1,np_niz2,np_niz1,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        y+=1
    ###############################################################################

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Income by player|  ', '  Income + Inflation by player|  ']
    print("###################################################################################################################################################")
    print(df_new)
    print("###################################################################################################################################################")

    return df_new # function FULL optimized ~ 15.
#######################################################################################################################################

#get average League netto earnings for each player
#  --> for League datas
def GetAVGBalanceFORplayerDepartures(DFrame):

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
        int_koef = [0] * count
        ###############################################################################

        # cast DataFrame rows to folat and int
        DFrame["Balance"].astype(np.int64)
        DFrame["Departures"].astype(np.int64)
        DFrame["Competition"].astype(np.str)
        DFrame["Nationality"].astype(np.str)
        DFrame["Year"].astype(np.int64)
        ###############################################################################

        #save values from the dateframe to a string
        i = 0
        for i in range(0,count):
            Balance[i] = DFrame["Balance"][i]
            Departures[i] = DFrame["Departures"][i]
            leauge[i] = DFrame["Competition"][i]
            Season[i] = DFrame["Year"][i]
            Nationality[i] = DFrame["Nationality"][i]
            ###############################################################################

        # for i in range(0,count):
        #     temp = Season[i]
        #     a = GETCoefficients(coef,temp)
        #     koef[i] = a
        #     ###############################################################################
        #
        # for i in range(0,count):
        #     interception[i] = round((Balance[i]*koef[i]),2)
        #     ###############################################################################

        for i in range(0,count):
            temp = Season[i]
            a = GETCoefficients(coef,temp)
            koef[i] = a
            ###############################################################################

        for i in range(0,len(int_koef)):
            temp = float(koef[i])
            int_koef[i] = temp
            ###############################################################################

        for i in range(0,count):
            a = float(Balance[i])*int_koef[i]
            interception[i] = round(a,2)
            ###############################################################################

        # conversion to numpy
        np_Balance = np.asarray(Balance, dtype='float64')
        np_Departures = np.asarray(Departures, dtype='int64')
        npNationality = np.asarray(Nationality, dtype='str')
        np_Season = np.asarray(Season, dtype='int64')
        npLeauge = np.asarray(leauge, dtype='str')
        np_CUT = np.asarray(CUT, dtype='float64')
        np_Interception = np.asarray(interception, dtype='float64')
        ###############################################################################

        np_CUT = np_Balance/np_Departures
        np_CUT_inflation = np_Interception/np_Departures


        niz = np.stack((npLeauge,np_Season,npNationality,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)

        ###############################################################################
        a = Input_chose_of_GetAVGBalanceFORplayerDepartures(niz)
        # set to DataFrame
        data = np.array(a)
        # set to DataFrame
        df = pd.DataFrame(data)
        # name of labels for head or names of collums
        ###############################################################################
        df.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Balance by player|  ', '  Balance + Inflation by player|  ']
        # return DataFrame with head an names of collums
        print("GetAVGBalanceFORpayerDepartures TEST")
        print(df)
        return df # function FULL -> BATCH ~ 16.
#######################################################################################################################################

# BATCH for  specific filtring data from estraction data from function GetAVGBalanceFORplayerDepartures
#  --> for League datas
def BATCH_for_GetAVGBalanceFORplayerDepartures(DFrame):

    # DataFrame to ecstract data
    nDFRAME = GetAVGBalanceFORplayerDepartures(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)


    #reserving the number of elements in a row
    Name_of_leauge  = [0] * count # indx 0
    Year_of_Season = [0] * count # indx 1
    Nationality = [0] * count # indx 2
    Balance_by_player = [0] * count # indx 3
    Balance_Inflation_by_player = [0] * count # indx 4

    # '    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Balance by player|  ', '  Balance + Inflation by player|  '
    # cast DataFrame rows to folat and int
    nDFRAME["    Name of League |  "].astype(np.str)# ind 0
    nDFRAME["   Year of Season |  "].astype(np.int64)# ind 1
    nDFRAME["    Nationality |  "].astype(np.str)# ind 2
    nDFRAME["    Balance by player|  "].astype(np.float64)# ind 3
    nDFRAME["  Balance + Inflation by player|  "].astype(np.float64)# ind 4
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):
        Name_of_leauge[i] =  nDFRAME["    Name of League |  "][i] # indx 0
        Year_of_Season[i] = nDFRAME["   Year of Season |  "][i] # indx 1
        Nationality[i] = nDFRAME["    Nationality |  "][i] # indx 2
        Balance_by_player[i] = nDFRAME["    Balance by player|  "][i] # indx 3
        Balance_Inflation_by_player[i] = nDFRAME["  Balance + Inflation by player|  "][i] # indx 4
        ###############################################################################

    # conversion to numpy
    np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
    np_Year_of_Season = np.asarray(Year_of_Season,dtype='int64')# indx 1
    np_Nationality = np.asarray(Nationality,dtype='str')# indx 2
    np_Balance_by_player = np.asarray(Balance_by_player, dtype = 'float64') # indx 3
    np_Balance_Inflation_by_player = np.asarray(Balance_Inflation_by_player,dtype='float64') # indx 4
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Name_of_leauge,np_Year_of_Season,np_Nationality,np_Balance_by_player,np_Balance_Inflation_by_player),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Balance by player|  ', '  Balance + Inflation by player|  ']
    ###############################################################################

    print("################################################################################################################")
    print(df_a)
    print("################################################################################################################")

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for LEAUGE
    listLEAUGE = np_Name_of_leauge.tolist()
    listLEAUGE = remove_duplicates(listLEAUGE)
    listLEAUGE.sort()
    ###############################################################################

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Year_of_Season
    listYear_of_Season = np_Year_of_Season.tolist()
    listYear_of_Season = remove_duplicates(listYear_of_Season)
    listYear_of_Season.sort()
    ###############################################################################

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Nationality
    listNationality = np_Nationality.tolist()
    listNationality = remove_duplicates(listNationality)
    listNationality.sort()
    ###############################################################################
    #######################################################################################################################################


    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'

    while True:

        print("\n")
        print("\n\t Chose a option of proces data by LEAUGE,Year_of_Season or Nationality  : ")
        print("\t 1 -> LEAUGE statistic ! ")
        print("\t 2 -> Year_of_Season statistic ! ")
        print("\t 3 -> Nationality statistic ! ")
        value = raw_input("\n\tValue between 1 and 3    : ")
        print("\n")
        if value.isdigit() == True:

            value = int(value)
            if value == 1:
                flag = 1
                ###############################################################################
                cont_LEAUGE = 0
                print("###############################################################################")
                print("\t Meni  LEAUGE statistic  !!!")
                for i in range(0,len(listLEAUGE)):
                    print(i+1,". : ",listLEAUGE[i])
                    cont_LEAUGE += 1
                print("###############################################################################")
                while True:

                    print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_LEAUGE:
                            print("You Chose : ",listLEAUGE[value])
                            flagTemp =  str(listLEAUGE[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
                         continue
                break
                ###############################################################################
            elif value == 2:

                flag = 2
                ###############################################################################
                cont_Year_of_Season = 0
                print("###############################################################################")
                print("\t Meni  State statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listYear_of_Season)):
                    print(i+1,". : ",listYear_of_Season[i])
                    cont_Year_of_Season += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_Year_of_Season:
                            print("You Chose : ",listYear_of_Season[value])
                            flagTemp =  int(listYear_of_Season[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
                         continue

                break
                ###############################################################################
            elif value == 3:
                flag = 3
                ###############################################################################
                cont_Nationality = 0
                print("###############################################################################")
                print("\t Meni  Competition statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listNationality)):
                    print(i+1,". : ",listNationality[i])
                    cont_Nationality += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_Nationality:
                            print("You Chose : ",listNationality[value])
                            flagTemp =  str(listNationality[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
                         continue
                break
                ###############################################################################
            else:
                print("\n\tValue between 1 or  4  !!!")
        elif value.isdigit() != True:

             print("\n\tValue between 1 or    !!!")
             continue

    #######################################################################################################################################


    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    # name of LEAUGE
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                bro +=1
    ###############################################################################

    # count number of rows in date frame
    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][1]) == flagTemp :
                bro +=1
    ###############################################################################

    # count number of rows in date frame
    # Nationality
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                bro +=1
    ###############################################################################
    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from State user chose options

    # name of LEAUGE
    y = 0
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################
    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][1]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################
    # Nationality
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################

    # reserving the number of elements in a row
    niz_N1 = [0]*bro
    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz1,np_niz2,np_niz1,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        y+=1
    ###############################################################################

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Balance by player|  ', '  Balance + Inflation by player|  ']
    print("###################################################################################################################################################")
    print(df_new)
    print("###################################################################################################################################################")

    return df_new # function FULL optimized ~ 17.
#######################################################################################################################################

# get sorted data by the leauge
#  --> for League datas
def GetDataForLeauge_AVG_Seasons(DFrame):

    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Nationality = [0] * count
    Arrivals = [0] * count
    koef = [0] * count
    Season = [0] * count
    leauge = [0] * count
    niz1 = [0] *count
    Expenditures = [0] *count
    Income = [0] *count
    Balance = [0] *count
    Departures = [0] *count
    inter_Balance = [0] *count
    inter_Expenditures = [0] *count
    inter_Income = [0] *count
    int_koef = [0] * count
    ###############################################################################

    # cast DataFrame rows to folat and int and str
    DFrame["Expenditures"].astype(np.int64)
    DFrame["Income"].astype(np.int64)
    DFrame["Balance"].astype(np.int64)
    DFrame["Departures"].astype(np.int64)
    DFrame["Arrivals"].astype(np.int64)
    DFrame["Competition"].astype(np.str)
    DFrame["Year"].astype(np.int64)
    ###############################################################################

    i = 0
    for i in range(0,count):
        Arrivals[i] = DFrame["Arrivals"][i]
        leauge[i] = DFrame["Competition"][i]
        Season[i] =  DFrame["Year"][i]
        Expenditures[i] =  DFrame["Expenditures"][i]
        Income[i] =  DFrame["Income"][i]
        Balance[i] =  DFrame["Balance"][i]
        Departures[i] =  DFrame["Departures"][i]
        ###############################################################################

    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a
        ###############################################################################

    for i in range(0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp
        ###############################################################################

    for i in range(0,count):
        a = float(Balance[i])*int_koef[i]
        b = float(Expenditures[i])*int_koef[i]
        c = float(Income[i])*int_koef[i]
        inter_Balance[i] = round(a,2)
        inter_Expenditures[i] = round(b,2)
        inter_Income[i] = round(c,2)
        ###############################################################################

    npLeauge = np.asarray(leauge, dtype = 'str')
    np_Arrival = np.asarray(Arrivals, dtype ='int64')
    np_Season = np.asarray(Season, dtype = 'int64' )
    np_Expenditures = np.asarray(inter_Expenditures, dtype = 'float64' )
    np_Income = np.asarray(inter_Income, dtype = 'float64' )
    np_Balance = np.asarray(inter_Balance, dtype = 'float64' )
    np_Departures = np.asarray(Departures, dtype = 'int64' )
    ###############################################################################


    np_niz1 = np.asarray(niz1, dtype = 'str')
    np_niz2 = np.asarray(niz1, dtype = 'int64')
    np_niz3 = np.asarray(niz1, dtype = 'int64')
    np_niz4 = np.asarray(niz1, dtype = 'int64')


    niz = np.stack((np_niz1,np_niz2,np_niz3,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4), axis = -1)
    a = np.stack((np_Arrival,npLeauge,np_Expenditures,np_Income,np_Balance,np_Departures,np_Season), axis = -1)
    ###############################################################################

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
        suma_Arrival = int(a[i][0])
        sum_Expenditures = float(a[i][2])
        sum_Income = float(a[i][3])
        sum_Balance = float(a[i][4])
        sum_Departures = int(a[i][5])
        ###############################################################################
        for j in range(i + 1, n, 1):
            if (a[i][1] == a[j][1]):
                suma_Arrival += int(a[j][0])
                sum_Expenditures += float(a[j][2])
                sum_Income += float(a[j][3])
                sum_Balance += float(a[j][4])
                sum_Departures += int(a[j][5])
                visited[j] = True
                count += 1
                ###############################################################################

        if a[i][1] != 0 :
            niz[t][1] = a[i][1]
            niz[t][0] = suma_Arrival
            niz[t][2] = count
            niz[t][3] = sum_Expenditures
            niz[t][4] = sum_Income
            niz[t][5] = sum_Departures
            niz[t][6] = sum_Balance
            niz[t][7] = round(sum_Expenditures/float(suma_Arrival),2)
            niz[t][8] = round(sum_Income/float(sum_Departures),2)
            niz[t][9] = round(sum_Balance/float(sum_Departures),2)
            niz[t][10] = round(sum_Expenditures/float(count),2)
            niz[t][11] = round(sum_Income/float(count),2)
            niz[t][12] = round(sum_Balance/float(count),2)
            niz[t][13] = a[i][6]
            t +=1
            suma = 0
            ###############################################################################

    N =0
    for i in range(0,len(niz)):
        if int(niz[i][0]) != 0:
            N +=1


    #inicijalizacija novog niza ::
    niz_1 = [0] * N


    np_niz_1 = np.asarray(niz_1,dtype='str')
    np_niz_2 = np.asarray(niz_1, dtype='int64')
    np_niz_3 = np.asarray(niz_1, dtype='int64')
    np_niz_4 = np.asarray(niz_1, dtype='float64')


    new_niz = np.stack((np_niz_1,np_niz_2,np_niz_3,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4), axis = -1)
    ###############################################################################
    for i in range(0,N):
        #print("int(niz[i][0])",int(niz[i][0]))
        if int(niz[i][0]) != 0:
            #print(" drugi ispis int(niz[i][0])",int(niz[i][0]))
            int(niz[i][0]) != 0
            new_niz[i][0] = niz[i][1] # leauge
            new_niz[i][1] = niz[i][3] # Expend
            new_niz[i][2] = niz[i][4] # Income
            new_niz[i][3] = niz[i][6] # Balance
            new_niz[i][4] = niz[i][2] # number of seasons
            new_niz[i][5] = niz[i][0] # sum of Arrivlas of all seasons
            new_niz[i][6] = niz[i][5] # sum of Depatrues of all seasons
            new_niz[i][7] = niz[i][7] # avg Expend of Arrivlas
            new_niz[i][8] = niz[i][8] # avg Income of Arrivlas
            new_niz[i][9] = niz[i][9] # avg Balance of Arrivlas
            new_niz[i][10] = niz[i][10] # avg Expend number the seasons
            new_niz[i][11] = niz[i][11] # avg Income number the seasons
            new_niz[i][12] = niz[i][12] # avg Balance number the seasons
            ###############################################################################

    # call the function
    a = Input_chose_of_GetDataForLeauge_AVG_Season(new_niz)
    # set to DataFrame
    data = np.array(a)

    df = pd.DataFrame(data)
    df.columns = ['    Name of leauge |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
     '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
     '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
    print(df)
    ###############################################################################
    return df # function FULL -> BATCH ~ 18.
#######################################################################################################################################

# BATCH for  specific filtring data from estraction data from function GetDataForLeauge_AVG_Seasons
#  --> for League datas
def BATCH_for_GetDataForLeauge_AVG_Seasons(DFrame):

    # DataFrame to ecstract data
    nDFRAME = GetDataForLeauge_AVG_Seasons(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)


    #reserving the number of elements in a row
    Name_of_leauge  = [0] * count # indx 0
    Expend = [0] * count # indx 1
    Income = [0] * count # indx 2
    Balance =  [0] * count # indx 3
    number_of_Season = [0] * count # indx 4
    sum_of_Arrivlas = [0] * count # indx 5
    sum_of_Depatrues = [0] * count # indx 6
    avg_Expend_of_Arrivlas = [0] * count # indx 7
    avg_Income_of_Depatrues =  [0] * count # indx 8
    avg_Balance_of_Depatrues = [0] * count # indx 9
    avg_Expend_Season = [0] * count # indx 10
    avg_Income_Season  =  [0] * count # indx 11
    avg_Balance_Season  =  [0] * count # indx 12


    # cast DataFrame rows to folat and int
    nDFRAME["    Name of leauge |  "].astype(np.str)# ind 0
    nDFRAME["    Expend |  "].astype(np.float64)# ind 1
    nDFRAME["    Income |  "].astype(np.float64)# ind 2
    nDFRAME["    Balance |  "].astype(np.float64)# ind 3
    nDFRAME["    number of Season |  "].astype(np.int64)# ind 4
    nDFRAME["    sum of Arrivlas |  "].astype(np.int64)# ind 5
    nDFRAME["    sum of Depatrues |  "].astype(np.int64)# ind 6
    nDFRAME["    avg Expend of Arrivlas |  "].astype(np.float64)# ind 7
    nDFRAME["    avg Income of Depatrues |  "].astype(np.float64)# ind 8
    nDFRAME["    avg Balance of Depatrues |  "].astype(np.float64)# ind 9
    nDFRAME["    avg Expend/Season |  "].astype(np.float64)# ind 10
    nDFRAME["    avg Income/Season |  "].astype(np.float64)# ind 11
    nDFRAME["    avg Balance/Season |  "].astype(np.float64)# ind 12
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Name_of_leauge[i] =  nDFRAME["    Name of leauge |  "][i] # indx 0
        Expend[i] = nDFRAME["    Expend |  "][i] # indx 1
        Income[i] = nDFRAME["    Income |  "][i] # indx 2
        Balance[i] = nDFRAME["    Balance |  "][i] # indx 3
        number_of_Season[i] = nDFRAME["    number of Season |  "][i] # indx 4
        sum_of_Arrivlas[i] = nDFRAME["    sum of Arrivlas |  "][i] # indx 5
        sum_of_Depatrues[i] = nDFRAME["    sum of Depatrues |  "][i] # indx 6
        avg_Expend_of_Arrivlas[i] = nDFRAME["    avg Expend of Arrivlas |  "][i] # indx 7
        avg_Income_of_Depatrues[i] = nDFRAME["    avg Income of Depatrues |  "][i] # indx 8
        avg_Balance_of_Depatrues[i] = nDFRAME["    avg Balance of Depatrues |  "][i] # indx 9
        avg_Expend_Season[i] = nDFRAME["    avg Expend/Season |  "][i] # indx 10
        avg_Income_Season[i] = nDFRAME["    avg Income/Season |  "][i] # indx 11
        avg_Balance_Season[i] = nDFRAME["    avg Balance/Season |  "][i] # indx 12
        ###############################################################################

    # conversion to numpy
    np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
    np_Expend = np.asarray(Expend,dtype='float64')# indx 1
    np_Income = np.asarray(Income,dtype='float64')# indx 2
    np_Balance = np.asarray(Balance, dtype = 'float64') # indx 3
    np_number_of_Season = np.asarray(number_of_Season,dtype='int64') # indx 4
    np_sum_of_Arrivlas = np.asarray(sum_of_Arrivlas, dtype ='int64') # indx 5
    np_sum_of_Depatrues = np.asarray(sum_of_Depatrues,dtype='int64') # indx 6
    np_avg_Expend_of_Arrivlas = np.asarray(avg_Expend_of_Arrivlas, dtype = 'float64' ) # indx 7
    np_avg_Income_of_Depatrues = np.asarray(avg_Income_of_Depatrues,dtype='float64') # indx 8
    np_avg_Balance_of_Depatrues = np.asarray(avg_Balance_of_Depatrues, dtype = 'float64' ) # indx 9
    np_avg_Expend_Season = np.asarray(avg_Expend_Season, dtype = 'float64' ) # indx 10
    np_avg_Income_Season = np.asarray(avg_Income_Season, dtype = 'float64' ) # indx 11
    np_avg_Balance_Season = np.asarray(avg_Balance_Season, dtype = 'float64' ) # indx 12
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Name_of_leauge,np_Expend,np_Income,np_Balance,np_number_of_Season,np_sum_of_Arrivlas,np_sum_of_Depatrues,
    np_avg_Expend_of_Arrivlas,np_avg_Income_of_Depatrues,np_avg_Balance_of_Depatrues,np_avg_Expend_Season,np_avg_Income_Season,np_avg_Balance_Season),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Name of leauge |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
     '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
     '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
    ###############################################################################

    print("################################################################################################################")
    print(df_a)
    print("################################################################################################################")

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for LEAUGE
    listLEAUGE = np_Name_of_leauge.tolist()
    listLEAUGE = remove_duplicates(listLEAUGE)
    listLEAUGE.sort()
    ###############################################################################

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for number_of_Season
    listNUMBERofSesons = np_number_of_Season.tolist()
    listNUMBERofSesons = remove_duplicates(listNUMBERofSesons)
    listNUMBERofSesons.sort()
    ###############################################################################
    #######################################################################################################################################


    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'

    while True:

        print("\n")
        print("\n\t Chose a option of proces data by State or Competition  : ")
        print("\t 1 -> LEAUGE statistic ! ")
        print("\t 2 -> NUMBER of Sesons statistic ! ")
        value = raw_input("\n\tValue between 1 and 2    : ")
        print("\n")
        if value.isdigit() == True:

            value = int(value)
            if value == 1:
                flag = 1
                ###############################################################################
                # CLUBS
                cont_LEAUGE = 0
                print("###############################################################################")
                print("\t Meni  LEAUGE statistic  !!!")
                #cont_state = 0
                for i in range(0,len(listLEAUGE)):
                    print(i+1,". : ",listLEAUGE[i])
                    cont_LEAUGE += 1
                print("###############################################################################")
                while True:

                    print("\n\t Enter Club   between 0 and ",cont_LEAUGE," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_LEAUGE:
                            print("You Chose : ",listLEAUGE[value])
                            flagTemp =  str(listLEAUGE[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\t Enter Club   between 0 and ",cont_LEAUGE," : ")
                         continue
                break
                ###############################################################################


            elif value == 2:

                flag = 2
                ###############################################################################
                cont_NUMBERofSesons = 0
                print("###############################################################################")
                print("\t Meni  State statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listNUMBERofSesons)):
                    print(i+1,". : ",listNUMBERofSesons[i])
                    cont_NUMBERofSesons += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter State   between 1 and ",cont_NUMBERofSesons," : ")
                    value = input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_NUMBERofSesons:
                            print("You Chose : ",listNUMBERofSesons[value])
                            flagTemp =  int(listNUMBERofSesons[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                          print("\n\tValue between 1 or  2  !!!")
                          continue
                break
                ###############################################################################
            else:
                print("\n\tValue between 1 or  4  !!!")
        elif value.isdigit() != True:

             print("\n\tValue between 1 or  2  !!!")
             continue
    #######################################################################################################################################

    print("flagTemp",flagTemp,"flag",flag)
    #######################################################################################################################################

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    # LEAUGE
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                bro +=1
    ###############################################################################

    # count number of rows in date frame
    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][4]) == flagTemp :
                bro +=1
    ###############################################################################

    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    array6 = [0] * bro
    array7 = [0] * bro
    array8 = [0] * bro
    array9 = [0] * bro
    array10 = [0] * bro
    array11 = [0] * bro
    array12 = [0] * bro
    array13 = [0] * bro
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from State user chose options
    y = 0
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################

    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][4]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################


    # reserving the number of elements in a row
    niz_N1 = [0]*bro
    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz1,np_niz3,np_niz3,np_niz3,np_niz2,np_niz2,np_niz2,np_niz3,np_niz3,np_niz3,np_niz3,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        new_niz[i][5] = array6[y]
        new_niz[i][6] = array7[y]
        new_niz[i][7] = array8[y]
        new_niz[i][8] = array9[y]
        new_niz[i][9] = array10[y]
        new_niz[i][10] = array11[y]
        new_niz[i][11] = array12[y]
        new_niz[i][12] = array13[y]
        y+=1
    ###############################################################################

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Name of leauge |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
     '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
     '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
    print("###################################################################################################################################################")
    print(df_new)
    print("###################################################################################################################################################")

    return df_new # function FULL optimized ~ 19.
#######################################################################################################################################

# get avg Year Season of first 25 leuge money transaction for all Leuges ,regardless of the league, therefore, only years of all seasons together
#  --> for League datas
def GetBYyear(DFrame):

    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Nationality = [0] * count
    Arrivals = [0] * count
    Season = [0] * count
    leauge = [0] * count
    niz1 = [0] *count
    Expenditures = [0] *count
    Income = [0] *count
    Balance = [0] *count
    Departures = [0] *count

    koef = [0] * count
    inter_Balance = [0] *count
    inter_Expenditures = [0] *count
    inter_Income = [0] * count
    int_koef = [0] * count
    ###############################################################################

    # cast DataFrame rows to folat and int and str
    DFrame["Expenditures"].astype(np.int64)
    DFrame["Income"].astype(np.int64)
    DFrame["Balance"].astype(np.int64)
    DFrame["Departures"].astype(np.int64)
    DFrame["Arrivals"].astype(np.int64)
    DFrame["Competition"].astype(np.str)
    DFrame["Year"].astype(np.int64)
    ###############################################################################

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Arrivals[i] = DFrame["Arrivals"][i]
        leauge[i] = DFrame["Competition"][i]
        Season[i] =  DFrame["Year"][i]
        Expenditures[i] =  DFrame["Expenditures"][i]
        Income[i] =  DFrame["Income"][i]
        Balance[i] =  DFrame["Balance"][i]
        Departures[i] =  DFrame["Departures"][i]
        ###############################################################################

    # calculation of coeficent of inflacion
    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a
        ###############################################################################

    for i in range(0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp
        ###############################################################################
    # calculation  Inflation for Potential, Earned and Profit
    for i in range(0,count):
        a = float(Balance[i])*int_koef[i]
        b = float(Expenditures[i])*int_koef[i]
        c = float(Income[i])*int_koef[i]
        inter_Balance[i] = round(a,2)
        inter_Expenditures[i] = round(b,2)
        inter_Income[i] = round(c,2)
        ###############################################################################


    npLeauge = np.asarray(leauge, dtype = 'str')
    np_Arrival = np.asarray(Arrivals, dtype ='int64')
    np_Season = np.asarray(Season, dtype = 'int64' )
    np_Expenditures = np.asarray(inter_Expenditures, dtype = 'float64' )
    np_Income = np.asarray(inter_Income, dtype = 'float64' )
    np_Balance = np.asarray(inter_Balance, dtype = 'float64' )
    np_Departures = np.asarray(Departures, dtype = 'int64' )
    ###############################################################################


    np_niz1 = np.asarray(niz1, dtype = 'str')
    np_niz2 = np.asarray(niz1, dtype = 'int64')
    np_niz3 = np.asarray(niz1, dtype = 'int64')
    np_niz4 = np.asarray(niz1, dtype = 'int64')

    #set arr to stack for operations with data lik sort and convert
    niz = np.stack((np_niz1,np_niz2,np_niz3,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4), axis = -1)
    a = np.stack((np_Arrival,npLeauge,np_Expenditures,np_Income,np_Balance,np_Departures,np_Season), axis = -1)
    ###############################################################################

    # Function for sorting
    # varibales for sorting
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
        suma_Arrival = int(a[i][0])
        sum_Expenditures = float(a[i][2])
        sum_Income = float(a[i][3])
        sum_Balance = float(a[i][4])
        sum_Departures = int(a[i][5])
        ###############################################################################
        for j in range(i + 1, n, 1):
            if (a[i][6] == a[j][6]):
                suma_Arrival += int(a[j][0])
                sum_Expenditures += float(a[j][2])
                sum_Income += float(a[j][3])
                sum_Balance += float(a[j][4])
                sum_Departures += int(a[j][5])
                visited[j] = True
                count += 1
                ###############################################################################

        if a[i][1] != 0 :
            niz[t][1] = a[i][1]
            niz[t][0] = suma_Arrival
            niz[t][2] = count
            niz[t][3] = sum_Expenditures
            niz[t][4] = sum_Income
            niz[t][5] = sum_Departures
            niz[t][6] = sum_Balance
            niz[t][7] = round(sum_Expenditures/float(suma_Arrival),2)
            niz[t][8] = round(sum_Income/float(sum_Departures),2)
            niz[t][9] = round(sum_Balance/float(sum_Departures),2)
            niz[t][10] = round(sum_Expenditures/(count),2)
            niz[t][11] = round(sum_Income/(count),2)
            niz[t][12] = round(sum_Balance/float(count),2)
            niz[t][13] = a[i][6]
            ###############################################################################

            t +=1
            suma = 0

    # count array size with N
    N =0
    for i in range(0,len(niz)):
        if int(niz[i][0]) != 0:
            N +=1


    #Initialize a new array
    niz_1 = [0] * N


    np_niz_1 = np.asarray(niz_1,dtype='str')
    np_niz_2 = np.asarray(niz_1, dtype='int64')
    np_niz_3 = np.asarray(niz_1, dtype='int64')
    np_niz_4 = np.asarray(niz_1, dtype='float64')


    new_niz = np.stack((np_niz_1,np_niz_2,np_niz_3,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4), axis = -1)

    # avg Balance number the seasons
    for i in range(0,N):
        if int(niz[i][0]) != 0:
            # int(niz[i][0]) != 0
            new_niz[i][0] = niz[i][13] # year
            new_niz[i][1] = niz[i][3] # Expend
            new_niz[i][2] = niz[i][4] # Income
            new_niz[i][3] = niz[i][6] # Balance
            new_niz[i][4] = niz[i][2] # number of seasons
            new_niz[i][5] = niz[i][0] # sum of Arrivlas of all seasons
            new_niz[i][6] = niz[i][5] # sum of Depatrues of all seasons
            new_niz[i][7] = niz[i][7] # avg Expend of Arrivlas
            new_niz[i][8] = niz[i][8] # avg Income of Depatrues
            new_niz[i][9] = niz[i][9] # avg Balance of Depatrues
            new_niz[i][10] = niz[i][10] # avg Expend number the seasons
            new_niz[i][11] = niz[i][11] # avg Income number the seasons
            new_niz[i][12] = niz[i][12] # avg Balance number the seasons
            ###############################################################################


    # sort by appropriate elements and by columns
    # cekanje na funkciju !!!!!  meni napravljen

    # convert from stack with values to data for dataFrame
    a = Input_chose_of_GetBYyear(new_niz)
    data = np.array(a)
    # set to DataFrame
    df = pd.DataFrame(data)
    # name of labels for head or names of collums
    df.columns = ['    Year |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
     '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
     '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
    ###############################################################################
    # return DataFrame with head an names of collums
    print(df)
    return df # function FULL -> BATCH  ~ 20.
#######################################################################################################################################

# BATCH for  specific filtring data from estraction data from function GetBYyear
#  --> for League datas
def BATCH_for_GetBYyear(DFrame):

    # DataFrame to ecstract data
    nDFRAME = GetBYyear(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)


    #reserving the number of elements in a row
    Year  = [0] * count # indx 0
    Expend = [0] * count # indx 1
    Income = [0] * count # indx 2
    Balance =  [0] * count # indx 3
    number_of_Season = [0] * count # indx 4
    sum_of_Arrivlas = [0] * count # indx 5
    sum_of_Depatrues = [0] * count # indx 6
    avg_Expend_of_Arrivlas = [0] * count # indx 7
    avg_Income_of_Depatrues =  [0] * count # indx 8
    avg_Balance_of_Depatrues = [0] * count # indx 9
    avg_Expend_Season = [0] * count # indx 10
    avg_Income_Season  =  [0] * count # indx 11
    avg_Balance_Season  =  [0] * count # indx 12


    # cast DataFrame rows to folat and int
    nDFRAME["    Year |  "].astype(np.int64)# ind 0
    nDFRAME["    Expend |  "].astype(np.str)# ind 1
    nDFRAME["    Income |  "].astype(np.str)# ind 2
    nDFRAME["    Balance |  "].astype(np.str)# ind 3
    nDFRAME["    number of Season |  "].astype(np.int64)# ind 4
    nDFRAME["    sum of Arrivlas |  "].astype(np.int64)# ind 5
    nDFRAME["    sum of Depatrues |  "].astype(np.int64)# ind 6
    nDFRAME["    avg Expend of Arrivlas |  "].astype(np.float64)# ind 7
    nDFRAME["    avg Income of Depatrues |  "].astype(np.float64)# ind 8
    nDFRAME["    avg Balance of Depatrues |  "].astype(np.float64)# ind 9
    nDFRAME["    avg Expend/Season |  "].astype(np.float64)# ind 10
    nDFRAME["    avg Income/Season |  "].astype(np.float64)# ind 11
    nDFRAME["    avg Balance/Season |  "].astype(np.float64)# ind 12
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Year[i] =  nDFRAME["    Year |  "][i] # indx 0
        Expend[i] = nDFRAME["    Expend |  "][i] # indx 1
        Income[i] = nDFRAME["    Income |  "][i] # indx 2
        Balance[i] = nDFRAME["    Balance |  "][i] # indx 3
        number_of_Season[i] = nDFRAME["    number of Season |  "][i] # indx 4
        sum_of_Arrivlas[i] = nDFRAME["    sum of Arrivlas |  "][i] # indx 5
        sum_of_Depatrues[i] = nDFRAME["    sum of Depatrues |  "][i] # indx 6
        avg_Expend_of_Arrivlas[i] = nDFRAME["    avg Expend of Arrivlas |  "][i] # indx 7
        avg_Income_of_Depatrues[i] = nDFRAME["    avg Income of Depatrues |  "][i] # indx 8
        avg_Balance_of_Depatrues[i] = nDFRAME["    avg Balance of Depatrues |  "][i] # indx 9
        avg_Expend_Season[i] = nDFRAME["    avg Expend/Season |  "][i] # indx 10
        avg_Income_Season[i] = nDFRAME["    avg Income/Season |  "][i] # indx 11
        avg_Balance_Season[i] = nDFRAME["    avg Balance/Season |  "][i] # indx 12
        ###############################################################################

    # conversion to numpy
    np_Year = np.asarray(Year, dtype = 'int64') # indx 0
    np_Expend = np.asarray(Expend,dtype='float64')# indx 1
    np_Income = np.asarray(Income,dtype='float64')# indx 2
    np_Balance = np.asarray(Balance, dtype = 'float64') # indx 3
    np_number_of_Season = np.asarray(number_of_Season,dtype='int64') # indx 4
    np_sum_of_Arrivlas = np.asarray(sum_of_Arrivlas, dtype ='int64') # indx 5
    np_sum_of_Depatrues = np.asarray(sum_of_Depatrues,dtype='int64') # indx 6
    np_avg_Expend_of_Arrivlas = np.asarray(avg_Expend_of_Arrivlas, dtype = 'float64' ) # indx 7
    np_avg_Income_of_Depatrues = np.asarray(avg_Income_of_Depatrues,dtype='float64') # indx 8
    np_avg_Balance_of_Depatrues = np.asarray(avg_Balance_of_Depatrues, dtype = 'float64' ) # indx 9
    np_avg_Expend_Season = np.asarray(avg_Expend_Season, dtype = 'float64' ) # indx 10
    np_avg_Income_Season = np.asarray(avg_Income_Season, dtype = 'float64' ) # indx 11
    np_avg_Balance_Season = np.asarray(avg_Balance_Season, dtype = 'float64' ) # indx 12
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Year,np_Expend,np_Income,np_Balance,np_number_of_Season,np_sum_of_Arrivlas,np_sum_of_Depatrues,
    np_avg_Expend_of_Arrivlas,np_avg_Income_of_Depatrues,np_avg_Balance_of_Depatrues,np_avg_Expend_Season,np_avg_Income_Season,np_avg_Balance_Season),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Year |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
     '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
     '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
    ###############################################################################

    print("################################################################################################################")
    print(df_a)
    print("################################################################################################################")

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for YEAR
    listYEAR = np_Year.tolist()
    listYEAR = remove_duplicates(listYEAR)
    listYEAR.sort()
    ###############################################################################


    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'

    while True:

        print("\n")
        print("\n\t Chose a option of proces data by YEAR : ")
        print("\t 1 -> YEAR ! ")
        value = raw_input("\n\tValue ")
        print("\n")
        if value.isdigit() == True:

            value = int(value)
            if value == 1:

                flag = 1
                ###############################################################################
                # drzave
                cont_YEAR = 0
                print("###############################################################################")
                print("\t Meni  State!!!")
                #cont_state = 0
                for i in range(0,len(listYEAR)):
                    print(i+1,". : ",listYEAR[i])
                    cont_YEAR += 1
                print("###############################################################################")
                while True:

                    print("\n\t Enter State   between 0 and ",cont_YEAR," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_YEAR:
                            print("You Chose : ",listYEAR[value])
                            flagTemp =  int(listYEAR[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                          print("\n\t Enter State   between 0 and ",cont_YEAR," : ")
                          continue
                break
                ###############################################################################
            else:
                print("\n\tValue :  !!!")
        elif value.isdigit() != True:

             print("\n\tValue 1 !!!")
             continue
    #######################################################################################################################################

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    # YEAR
    if flag == 1:
        for i in range(0,len(a)):
            if int(a[i][0]) == flagTemp :
                bro +=1
    ###############################################################################

    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    array6 = [0] * bro
    array7 = [0] * bro
    array8 = [0] * bro
    array9 = [0] * bro
    array10 = [0] * bro
    array11 = [0] * bro
    array12 = [0] * bro
    array13 = [0] * bro
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from State user chose options
    y = 0
    if flag == 1:
        for i in range(0,len(a)):
            if int(a[i][0]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################


    # reserving the number of elements in a row
    niz_N1 = [0]*bro
    #Initialize a new array
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz2,np_niz3,np_niz3,np_niz3,np_niz2,np_niz2,np_niz2,np_niz3,np_niz3,np_niz3,np_niz3,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        new_niz[i][5] = array6[y]
        new_niz[i][6] = array7[y]
        new_niz[i][7] = array8[y]
        new_niz[i][8] = array9[y]
        new_niz[i][9] = array10[y]
        new_niz[i][10] = array11[y]
        new_niz[i][11] = array12[y]
        new_niz[i][12] = array13[y]
        y+=1
    ###############################################################################

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Year |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
     '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
     '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
    print("###################################################################################################################################################")
    print(df_new)
    print("###################################################################################################################################################")

    return df_new # function FULL optimized ~ 21.
#######################################################################################################################################

# get data for clubs calculate inflacion for profit ,Income and Expend
#  --> for Clubs datas
def GETDataClubs_with_seasons(DFrame):

    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Order = [0] * count # 0
    Name_of_club = [0] * count # 1
    State = [0] * count # 2
    Competition =  [0] * count # 3
    Expenditures = [0] * count # 4
    Arrivals = [0] * count # 5
    Income = [0] * count # 6
    Departures = [0] * count # 7
    Balance =  [0] * count # 8
    Season = [0] * count # 9

    koef =  [0] * count
    interception_Expenditures = [0] * count
    interception_Income =  [0] * count
    interception_Balance = [0] * count
    int_koef = [0]* count
    ###############################################################################

    # cast DataFrame rows to folat and int
    DFrame["Order"].astype(np.int64) # 0
    DFrame["Club"].astype(np.str) # 1
    DFrame["State"].astype(np.str) # 2
    DFrame["Competition"].astype(np.str) # 3
    DFrame["Expenditures"].astype(np.float64) # 4
    DFrame["Arrivals"].astype(np.int64) # 5
    DFrame["Income"].astype(np.float64) # 6
    DFrame["Departures"].astype(np.int64) # 7
    DFrame["Balance"].astype(np.float64) # 8
    DFrame["Season"].astype(np.int64) # 9
    ###############################################################################


    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Order[i] = DFrame["Order"][i] # 0
        Name_of_club[i] = DFrame["Club"][i] # 1
        State[i] = DFrame["State"][i] # 2
        Competition[i] = DFrame["Competition"][i] # 3
        Expenditures[i] = DFrame["Expenditures"][i]# 4
        Arrivals[i] = DFrame["Arrivals"][i]# 5
        Income[i] = DFrame["Income"][i]# 6
        Departures[i] = DFrame["Departures"][i]# 7
        Balance[i] =  DFrame["Balance"][i]# 8
        Season[i] =  DFrame["Season"][i]# 9
        ############################################################################


    # calcualtion of coeficent for clubs seasons
    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a
        ###############################################################################

    # calculation of coeficent of inflacion
    for i in range (0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp
        ###############################################################################

    # calculation  Inflation for Potential, Earned and Profit
    for i in range(0,count):
        a = float(Income[i])*int_koef[i]
        b = float(Balance[i])*int_koef[i]
        c = float(Expenditures[i])*int_koef[i]
        interception_Income[i] = round(a,2)
        interception_Balance[i] = round(b,2)
        interception_Expenditures[i] = round(c,2)
        ###############################################################################


    # conversion to numpy
    np_Order = np.asarray(Order,dtype='int64') # 0
    np_Club = np.asarray(Name_of_club,dtype='str') # 1
    np_State = np.asarray(State,dtype='str') # 2
    np_Competition = np.asarray(Competition,dtype='str') # 3
    np_Expenditures = np.asarray(Expenditures,dtype='float64') # 4
    np_Arrivals = np.asarray(Arrivals,dtype='int64') # 5
    np_Income = np.asarray(Income,dtype='float64') # 6
    np_Departures = np.asarray(Departures,dtype='int64') # 7
    np_Balance = np.asarray(Balance,dtype='float64') # 8
    np_Seasons =  np.asarray(Season,dtype='int64') # 9

    np_INF_Income = np.asarray(interception_Income,dtype='float64') # 10
    np_INF_Balance = np.asarray(interception_Balance,dtype='float64') # 11
    np_INF_Expenditures = np.asarray(interception_Expenditures,dtype='float64') # 12
    ###############################################################################

    # set the numpy arrays values into stack
    niz = np.stack((np_Order,np_Club,np_State,np_Competition,np_Expenditures,np_Arrivals,np_Income,np_Departures,
    np_Balance,np_Seasons,np_INF_Income,np_INF_Expenditures,np_INF_Balance),axis= -1)

    # convert from stack with values to data for dataFrame
    a = Input_chose_of_sort_CLUBS_GETDataClubs_with_seasons(niz)
    # set to DataFrame
    data = np.array(a)
    # set to DataFrame
    df = pd.DataFrame(data)

    df.columns = ['    Order |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Arrivals |  ','    Income  |  ', '    Departures |  ','    Balance |  ','    Season |  ',
     ' Inflacion + Income |  ',' Inflacion + Expenditures |  ',' Inflacion + Balance |  ']
    ###############################################################################

    # return DataFrame with head an names of collums
    print(df)
    return df # function FULL -> BATCH optimized ~ 22.
#######################################################################################################################################

# BATCH for  specific filtring data from estraction data from function GETDataClubs_with_seasons
#  --> for Clubs data
def BATCH_for_GETDataClubs_with_seasons(DFrame):

    # DataFrame to ecstract data
    nDFRAME = GETDataClubs_with_seasons(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    #reserving the number of elements in a row
    Order  = [0] * count # indx 0
    Club = [0] * count # indx 1
    State = [0] * count # indx 2
    Competition =  [0] * count # indx 3
    Expenditures = [0] * count # indx 4
    Arrivals = [0] * count # indx 5
    Income = [0] * count # indx 6
    Departures = [0] * count # indx 7
    Balance =  [0] * count # indx 8
    Season = [0] * count # indx 9
    inflation_Income = [0] * count # indx 10
    inflation_Expenditures = [0] * count # indx 11
    inflation_Balance =  [0] * count # indx 12

    # cast DataFrame rows to folat and int
    nDFRAME["    Order |  "].astype(np.int64)# ind 0
    nDFRAME["    Club |  "].astype(np.str)# ind 1
    nDFRAME["    State |  "].astype(np.str)# ind 2
    nDFRAME["    Competition |  "].astype(np.str)# ind 3
    nDFRAME["    Expenditures |  "].astype(np.float64)# ind 4
    nDFRAME["    Arrivals |  "].astype(np.int64)# ind 5
    nDFRAME["    Income  |  "].astype(np.float64)# ind 6
    nDFRAME["    Departures |  "].astype(np.int64)# ind 7
    nDFRAME["    Balance |  "].astype(np.float64)# ind 8
    nDFRAME["    Season |  "].astype(np.int64)# ind 9
    nDFRAME[" Inflacion + Income |  "].astype(np.float64)# ind 10
    nDFRAME[" Inflacion + Expenditures |  "].astype(np.float64)# ind 11
    nDFRAME[" Inflacion + Balance |  "].astype(np.float64)# ind 12
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Order[i] =  nDFRAME["    Order |  "][i] # indx 0
        Club[i] = nDFRAME["    Club |  "][i] # indx 1
        State[i] = nDFRAME["    State |  "][i] # indx 2
        Competition[i] = nDFRAME["    Competition |  "][i] # indx 3
        Expenditures[i] = nDFRAME["    Expenditures |  "][i] # indx 4
        Arrivals[i] = nDFRAME["    Arrivals |  "][i] # indx 5
        Income[i] = nDFRAME["    Income  |  "][i] # indx 6
        Departures[i] = nDFRAME["    Departures |  "][i] # indx 7
        Balance[i] = nDFRAME["    Balance |  "][i] # indx 8
        Season[i] = nDFRAME["    Season |  "][i] # indx 9
        inflation_Income[i] = nDFRAME[" Inflacion + Income |  "][i] # indx 10
        inflation_Expenditures[i] = nDFRAME[" Inflacion + Expenditures |  "][i] # indx 11
        inflation_Balance[i] = nDFRAME[" Inflacion + Balance |  "][i] # indx 12
        ###############################################################################

    # conversion to numpy
    np_Order = np.asarray(Order, dtype = 'int64') # indx 0
    np_Club = np.asarray(Club,dtype='str')# indx 1
    np_State = np.asarray(State,dtype='str')# indx 2
    np_Competition = np.asarray(Competition, dtype = 'str') # indx 3
    np_Expenditures = np.asarray(Expenditures,dtype='float64') # indx 4
    np_Arrivals = np.asarray(Arrivals, dtype ='int64') # indx 5
    np_Income = np.asarray(Income,dtype='float64') # indx 6
    np_Departures = np.asarray(Departures, dtype = 'int64' ) # indx 7
    np_Balance = np.asarray(Balance,dtype='float64') # indx 8
    np_Season = np.asarray(Season,dtype='int64') # indx 9
    np_inflation_Income = np.asarray(inflation_Income, dtype = 'float64' ) # indx 10
    np_inflation_Expenditures = np.asarray(inflation_Expenditures, dtype = 'float64' ) # indx 11
    np_inflation_Balance = np.asarray(inflation_Balance, dtype = 'float64' ) # indx 12
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Order,np_Club,np_State,np_Competition,np_Expenditures,np_Arrivals,np_Income,np_Departures,np_Balance,
    np_Season,np_inflation_Income,np_inflation_Expenditures,np_inflation_Balance),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Order |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Arrivals |  ','    Income  |  ', '    Departures |  ','    Balance |  ','    Season |  ',
     ' Inflacion + Income |  ',' Inflacion + Expenditures |  ',' Inflacion + Balance |  ']
    ###############################################################################

    print("################################################################################################################")
    print(df_a)
    print("################################################################################################################")

    # CLUB
    # convert data from numpay ndarray to list and remove duplicates elemtes of list for CLUB
    listClub = np_Club.tolist()
    listClub = remove_duplicates(listClub)
    listClub.sort()

    #STATE
    # convert data from numpay ndarray to list and remove duplicates elemtes of list for STATE
    listState = np_State.tolist()
    listState = remove_duplicates(listState)
    listState.sort()
    ###############################################################################

    # COMPETITION
    # convert data from numpay ndarray to list and remove duplicates elemtes of list for CLUB
    listCOMPETITION = np_Competition.tolist()
    listCOMPETITION = remove_duplicates(listCOMPETITION)
    listCOMPETITION.sort()

    # SESAON
    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Competition
    listSESAON = np_Season.tolist()
    listSESAON = remove_duplicates(listSESAON)
    listSESAON.sort()
    ###############################################################################
    #######################################################################################################################################

    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'

    while True:

        print("\n")
        print("\n\t Chose a option of proces data by State or Competition  : ")
        print("\t 1 -> Club statistic ! ")
        print("\t 2 -> State statistic ! ")
        print("\t 3 -> Competition statistic ! ")
        print("\t 4 -> Season statistic ! ")
        value = raw_input("\n\tValue between 1 and 4    : ")
        if value.isdigit() == True:

            value = int(value)
            if value == 1:

                flag = 1
                ###############################################################################
                # CLUBS
                cont_CLUB = 0
                print("###############################################################################")
                print("\t Meni  Club statistic  !!!")
                #cont_state = 0
                for i in range(0,len(listClub)):
                    print(i+1,". : ",listClub[i])
                    cont_CLUB += 1
                print("###############################################################################")
                while True:

                    print("\n\t Enter Club   between 0 and ",cont_CLUB," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_CLUB:
                            print("You Chose : ",listClub[value])
                            flagTemp =  str(listClub[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                           print("\n\t Enter Club   between 0 and ",cont_CLUB," : ")
                           continue

                break
                ###############################################################################
            elif value == 2:

                flag = 2
                ###############################################################################
                cont_State = 0
                print("###############################################################################")
                print("\t Meni  State statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listState)):
                    print(i+1,". : ",listState[i])
                    cont_State += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter State   between 1 and ",cont_State," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_State:
                            print("You Chose : ",listState[value])
                            flagTemp =  str(listState[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                           print("\n\t Enter State   between 1 and ",cont_State," : ")
                           continue
                break
                ###############################################################################
            elif value == 3:

                flag = 3
                ###############################################################################
                cont_COMPETITION = 0
                print("###############################################################################")
                print("\t Meni  Competition statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listCOMPETITION)):
                    print(i+1,". : ",listCOMPETITION[i])
                    cont_COMPETITION += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter Competition   between 1 and ",cont_COMPETITION," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_COMPETITION:
                            print("You Chose : ",listCOMPETITION[value])
                            flagTemp =  str(listCOMPETITION[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                           print("\n\t Enter Competition   between 1 and ",cont_COMPETITION," : ")
                           continue
                break
                ###############################################################################
            elif value == 4:

                flag = 4
                ###############################################################################
                cont_Seson = 0
                print("###############################################################################")
                print("\t Meni  Season statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listSESAON)):
                    print(i+1,". : ",listSESAON[i])
                    cont_Seson += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter Season   between 1 and ",cont_Seson," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_Seson:
                            print("You Chose : ",listSESAON[value])
                            flagTemp =  int(listSESAON[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                           print("\n\t Enter Season   between 1 and ",cont_Seson," : ")
                           continue
                break
                ###############################################################################

            else:
                print("\n\tValue between 1 or  4  !!!")
        elif value.isdigit() != True:

             print("\n\tValue between 1 and 4  !!!")
             continue

    #######################################################################################################################################

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    # CLUB
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][1]) == flagTemp :
                bro +=1
    ###############################################################################
    # count number of rows in date frame
    # STATE
    if flag == 2:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                bro +=1
    ###############################################################################
    # count number of rows in date frame
    # COMPETITION
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][3]) == flagTemp :
                bro +=1
    ###############################################################################
    # count number of rows in date frame
    # SESAON
    if flag == 4:
        for i in range(0,len(a)):
            if int(a[i][9]) == flagTemp :
                bro +=1
    ###############################################################################
    #######################################################################################################################################
    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    array6 = [0] * bro
    array7 = [0] * bro
    array8 = [0] * bro
    array9 = [0] * bro
    array10 = [0] * bro
    array11 = [0] * bro
    array12 = [0] * bro
    array13 = [0] * bro
    ###############################################################################

    y = 0
    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from CLUB user chose options
    # CLUB
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][1]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from STATE user chose options
    # STATE
    if flag == 2:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from Competition user chose options
    # COMPETITION
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][3]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from Competition user chose options
    # SESAON
    if flag == 4:
        for i in range(0,len(a)):
            if int(a[i][9]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################

    # reserving the number of elements in a row
    niz_N1 = [0]*bro
    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz2,np_niz1,np_niz1,np_niz1,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        new_niz[i][5] = array6[y]
        new_niz[i][6] = array7[y]
        new_niz[i][7] = array8[y]
        new_niz[i][8] = array9[y]
        new_niz[i][9] = array10[y]
        new_niz[i][10] = array11[y]
        new_niz[i][11] = array12[y]
        new_niz[i][12] = array13[y]
        y+=1
    ###############################################################################

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Order |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Arrivals |  ','    Income  |  ', '    Departures |  ','    Balance |  ','    Season |  ',
     ' Inflacion + Income |  ',' Inflacion + Expenditures |  ',' Inflacion + Balance |  ']
    print("###################################################################################################################################################")
    print(df_new)
    print("###################################################################################################################################################")

    return df_new # function   optimized ~ 23.
#######################################################################################################################################

# get data for clubs calculate inflacion for profit ,Income and Expend but for clubs for all seasons
#  --> for Clubs data
def GetDate_for_Clubs_throught_all_seasons(DFrame):

        #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Order  = [0] * count # indx 0
    Name_of_club = [0] * count # indx 1
    State_of_club = [0] * count # indx 2
    Competition =  [0] * count # indx 3
    Expenditures = [0] * count # indx 4
    Arrivals = [0] * count # indx 5
    Income = [0] * count # indx 6
    Departures = [0] * count # indx 7
    Balance =  [0] * count # indx 8
    Season = [0] * count # ind 9
    ###############################################################################

    # optimized array for operation for counting of  inflation
    koef =  [0] * count
    interception_Expenditures = [0] * count # ind 10
    interception_Income =  [0] * count# ind 11
    interception_Balance = [0] * count# ind 12
    int_koef = [0]* count
    niz1 = [0]* count
    ###############################################################################

    # cast DataFrame rows to folat and int
    DFrame["Order"].astype(np.int64)# ind 0
    DFrame["Club"].astype(np.str)# ind 1
    DFrame["State"].astype(np.str)# ind 2
    DFrame["Competition"].astype(np.str)# ind 3
    DFrame["Expenditures"].astype(np.float64)# ind 4
    DFrame["Arrivals"].astype(np.int64)# ind 5
    DFrame["Income"].astype(np.float64)# ind 6
    DFrame["Departures"].astype(np.int64)# ind 7
    DFrame["Balance"].astype(np.float64)# ind 8
    DFrame["Season"].astype(np.int64)# ind 9
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Order[i] = DFrame["Order"][i] # indx 0
        Name_of_club[i] = DFrame["Club"][i] # indx 1
        State_of_club[i] =  DFrame["State"][i]# indx 2
        Competition[i] = DFrame["Competition"][i] # indx 3
        Expenditures[i] =  DFrame["Expenditures"][i]# indx 4
        Arrivals[i] =  DFrame["Arrivals"][i]# indx 5
        Income[i] =  DFrame["Income"][i]# indx 6
        Departures[i] =  DFrame["Departures"][i]# indx 7
        Balance[i] =  DFrame["Balance"][i]# indx 8
        Season[i] =  DFrame["Season"][i]# ind 9
        ###############################################################################

    # calcualtion of coeficent for clubs seasons
    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a

    # calculation of coeficent of inflacion
    for i in range (0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp

    # calculation  Inflation for Potential, Earned and Profit
    for i in range(0,count):

        a = float(Income[i])*int_koef[i]
        b = float(Balance[i])*int_koef[i]
        c = float(Expenditures[i])*int_koef[i]
        interception_Income[i] = round(a,2)
        interception_Balance[i] = round(b,2)
        interception_Expenditures[i] = round(c,2)
        ###############################################################################

        # conversion to numpy
    np_Order = np.asarray(Order, dtype = 'int64') # indx 0
    np_Name_of_club = np.asarray(Name_of_club,dtype='str')# indx 1
    np_State_of_club = np.asarray(State_of_club,dtype='str')# indx 2
    npLeauge = np.asarray(Competition, dtype = 'str') # indx 3
    np_Expenditures = np.asarray(Expenditures,dtype='float64') # indx 4
    np_Arrival = np.asarray(Arrivals, dtype ='int64') # indx 5
    np_Income = np.asarray(Income,dtype='float64') # indx 6
    np_Departures = np.asarray(Departures, dtype = 'int64' ) # indx 7
    np_Balance = np.asarray(Balance,dtype='float64') # indx 8
    np_Season = np.asarray(Season, dtype = 'int64' ) # indx 9
    np_in_Expenditure = np.asarray(interception_Expenditures, dtype = 'float64' ) # indx 10
    np_in_Income = np.asarray(interception_Income, dtype = 'float64' ) # indx 11
    np_in_Balance = np.asarray(interception_Balance, dtype = 'float64' ) # indx 12
    ###############################################################################


    # set the numpy arrays values into stack
    a = np.stack((np_Order,np_Name_of_club,np_State_of_club,npLeauge,np_Expenditures,np_Arrival,np_Income,
    np_Departures,np_Balance,np_Season,np_in_Expenditure,np_in_Income,np_in_Balance),axis= -1)


    np_niz1 = np.asarray(niz1, dtype = 'str')
    np_niz2 = np.asarray(niz1, dtype = 'int64')
    np_niz3 = np.asarray(niz1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    niz = np.stack((np_niz2,np_niz1,np_niz1,np_niz1,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz3,np_niz3),axis= -1)
    ###############################################################################

    # Function for sorting
    # variables in function for sorting
    n = count
    t = 0
    flag =  0

    visited = [False for i in range(n)]
    # Traverse through array elements
    # and count frequencies
    for i in range(n):
        # Skip this element if already
        # processed
        if (visited[i] == True):
            continue
        count = 1
        club = a[i][1]

        if club != 0:
            flag +=1

        suma_Arrival = int(a[i][5])
        sum_INF_Expenditures = float(a[i][10])
        sum_INF_Income = float(a[i][11])
        sum_INF_Balance = float(a[i][12])
        sum_Expenditures = float(a[i][4])
        sum_Income = float(a[i][6])
        sum_Balance = float(a[i][8])
        sum_Departures = int(a[i][7])
        ###############################################################################

        for j in range(i + 1, n, 1):
            if (a[i][1] == a[j][1]):

                suma_Arrival += int(a[j][5])
                sum_Expenditures += float(a[j][4])
                sum_Income += float(a[j][6])
                sum_Balance += float(a[j][8])
                sum_Departures += int(a[j][7])
                sum_INF_Expenditures += float(a[j][10])
                sum_INF_Income += float(a[j][11])
                sum_INF_Balance += float(a[j][12])
                visited[j] = True
                count += 1
                ###############################################################################
        if a[i][1] != 0 :
            niz[t][0] = a[i][0]
            niz[t][1] = a[i][1]
            niz[t][2] = a[i][2]
            niz[t][3] = a[i][3]
            niz[t][4] = sum_Expenditures
            niz[t][5] = suma_Arrival
            niz[t][6] = sum_Income
            niz[t][7] = sum_Departures
            niz[t][8] = sum_Balance
            niz[t][9] = a[i][9]
            niz[t][10] = sum_INF_Expenditures
            niz[t][11] = sum_INF_Income
            niz[t][12] = sum_INF_Balance
            ###############################################################################

            t +=1
            suma = 0

    # count array size with N
    # variables for flag
    N = flag
    niz_N1 = [0] * flag


    #Initialize a new array

    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz2,np_niz1,np_niz1,np_niz1,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz3,np_niz3,np_niz3),axis= -1)

    # avg Balance number the seasons
    for i in range(0,N):
        new_niz[i][0] = niz[i][0]
        new_niz[i][1] = niz[i][1]
        new_niz[i][2] = niz[i][2]
        new_niz[i][3] = niz[i][3]
        new_niz[i][4] = niz[i][4]
        new_niz[i][6] = niz[i][5]
        new_niz[i][5] = niz[i][6]
        new_niz[i][7] = niz[i][7]
        new_niz[i][8] = niz[i][8]
        #new_niz[i][9] = niz[i][9]
        new_niz[i][9] = niz[i][10]
        new_niz[i][10] = niz[i][11]
        new_niz[i][11] = niz[i][12]
        ###############################################################################

    # sort by appropriate elements and by columns
    a = Input_chose_of_sort_CLUBS(new_niz)

    # convert from stack with values to data for dataFrame
    data = np.array(a)
    # set to DataFrame
    df = pd.DataFrame(data)
    # name of labels for head or names of collums
    df.columns = ['    Order of Expend |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Income |  ','    Arrivals |  ', '    Departures |  ','    Balance |  ',
     '    inflation Expenditure |  ',' inflation Income |  ',' inflation Balance |  ']
    ###############################################################################(
    # return DataFrame with head an names of collums
    print(df)
    return df # function FULL -> BATCH optimized ~ 24.
#######################################################################################################################################

# BATCH for  specific filtring data from estraction data from function GetDate_for_Clubs_throught_all_seasons
#  --> for Clubs data
def BATCH_for_GetDate_for_Clubs_throught_all_seasons(DFrame):

    # DataFrame to ecstract data
    nDFRAME = GetDate_for_Clubs_throught_all_seasons(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)


    #reserving the number of elements in a row
    Order_of_Expend  = [0] * count # indx 0
    Club = [0] * count # indx 1
    State = [0] * count # indx 2
    Competition =  [0] * count # indx 3
    Expenditures = [0] * count # indx 4
    Income = [0] * count # indx 5
    Arrivals = [0] * count # indx 6
    Departures = [0] * count # indx 7
    Balance =  [0] * count # indx 8
    inflation_Expenditure = [0] * count # indx 9
    inflation_Income = [0] * count # indx 10
    inflation_Balance =  [0] * count # indx 11


    # cast DataFrame rows to folat and int
    nDFRAME["    Order of Expend |  "].astype(np.int64)# ind 0
    nDFRAME["    Club |  "].astype(np.str)# ind 1
    nDFRAME["    State |  "].astype(np.str)# ind 2
    nDFRAME["    Competition |  "].astype(np.str)# ind 3
    nDFRAME["    Expenditures |  "].astype(np.float64)# ind 4
    nDFRAME["    Income |  "].astype(np.float64)# ind 5
    nDFRAME["    Arrivals |  "].astype(np.int64)# ind 6
    nDFRAME["    Departures |  "].astype(np.int64)# ind 7
    nDFRAME["    Balance |  "].astype(np.float64)# ind 8
    nDFRAME["    inflation Expenditure |  "].astype(np.float64)# ind 9
    nDFRAME[" inflation Income |  "].astype(np.float64)# ind 10
    nDFRAME[" inflation Balance |  "].astype(np.float64)# ind 11
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Order_of_Expend[i] =  nDFRAME["    Order of Expend |  "][i] # indx 0
        Club[i] = nDFRAME["    Club |  "][i] # indx 1
        State[i] = nDFRAME["    State |  "][i] # indx 2
        Competition[i] = nDFRAME["    Competition |  "][i] # indx 3
        Expenditures[i] = nDFRAME["    Expenditures |  "][i] # indx 4
        Income[i] = nDFRAME["    Income |  "][i] # indx 5
        Arrivals[i] = nDFRAME["    Arrivals |  "][i] # indx 6
        Departures[i] = nDFRAME["    Departures |  "][i] # indx 7
        Balance[i] = nDFRAME["    Balance |  "][i] # indx 8
        inflation_Expenditure[i] = nDFRAME["    inflation Expenditure |  "][i] # indx 9
        inflation_Income[i] = nDFRAME[" inflation Income |  "][i] # indx 10
        inflation_Balance[i] = nDFRAME[" inflation Balance |  "][i] # indx 11
        ###############################################################################

    # conversion to numpy
    np_Order_of_Expend = np.asarray(Order_of_Expend, dtype = 'int64') # indx 0
    np_Club = np.asarray(Club,dtype='str')# indx 1
    np_State = np.asarray(State,dtype='str')# indx 2
    np_Competition = np.asarray(Competition, dtype = 'str') # indx 3
    np_Expenditures = np.asarray(Expenditures,dtype='float64') # indx 4
    np_Income = np.asarray(Income, dtype ='float64') # indx 5
    np_Arrivals = np.asarray(Arrivals,dtype='int64') # indx 6
    np_Departures = np.asarray(Departures, dtype = 'int64' ) # indx 7
    np_Balance = np.asarray(Balance,dtype='float64') # indx 8
    np_inflation_Expenditure = np.asarray(inflation_Expenditure, dtype = 'float64' ) # indx 9
    np_inflation_Income = np.asarray(inflation_Income, dtype = 'float64' ) # indx 10
    np_inflation_Balance = np.asarray(inflation_Balance, dtype = 'float64' ) # indx 11
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Order_of_Expend,np_Club,np_State,np_Competition,np_Expenditures,np_Income,np_Arrivals,np_Departures,
    np_Balance,np_inflation_Expenditure,np_inflation_Income,np_inflation_Balance),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Order of Expend |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Income |  ','    Arrivals |  ', '    Departures |  ','    Balance |  ',
     '    inflation Expenditure |  ',' inflation Income |  ',' inflation Balance |  ']
    ###############################################################################

    print("################################################################################################################")
    print(df_a)
    print("################################################################################################################")

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for states
    listSTATE = np_State.tolist()
    listSTATE = remove_duplicates(listSTATE)

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Competition
    listCompetition = np_Competition.tolist()
    listCompetition = remove_duplicates(listCompetition)
    ###############################################################################

    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'

    while True:

        print("\n")
        print("\n\t Chose a option of proces data by State or Competition  : ")
        print("\t 1 -> State ! ")
        print("\t 2 -> Competition ! ")
        value = raw_input("\n\tValue between 1 or  2  : ")
        if value.isdigit() == True:

            value = int(value)
            if value == 1:
                flag = 1
                ###############################################################################
                # drzave
                cont_state = 0
                print("###############################################################################")
                print("\t Meni  State!!!")
                #cont_state = 0
                for i in range(0,len(listSTATE)):
                    print(i+1,". : ",listSTATE[i])
                    cont_state += 1
                print("###############################################################################")
                while True:

                    print("\n\t Enter State   between 1 and ",cont_state," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_state:
                            print("You Chose : ",listSTATE[value])
                            flagTemp =  str(listSTATE[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\t Enter State   between 1 and ",cont_state," : ")
                         continue

                break
                ###############################################################################
            elif value == 2:

                flag = 2
                ###############################################################################
                cont_Compe = 0
                print("###############################################################################")
                print("\t Meni  Competition!!!")
                #cont_Compe = 0
                for i in range(0,len(listCompetition)):
                    print(i+1,". : ",listCompetition[i])
                    cont_Compe += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter Competition   between 1 and ",cont_Compe," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_Compe:
                            print("You Chose : ",listCompetition[value])
                            flagTemp =  str(listCompetition[value])
                            break
                        else:
                           print("\n\tValue between 1 and ",cont_Compe," :")
                    elif value.isdigit() != True:

                         print("\n\tValue between 1 and ",cont_Compe," :")
                         continue
                break
                ###############################################################################
            else:
                print("\n\tValue between 1 or  2  !!!")
        elif value.isdigit() != True:

             print("\n\tValue between 1 and 2 !!!")
             continue
    #######################################################################################################################################

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                bro +=1
    ###############################################################################
    # count number of rows in date frame
    if flag == 2:
        for i in range(0,len(a)):
            if str(a[i][3]) == flagTemp :
                bro +=1
    ###############################################################################
    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    array6 = [0] * bro
    array7 = [0] * bro
    array8 = [0] * bro
    array9 = [0] * bro
    array10 = [0] * bro
    array11 = [0] * bro
    array12 = [0] * bro
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from State user chose options
    y = 0
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                y+=1
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from Competition user chose options
    if flag == 2:
        for i in range(0,len(a)):
            if str(a[i][3]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                y+=1
    ###############################################################################

    # reserving the number of elements in a row
    niz_N1 = [0]*bro
    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz2,np_niz1,np_niz1,np_niz1,np_niz3,np_niz3,np_niz2,np_niz2,np_niz3,np_niz3,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        new_niz[i][5] = array6[y]
        new_niz[i][6] = array7[y]
        new_niz[i][7] = array8[y]
        new_niz[i][8] = array9[y]
        new_niz[i][9] = array10[y]
        new_niz[i][10] = array11[y]
        new_niz[i][11] = array12[y]
        y+=1
    ###############################################################################

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Order of Expend |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Income |  ','    Arrivals |  ', '    Departures |  ','    Balance |  ',
     '    inflation Expenditure |  ',' inflation Income |  ',' inflation Balance |  ']
    print("###################################################################################################################################################")
    print(df_new)
    print("###################################################################################################################################################")

    return df_new # function FULL optimized ~ 25.
#######################################################################################################################################

# a function in python that erases repeating sequence members from the array
def remove_duplicates(l):

    return list(set(l)) # function optimized ~ 26.
#######################################################################################################################################

# a function in python that release  memory for dataframes
def Delite_DataFrame_from_memory(DatFr):

    print("\n\t Release DataFrame memory !!!")
    del(DatFr) # function  ~ 27.
#######################################################################################################################################
