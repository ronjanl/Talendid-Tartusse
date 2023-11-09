with open("suspectible_sorteeritud", "r") as info_fail:
      info_read = info_fail.readlines()

with open("sekveneeritud", "r")as genoom_fail:
    genoom_read = genoom_fail.readlines()

with open("genoomide_id_suspectible_sorteeritud", "w") as genoomid_fail:
        for rida in genoom_read:
            if rida in info_read:
                uus = rida.replace('"', " ")
                genoomid_fail.write(uus)
          