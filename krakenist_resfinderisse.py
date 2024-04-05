# -*- coding: utf-8 -*-
import sys

# Accessing command-line arguments
if len(sys.argv) > 2:
    aadress = "/mambakodu/mremm/talendid/KRAKEN/test." + sys.argv[1] + "_kraken2_output.txt"
    otsitav = sys.argv[2].lower()
else:
    print("Palun lisa testi number ja otsitav.")
    exit()

lugemite_list = []

#võtab kõik vastava liigi lugemite nimed
with open(aadress, "r") as f:
    print("opened")
    for line in f:
        if otsitav in line.lower():
            lugemite_list.append(line.split()[1])

print("leiti " + str(len(lugemite_list)) + " " + otsitav + " lugemit")

aadress_fastq = "/mambakodu/mremm/talendid/test." + sys.argv[1] + ".fastq"

kirjuta_list = []

lugemeid_l2bitud = 0

#võtab fastq failist vastavate lugemite osad
with open(aadress_fastq, "r") as f:
    print("fastq fail avanes")
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        if any(lugem in line for lugem in lugemite_list):
            lugemeid_l2bitud += 1
            kirjuta_list.extend(lines[i:i+2])
            print(lugemeid_l2bitud//2)


print("kirjutab uut fastq faili")

#teeb failinime tühikuvabaks
uus_string = ""
for i in otsitav:
    if i == " ":
        uus_string += "_"
        #print("oli tühik")
    else:
        uus_string += i

aadress_write = "/mambakodu/niine/resfinderisse/test." + sys.argv[1] + "_" + uus_string + ".fastq"

i = 0
#kirjutab uue fastq faili vastava liigi jaoks
with open(aadress_write, "w") as f:
    for rida in kirjuta_list:
        i += 1
        print(i//4)
        f.write(rida)

print("valmis")

#jooksutamise näide: python /mambakodu/niine/krakenist_resfinderisse.py 3.6 "taxid 1280"
#NB! pane otsitavale jutumärgid ümber - staphylococcus aureus ilma jutumärkideta otsib staphylococcuse perekonda
