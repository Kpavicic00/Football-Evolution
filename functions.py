import numpy as np
# functions

# function for input years interval 2000 to 2018
def unos():
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

# function  count the length of lines for the required size allocation of the string
def file_lengthy(fname):
    with open(fname) as f:
        for i ,j in enumerate (f):
            pass
        return i +1

# uzmanje i baratanje sa podacima u smislu koeficjenta
def koeficijenat(files):
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
    i = unos()
    np_specific_coefficient = np_koef[np_years == i]
    print("\n\t You have chosen a year :  ",i)
    return np_specific_coefficient

# takes charge of the chosen league and the selected season and the data to be chosen

def GetData(file):
        lenght = file_lengthy(files) # count the length of lines for the required size allocation of the string

        # read from file
        with open(files, "r") as f:
            data = f.readlines()

        count = 0 # counter for arrays

        #reserving the number of elements in a row
        season_int = [0] * lenght
        order_of_league_int = [0] * lenght
        name_of_league_str = [0] * lenght
        spent_by_the_league_int = [0] * lenght
        players_come_int = [0] * lenght
        league_s_earnings_int = [0] * lenght
        the_player_gets_out_int = [0] * lenght
        total_profit_int = [0] * lenght

        for line in data: # passing through all 8 rows
            words = line.split() # a temporary variable that saves the data from the rows and parses them separately in the sequences

            #the data from each line is entered into a separate string
            season_int[count] = words[0]
            order_of_league_int[count] = words[1]
            name_of_league_str[count] = words[2]
            spent_by_the_league_int[count] = words[3]
            players_come_int[count] = words[4]
            league_s_earnings_int[count] = words[5]
            the_player_gets_out_int[count] = words[6]
            total_profit_int[count] = words[7]
            count += 1

        # conversion to numpy
        np_season_np = np.asarray(season_int, dtype = 'int64')
        np_order_of_league_np = np.asarray(order_of_league_int, dtype = 'int64')
        np_name_of_leauge = np.asarray(np_xname_of_league_str, dtype = 'str')
        np_spent_by_the_league_int = np.asarray(spent_by_the_league_int, dtype = 'int64')
        np_players_come_int = np.asarray(players_come_int, dtype = 'int64')
        np_league_s_earnings_int = np.asarray(league_s_earnings_int, dtype = 'int64')
        np_the_player_gets_out_int = np.asarray(the_player_gets_out_int, dtype = 'int64')
        np_total_profit_int = np.asarray(total_profit_int, dtype = 'int64')



        # unosni dio  staviti try catch izmedu intervala 2000 i 2009 te da ih mnozi sa indeksom 2019
        i = unos()
        np_specificna_koef = np_koef[np_years == i]
        print("\n\t Izabrali ste godinu :  ",i)
        return np_specificna_koef
