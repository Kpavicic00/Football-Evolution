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


count_1 = 0
count_3 = 0
count_5 = 0
count_7 = 0
count_9 = 0
count_11 = 0
count_13 = 0


while True:


    Meni_for_MAIN_program()
    value = raw_input("\n\tChoose option  : ")

    if value.isdigit() == True:

        value = int(value)
        if value == 1:


            if count_1 == 0:
                print("\t===========================================================")
                print("\t= You choose function => GetAVGExpendFORplayerArrivals !  =")
                print("\t===========================================================")
                leuge_DF = DataFrameFunc(fp_league)
                a_leuge_DF = GetAVGExpendFORplayerArrivals(leuge_DF)
                WriteTOcsvFILE_mult_DATAFRAMES(save_csv_Expend,a_leuge_DF)
                Delite_DataFrame_from_memory(leuge_DF)
                Delite_DataFrame_from_memory(a_leuge_DF)
                count_1 +=1

            if count_1 == 1:
                print("\t=============================================")
                print("\t = You can use this function only one  !!!  =")
                print("\t = Pleas use something else  :-)       !!!  =")
                print("\t=============================================")
                print("\n")
                continue


        elif  value == 2:
            print("\t=====================================================================")
            print("\t= You choose function => BATCH_for_GetAVGExpendFORplayerArrivals !  =")
            print("\t=====================================================================")
            leuge_DF = DataFrameFunc(fp_league)
            a_leuge_DF = BATCH_for_GetAVGExpendFORplayerArrivals(leuge_DF)
            Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF)
            Delite_DataFrame_from_memory(leuge_DF)
            Delite_DataFrame_from_memory(a_leuge_DF)

        elif  value == 3:
            if count_3 == 0:
                print("\t=============================================================")
                print("\t= You choose function => GetAVGIncomeFORplayerDepartures !  =")
                print("\t=============================================================")
                leuge_DF = DataFrameFunc(fp_league)
                a_leuge_DF = GetAVGIncomeFORplayerDepartures(leuge_DF)
                WriteTOcsvFILE_mult_DATAFRAMES(save_csv_Income,a_leuge_DF)
                Delite_DataFrame_from_memory(leuge_DF)
                Delite_DataFrame_from_memory(a_leuge_DF)
                count_3 +=1

            if count_1 == 1:
                print("\t=============================================")
                print("\t = You can use this function only one  !!!  =")
                print("\t = Pleas use something else  :-)       !!!  =")
                print("\t=============================================")
                print("\n")
                continue

        elif  value == 4:

            print("\t=====================================================================")
            print("\t= You choose function => BATCH_for_GetAVGIncomeFORplayerDepartures !  =")
            print("\t=====================================================================")
            leuge_DF = DataFrameFunc(fp_league)
            a_leuge_DF = BATCH_for_GetAVGIncomeFORplayerDepartures(leuge_DF)
            Write_multiple_DF(save_csv_Income_BATCH,a_leuge_DF)
            Delite_DataFrame_from_memory(leuge_DF)
            Delite_DataFrame_from_memory(a_leuge_DF)

        elif  value == 5:

            if count_5 == 0:
                print("\t=============================================================")
                print("\t= You choose function => GetAVGBalanceFORplayerDepartures ! =")
                print("\t=============================================================")
                leuge_DF = DataFrameFunc(fp_league)
                a_leuge_DF = GetAVGBalanceFORplayerDepartures(leuge_DF)
                WriteTOcsvFILE_mult_DATAFRAMES(save_csv_Balance,a_leuge_DF)
                Delite_DataFrame_from_memory(leuge_DF)
                Delite_DataFrame_from_memory(a_leuge_DF)
                count_5 +=1

            if count_5 == 1:
                print("\t=============================================")
                print("\t = You can use this function only one  !!!  =")
                print("\t = Pleas use something else  :-)       !!!  =")
                print("\t=============================================")
                print("\n")
                continue

        elif  value == 6:

            print("\t===========================================================================")
            print("\t= You choose function => BATCH_for_GetAVGBalanceFORplayerDepartures !     =")
            print("\t===========================================================================")
            leuge_DF = DataFrameFunc(fp_league)
            a_leuge_DF = BATCH_for_GetAVGBalanceFORplayerDepartures(leuge_DF)
            Write_multiple_DF(save_csv_Balance_BATCH,a_leuge_DF)
            Delite_DataFrame_from_memory(leuge_DF)
            Delite_DataFrame_from_memory(a_leuge_DF)

        elif  value == 7:

            if count_7 == 0:
                print("\t=============================================================")
                print("\t= You choose function => GetDataForLeauge_AVG_Seasons !     =")
                print("\t=============================================================")
                leuge_DF = DataFrameFunc(fp_league)
                a_leuge_DF = GetDataForLeauge_AVG_Seasons(leuge_DF)
                WriteTOcsvFILE_mult_DATAFRAMES(save_csv_GetDataForLeauge_AVG_Seasons,a_leuge_DF)
                Delite_DataFrame_from_memory(leuge_DF)
                Delite_DataFrame_from_memory(a_leuge_DF)
                count_7 +=1

            if count_7 == 1:
                print("\t=============================================")
                print("\t = You can use this function only one  !!!  =")
                print("\t = Pleas use something else  :-)       !!!  =")
                print("\t=============================================")
                print("\n")
                continue

        elif  value == 8:

            print("\t=======================================================================")
            print("\t= You choose function => BATCH_for_GetDataForLeauge_AVG_Seasons !     =")
            print("\t=======================================================================")
            leuge_DF = DataFrameFunc(fp_league)
            a_leuge_DF = BATCH_for_GetDataForLeauge_AVG_Seasons(leuge_DF)
            Write_multiple_DF(save_csv_GetDataForLeauge_AVG_Seasons_BATCH,a_leuge_DF)
            Delite_DataFrame_from_memory(leuge_DF)
            Delite_DataFrame_from_memory(a_leuge_DF)

        elif  value == 9:

            if count_9 == 0:
                print("\t=============================================================")
                print("\t= You choose function => GetBYyear !                        =")
                print("\t=============================================================")
                leuge_DF = DataFrameFunc(fp_league)
                a_leuge_DF = GetBYyear(leuge_DF)
                WriteTOcsvFILE_mult_DATAFRAMES(save_csv_GetBYyear,a_leuge_DF)
                Delite_DataFrame_from_memory(leuge_DF)
                Delite_DataFrame_from_memory(a_leuge_DF)
                count_9 +=1

            if count_9 == 1:
                print("\t=============================================")
                print("\t = You can use this function only one  !!!  =")
                print("\t = Pleas use something else  :-)       !!!  =")
                print("\t=============================================")
                print("\n")
                continue

        elif  value == 10:

            print("\t======================================================================")
            print("\t= You choose function => BATCH_for_GetBYyear !                        =")
            print("\t=======================================================================")
            leuge_DF = DataFrameFunc(fp_league)
            a_leuge_DF = GetBYyear(leuge_DF)
            Write_multiple_DF(save_csv_GetBYyear_BATCH,a_leuge_DF)
            Delite_DataFrame_from_memory(leuge_DF)
            Delite_DataFrame_from_memory(a_leuge_DF)

        elif  value == 11:

            if count_11 == 0:
                print("\t=============================================================")
                print("\t= You choose function => GETDataClubs_with_seasons !        =")
                print("\t=============================================================")
                clubs_DF = DataFrameFuncClubs(clubs_KONACNA)
                a_clubs_DF = GETDataClubs_with_seasons(clubs_DF)
                WriteTOcsvFILE_mult_DATAFRAMES(save_csv_GETDataClubs_with_seasons,a_clubs_DF)
                Delite_DataFrame_from_memory(clubs_DF)
                Delite_DataFrame_from_memory(a_clubs_DF)
                count_11 +=1

            if count_11 == 1:
                print("\t=============================================")
                print("\t = You can use this function only one  !!!  =")
                print("\t = Pleas use something else  :-)       !!!  =")
                print("\t=============================================")
                print("\n")
                continue

        elif  value == 12:

            print("\t=======================================================================")
            print("\t= You choose function => BATCH_for_GETDataClubs_with_seasons !        =")
            print("\t=======================================================================")
            clubs_DF = DataFrameFuncClubs(clubs_KONACNA)
            a_clubs_DF = BATCH_for_GETDataClubs_with_seasons(clubs_DF)
            Write_multiple_DF(save_csv_GETDataClubs_with_seasons_BATCH,a_clubs_DF)
            Delite_DataFrame_from_memory(clubs_DF)
            Delite_DataFrame_from_memory(a_clubs_DF)

        elif  value == 13:

            if count_13 == 0:
                print("\t=======================================================================")
                print("\t= You choose function => GetDate_for_Clubs_throught_all_seasons !     =")
                print("\t=======================================================================")
                clubs_DF = DataFrameFuncClubs(clubs_KONACNA)
                a_clubs_DF = GetDate_for_Clubs_throught_all_seasons(clubs_DF)
                WriteTOcsvFILE_mult_DATAFRAMES(save_csv_GetDate_for_Clubs_throught_all_seasons,a_clubs_DF)
                Delite_DataFrame_from_memory(clubs_DF)
                Delite_DataFrame_from_memory(a_clubs_DF)
                count_13 +=1

            if count_13 == 1:
                print("\t=============================================")
                print("\t = You can use this function only one  !!!  =")
                print("\t = Pleas use something else  :-)       !!!  =")
                print("\t=============================================")
                print("\n")
                continue

        elif  value == 14:

            print("\t=================================================================================")
            print("\t= You choose function => BATCH_for_GetDate_for_Clubs_throught_all_seasons !     =")
            print("\t=================================================================================")
            clubs_DF = DataFrameFuncClubs(clubs_KONACNA)
            a_clubs_DF = BATCH_for_GetDate_for_Clubs_throught_all_seasons(clubs_DF)
            Write_multiple_DF(save_csv_GetDate_for_Clubs_throught_all_seasons_BATCH,a_clubs_DF)
            Delite_DataFrame_from_memory(clubs_DF)
            Delite_DataFrame_from_memory(a_clubs_DF)

        elif  value == 15:

            print("\t========================")
            print("\t = END OF PROGRAM !!!  =")
            print("\t========================")
            print("\n")
            break

        else:

            print("\t=====================")
            print("\t = ERROR INPUT !!!  =")
            print("\t=====================")
            print("\n")

    elif value.isdigit() != True:

        print("\t=====================")
        print("\t = ERROR INPUT !!!  =")
        print("\t=====================")
        print("\n")
        print("\t====================================")
        print("\t=Value between 1 and 15 !!!        =")
        print("\t====================================")
        print("\n")
        Meni_for_MAIN_program()
        continue
