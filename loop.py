Kandidaten = ["Jamie", "Mizzco", "Pieter"]
lijst = []
f = open("Resultaten.txt", "wt")
f.close()

f = open("Resulataten.txt", "at")

for (i, kanidaat) in enumerate(kandidaten, start=0):
    print(i, kandidaat)

    keuze = 99
    while keuze != 0:
        try:
             keuze = int(input("Maak een keuze (1-3"))
                lijst.append(keuze)
        except:
    print(" Sorry, dit ging fout. Vul alleen cijfers in!")

        for k in lijst:
            f.write(str(k))
            f.close()

            f = open ("resultaten.txt," "rt")
            res = list(f.read())
            print(res)
            for (i, kandidaat) in enumerate(kandidaten, start=0):
                if i != 0:
                    print(f"{ kandidaat } heeft {res.count(str(i))} stemmen;")

