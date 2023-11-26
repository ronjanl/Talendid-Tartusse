import shlex
import subprocess
import os

kataloog = '/mambakodu/alice/resistentsed_kataloog/'

for fail in os.listdir(kataloog):
    failid = os.path.join(kataloog, fail)
    if failid.endswith(".fna"):
        ilus_nimi = failid.replace(".fna", "")
        try:
            kraken2 = [
                "/storage9/db/kraken2/kraken2",
                "--memory-mapping",
                "--threads", "8",
                "--confidence", "0.005",
                "--db", "/storage9/db/kraken2/std_2022",
                "--report", ilus_nimi + ".std2022.kreport",
                failid
            ]
            result = subprocess.Popen(kraken2, stdout=subprocess.PIPE, stderr=s$

            out, err = result.communicate()

            print("Standard Output:")
            print(out)

            print("Standard Error:")
            print(err)

            if result.returncode == 0:
                print("Process completed successfully.")
            else:
                print("Error1")
        except subprocess.CalledProcessError as e:
            print("Error:")