can = 5
enerji = 5
max_enerji = 10
dal = 0
yaprak = 0
meyve = 0
odun =0
taş = 0
çadır = 0
balta = 0
gün = 1
saat = 00
dakika = 00
açlık = 100

while True:
    print(f"Canın: {can}, Enerjin: {enerji}/{max_enerji} açlık: {açlık}")
    print(f"     saat: {saat}:{dakika}  gün: {gün}")
    print(" ")
    if dal > 1 and taş > 1:
        print("balta yapmak için '1 yap' yaz (5 enerji)")
    if yaprak > 50 and odun > 2 and dal > 16 and taş > 4:
        print("çadır kurmak için '2 yap' yaz. (10 enerji)")
    print("yaprak toplamak için 1 yaz. (1 enerji)")
    print("taş toplamak için 2 yaz. (2 enerji)")
    print("dal toplamak için 3 yaz. (3 enerji)")
    if balta == 1:
        print("ağaç kesmek için 4 yaz (4 enerji)")
    print("malzemelerin listesini almak için 0 yaz")
    if meyve > 0 and açlık < 100:
        print("meyve yemek için 5 yaz")

    komut = input("> ")

    if komut == "1":
        if enerji > 0:
            yaprak += 5
            enerji = enerji - 1
        else:
            print("yeterli enerjin yok. bekliyorsun...")
    elif komut == "2":
        if enerji > 1:
            taş += 10
            enerji = enerji - 2
        else:
            print("yeterli enerjin yok. bekliyorsun...")
    elif komut == "3":
        if enerji > 2:
            dal += 3
            enerji = enerji - 3
        else:
            print("yeterli enerjin yok. bekliyorsun...")
    elif komut == "0":
        print(f"dal={dal}")
        print(f"taş={taş}")
        print(f"odun={odun}")
        print(f"yaprak={yaprak}")
        print(f"meyve={meyve}")
        if balta == 1:
            print("baltan var (ağaç kesebilirsin.)")
        else:
            print("baltan yok")
        if çadır == 1:
            print("çadırın var")
        else:
            print("çadırın yok")
    elif komut == "2 yap":
        if yaprak >= 50 and odun >= 2 and dal >= 16 and taş >= 4:
            if enerji > 9:
                if çadır == 0:
                    print("çadırını kurmayı başardın")
                    çadır = 1
                    yaprak -= 50
                    odun -= 2
                    dal -= 16
                    taş -= 4
                    enerji = enerji - 10
                else:
                    print("zaten çadırın var.")
            else:
                print("yeterli enerjin yok")
        else:
            print("çadır yapmak için yeterli malzemen yok. 'hile yapma :) :) :)'")
    elif komut == "1 yap":
        if balta == 0:
                if enerji > 4:
                    if taş > 0 and dal > 0:
                        balta = 1
                        taş -= 1
                        dal -= 1
                    else:
                        print("balta yapmak için yeterli malzemen yok 'hile yapma :) :) :)'")
                else:
                    print("yeterli enerjin yok")
        else:
            print("zaten baltan var")
    
            
    elif komut == "4" and balta == 1:
        if enerji>3:   
            odun += 3
            meyve += 2
            print("ağaç kestin")
        else:
            print("enerjin yetersiz")
    elif komut == "5" and meyve > 0 and açlık < 100:
        yeme_miktarı = int(input(f"yiyeceğin miktarı seç meyven: {meyve} >"))
        if yeme_miktarı <= meyve and yeme_miktarı > 0:
            açlık += yeme_miktarı
            meyve -= yeme_miktarı
        elif yeme_miktarı < 0:
            print("yemek kusmaya mı çalışıyorsun?!")
        else:
            print(f"{yeme_miktarı} meyven yok")
    else:
        if komut != "1""2""3""4""5""6""7""8""9""1 yap""2 yap""3 yap":
            print("bekliyorsun...")
        else:
            print("yeterli enerjin ya da malzemen olmadığı İçin bekliyorsun.")

    enerji = min(enerji + 1, max_enerji)
    if komut != 0:
        dakika += 30
    if dakika == 60:
        saat += 1
        dakika = 0
    if saat == 24:
        saat = 0
    if saat == 0 and dakika == 0:
        gün += 1
    if (gün % 14 == 0 or gün % 19 == 0) and saat == 10 and dakika == 30:
        if çadır == 1:
            print("yağmur yağdı ama sen çadırın sayesinde kurtuldun!")
        else:
            can -= 1
            print("yağmur yağdı ve üşüttün  ('can - 1')")
    if açlık > 0:
        açlık -= 1
    else:
        can -= 1
        print("\033[91m!!!ölüyorsun!!!\033[0m")

    if can == 0:
        print ("oyunu kaybettin")
        break