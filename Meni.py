import numpy as np
from functions import *



# txt FILES
koef = "/home/kristijan/github/FootballEvolcion/file.txt"
data = "/home/kristijan/github/FootballEvolcion/datas.txt"

print("\n\t Ispis koeficeijanata : ")
printFile(koef)

print("\n\t Ispis podataka : ")
printFile(data)


#print("\n\t Duljina redaka u Koef : "file_lengthy(koef),"\n\t Duljina redaka u podacima : "file_lengthy(data))

un = 0.0

un = koeficijenat(koef)
print("\n\t Koeficijent inflacije za tu godinu prema  doansnjoj vrijednosti : ",un)
