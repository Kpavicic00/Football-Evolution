import numpy as np
from functions import *



# txt FILES
koef = "/home/kristijan/github/FootballEvolcion/file.txt"
data = "/home/kristijan/github/FootballEvolcion/datas.txt"

print("\n\t Ispis koeficeijanata : ")
printFile(koef)

print("\n\t Ispis podataka : ")
printFile(data)


# deklaracija varijabli i incijalizacija

un = 0.0
string = "0.0"

# pozivi funkcija

un = Coefficients(koef)
string = str(un)


print("\n\t Koeficijent inflacije za tu godinu prema  doansnjoj vrijednosti : ",un)

#print("\n\t Duljina redaka u Koef : "file_lengthy(koef),"\n\t Duljina redaka u podacima : "file_lengthy(data))
