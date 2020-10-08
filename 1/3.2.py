ringide_arv = int(input("Sisesta ringide arv: "))
ring = 1
porgandite_arv = 0
while(ring <= ringide_arv):
    print(ring)
    if(ring % 2 == 0):
        porgandite_arv = porgandite_arv + ring
        print("said" + str(ring) + " porgandid")
        print(" kokku hetkel on " + str(porgandite_arv) + "porgandeid")
    ring += 1