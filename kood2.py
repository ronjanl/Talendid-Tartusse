with open("genome.txt", "r")as fail:

    with open("sekveneeritud", "w") as genoom:
        for rida in fail:
            values = rida.split("\t")
            id = values[0]
            genoom.write(id + "\n")