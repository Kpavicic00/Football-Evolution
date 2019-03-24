import numpy as np
# funkcije





#unosi dio za godine try catch
def unos():
    while True:
        print("\n\t Unesite godinu transakcije da bi dobili \n podatke transakcije prema trenutnom tecaju inflacije : ")
        value = input("Value between 2000 and 2018 :")
        try:
           value = int(value)
        except ValueError:
           print("Valid number, please")
           continue
        if 2000 <= value <= 2018:
           return value
           break
        else:
           print("Value between 2000 and 2018 :")

# citanje datoteka
def printFile(data):
    f = open(data, "r")
    print(f.read())

# funkcija koja vraca broj linija u fileu
def file_lengthy(fname):
    with open(fname) as f:
        for i ,j in enumerate (f):
            pass
        return i +1

# uzamnje i baratanje sa podacima u smislu koeficjenta
def koeficijenat(files):
    lenght = file_lengthy(files)

    with open(files, "r") as f:
        data = f.readlines()
    count = 0

    #rezerviranje broja elementa u nizu
    y = [0] * lenght
    k = [0] * lenght

    for line in data:
        words = line.split()

        y[count] = words[0] #spremanje podataka u niz y years
        k[count] = words[1] #spremanje podataka u niz K koeficiejnti inflacije
        count += 1

    # np_x = np.asarray(x)  # pretvorba u numpy
    np_years = np.asarray(y, dtype='int64')
    np_koef = np.asarray(k, dtype='float64')

    # unosni dio  staviti try catch izmedu intervala 2000 i 2009 te da ih mnozi sa indeksom 2019
    i = unos()
    np_specificna_koef = np_koef[np_years == i]
    print("\n\t Izabrali ste godinu :  ",i)
    return np_specificna_koef
