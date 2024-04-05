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

with open(aadress, "r") as f:
    print("opened")
    for line in f:
        if otsitav in line.lower():
            lugemite_list.append(line.split()[1])

print(len(lugemite_list))

aadress_fastq = "/mambakodu/mremm/talendid/test." + sys.argv[1] + ".fastq"

kirjuta_list = []

indeks = 0

"""
with open(aadress_fastq, "r") as f2:
    print("opened2")
    for line in f2:
        for lugem in lugemite_list:
            if lugem in line:
                kirjuta_list.append(line):
"""
j = 0
with open(aadress_fastq, "r") as f:
    print("opened2")
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        if any(lugem in line for lugem in lugemite_list):
            j += 1
            kirjuta_list.extend(lines[i:i+2])
            print(j//2)


print("kirjutab")

#format 
uus_string = ""
for i in otsitav:
    if i == " ":
        uus_string += "_"
        #print("oli tühik")
    else:
        uus_string += i

aadress_write = "/mambakodu/niine/resfinderisse/test." + sys.argv[1] + "_" + uus_string + ".fastq"

i = 0
with open(aadress_write, "w") as f:
    for rida in kirjuta_list:
        i += 1
        print(i//4)
        f.write(rida)

print("kood jooksis")

#jooksutamise näide: python /mambakodu/niine/krakenist_resfinderisse.py 3.6 "taxid 1280"