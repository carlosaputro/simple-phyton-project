import time

dt = [
    ["David", "Pria", 22, "Yahudi", "ENTP", "ITB"],
    ["Rachel", "Wanita", 20, "Yahudi", "INFJ", "UNPAR"],
    ["Li Wei", "Pria", 19, "Cina", "ISTJ", "ITB"],
    ["Mei Ling", "Wanita", 18, "Cina", "ENFP", "UNPAD"],
    ["Budi", "Pria", 21, "Jawa", "INTJ", "ITB"],
    ["Sari", "Wanita", 20, "Jawa", "ISFJ", "UNPAR"],
    ["Rizal", "Pria", 19, "Sunda", "ESTP", "UNPAD"],
    ["Nia", "Wanita", 18, "Sunda", "ESFP", "ITB"],
    ["Togar", "Pria", 23, "Batak", "ENTJ", "UNPAR"],
    ["Lestari", "Wanita", 22, "Batak", "ISFP", "UNPAD"],
    ["Hans", "Pria", 21, "Jerman", "INTP", "ITB"],
    ["Greta", "Wanita", 19, "Jerman", "INFJ", "UNPAD"],
    ["Giovanni", "Pria", 22, "Italia", "ENFP", "UNPAR"],
    ["Lucia", "Wanita", 21, "Italia", "ESFJ", "ITB"],
    ["Alejandro", "Pria", 23, "Spanyol", "ESTJ", "UNPAD"],
    ["Isabella", "Wanita", 20, "Spanyol", "INFP", "UNPAR"],
    ["Andrei", "Pria", 22, "Rusia", "ISTP", "ITB"],
    ["Natalia", "Wanita", 19, "Rusia", "ENFJ", "UNPAD"],
    ["Farhan", "Pria", 21, "Arab", "ENTP", "UNPAR"],
    ["Layla", "Wanita", 20, "Arab", "ISFJ", "ITB"]
]  #Database

pu = [["User1","Admin123456"],["User2","Admin1001"]]
a = [0,0]
logged_in = False
while logged_in = False:
    a[0] = input("Username: ")
    a[1] = input("Password: ")
    i = 0
    while i <= len(pu):
        if pu[i] == a[0]:
            logged_in = True
            break
        else:
            logged_in = False
        i += 1   
r = [0 for p in range (6)] #Menyimpan data yang nantinya diinput oleh user mengenai preferensi mereka 
yakin = 0
while yakin == 0:
    while r[0] != "Pria" and r[0] != "Wanita":
        r[0] = int(input("1. Pria\n 2. Wanita \nJenis kelamin kamu?"))
        if r[0] == 1:
            r[0] = "Wanita"
        elif r[0] == 2:
            r[0] = "Pria"
    while r[1] == 0 or r[2] == 0:
        r[1] = int(input("Batas bawah usia yang dicari? "))
        r[2] = int(input("Batas atas usia yang dicari? "))
        if r[2] < r[1]:
            r[1],r[2] = r[2],r[1]
        if r[1] < 18:
            print("Tidak boleh mencari yang di bawah 18 tahun")
            exit()
    while r[3] == 0:
        r[3] = str(input("Ras yang dicari? (Pisahkan dengan koma jika lebih dari 1)"))
        r[3] = r[3].capitalize()
        r[3] = [x.strip().capitalize() for x in r[3].split(",")]
    while r[4] == 0:
        r[4] = str(input("MBTI yang dicari? (Pisahkan dengan koma jika lebih dari 1)"))
        r[4] = [x.strip().upper() for x in r[4].split(",")]
    while r[5] == 0:
        r[5] = str(input("ITB/UNPAR/UNPAD\nMau dari Universitas mana? (Pisahkan dengan koma jika lebih dari 1)"))
        r[5] = [x.strip().upper() for x in r[5].split(",")]

    print(f"Yang anda cari\n Range usia: {r[1]} - {r[2]}\n Ras: {r[3]}\n MBTI: {r[4]}\n Kampus: {r[5]}")
    yakin = input("Apakah anda sudah yakin? Y/N")
    if yakin == "Y" or yakin == "y":
        yakin = 1
    elif yakin == "N" or yakin == "n":
        yakin = 0
        r = [0 for p in range (6)]
    else:
        yakin = 0
        r = [0 for p in range (6)]

mul = [-1 for t in range(4)] #array untuk multiplier faktor
while round(sum(mul),0) != 1:
    print("Masukkan seberapa penting faktor-faktor ini bagi Anda! (0 sangat tidak penting, 100 sangat penting) ")
    while mul[0] < 0 or mul[0] > 1:
        mul[0] = int(input("Masukkan faktor pengali usia (per 100): "))/100
    while mul[1] < 0 or mul[1] > 1:
        mul[1] = int(input("Masukkan faktor pengali ras (per 100): "))/100
    while mul[2] < 0 or mul[2] > 1:    
        mul[2] = int(input("Masukkan faktor pengali kampus (per 100): "))/100
    while mul[3] < 0 or mul[3] > 1:    
        mul[3] = int(input("Masukkan faktor pengali MBTI (per 100): "))/100
    gr = sum(mul)
    for q in range (4):
        mul[q] = (mul[q] * 1)/gr
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
jodh = 0
while jodh == 0:
    print("Processing.....0%")
    for x in range(10,101,1):
        print("Finding jodoh.."+str(x),"%")
        time.sleep(0.01)

    c = 0
    i = 0
    temp = 0
    jodoh = "NULL"
    while i < len(dt):
        if dt[i][2] >= r[1] and dt[i][2] <= r[2]:
            c = c + mul[0]*4
        if dt[i][3] in r[3]:
            c = c + mul[1]*4
        if dt[i][1] != r[0]:
            c = 0
        if dt[i][4] in r[4]:
            c = c + mul[3]*4
        if dt[i][5] in r[5]:
            c = c + mul[2]*4
        if c > temp:
            temp = c
            jodoh = dt[i][0]
            profil = dt[i]
            jdh = i
        c = 0 
        i = i+1

    if jodoh == "NULL":
        print("Yah gak ada yang cocok 😞")

    print("Selamat! Kamu paling cocok dengan:",jodoh+"!\nIni profilnya!\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++","\nNama:", profil[0],"\nGender:", profil[1],"\nUsia:",profil[2],"\nRas:",profil[3],"\nMBTI:",profil[4],"\nKampus:",profil[5],"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    confirm = str(input("Apakah anda terima? Y/N: "))
    if confirm == "Y" or confirm == "y":
        print("Selamat berbahagia!")
        jodh = 1
    elif confirm == "N" or confirm == "n":
        del dt[jdh]
        


