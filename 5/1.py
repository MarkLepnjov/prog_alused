#loeme andmed failist ja lisame ühekaupa nimekirja sisse
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
fail.close()
#kontrollime et andmed on olemas
print(vastuvõetud)
#küsime aasta kasutaja käest
aasta = int(input("Sisesta aastavahemikust [2011; 2019]: "))
print(aasta)
aastad = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
#kontrollime aasta olemasolu
if aasta in aastad:
    #on vaja teada millise indeksida antud aasta nimekirjas on
    i = aastad.index(aasta)
    #prindi sama ikdeksiga väärtus vastuvõted nimekirjast
    print("Aastas " + str(aasta) + "võeti vastu " + str(vastuvõetud[i]))