with open("suspectible.txt", "r")as fail:

    with open("suspectible_sorteeritud", "w") as genoom:
        for rida in fail:
            values = rida.split("\t")
            id = values[1]
            genoom.write(id + "\n")
