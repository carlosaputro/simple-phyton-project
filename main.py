import time
import random
dt = [
    ["Kevin Tanuwijaya", "Pria", 22, "Tionghoa", "ENTP", "ITB", "Teknik"],
    ["Cindy Halim", "Wanita", 20, "Tionghoa", "INFJ", "UNPAR", "Kesehatan"],
    ["Wilson Lie", "Pria", 19, "Tionghoa", "ISTJ", "ITB", "Sains"],
    ["Lydia Tan", "Wanita", 18, "Tionghoa", "ENFP", "UNPAD", "Sastra"],
    ["Budi Santoso", "Pria", 21, "Jawa", "INTJ", "ITB", "Teknik"],
    ["Sari Wulandari", "Wanita", 20, "Jawa", "ISFJ", "UNPAR", "Ekonomi"],
    ["Rizal Maulana", "Pria", 19, "Sunda", "ESTP", "UNPAD", "Kesehatan"],
    ["Nia Rahmawati", "Wanita", 18, "Sunda", "ESFP", "ITB", "Seni"],
    ["Togar Simanjuntak", "Pria", 23, "Batak", "ENTJ", "UNPAR", "Hukum"],
    ["Lestari Sihombing", "Wanita", 22, "Batak", "ISFP", "UNPAD", "Kesehatan"],
    ["Hans Gunawan", "Pria", 21, "Tionghoa", "INTP", "ITB", "Teknik"],
    ["Greta Wijaya", "Wanita", 19, "Tionghoa", "INFJ", "UNPAD", "Kesehatan"],
    ["Yonas Pattiradjawane", "Pria", 22, "Ambon", "ENFP", "UNPAR", "Seni"],
    ["Maria Niron", "Wanita", 21, "Flores", "ESFJ", "ITB", "Seni"],
    ["Alfred Tendean", "Pria", 23, "Manado", "ESTJ", "UNPAD", "Bisnis"],
    ["Isabela Langi", "Wanita", 20, "Manado", "INFP", "UNPAR", "Sastra"],
    ["Andri Putra", "Pria", 22, "Minang", "ISTP", "ITB", "Teknik"],
    ["Natalia Runtu", "Wanita", 19, "Minahasa", "ENFJ", "UNPAD", "Hukum"],
    ["Farhan Alatas", "Pria", 21, "Arab", "ENTP", "UNPAR", "Bisnis"],
    ["Layla Zahra", "Wanita", 20, "Arab", "ISFJ", "ITB", "Teknik"],
    ["Bahlil Lalahida", "Wanita", 20, "Jawa", "LPG", "UNPAR", "Bisnis"]
]


pu = [["User1","Admin123456"],["User2","Admin1001"],["User3","Password123"]] #Database username dan password
a = [0,0]
logged_in = False
while logged_in == False:
    a[0] = input("Username: ")
    a[1] = input("Password: ")
    i = 0
    while i <= len(pu)-1:
        if pu[i] == a:
            logged_in = True
            break
        else:
            logged_in = False
            print(a)
            print(pu[i])
        i += 1   
r = [0 for p in range (10)] #Menyimpan data yang nantinya diinput oleh user mengenai preferensi mereka 
yakin = 0
while yakin == 0:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nIsilah Profil dan preferensimu!\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    while r[6] == 0:
        r[6] = str(input("Nama: "))
    while r[9] == 0:
        r[9] = str(input("Asal Fakultas (Teknik/Sosial/Seni/Sastra/Bisnis/Kesehatan/Hukum): "))
    while r[7] == 0:
        r[7] = int(input("Usia:"))
        if r[7] < 18:
            print("Maaf, anda masih dibawah umur")
            exit()
    while r[0] != "Pria" and r[0] != "Wanita":
        r[0] = int(input("1. Pria\n 2. Wanita \nJenis kelamin kamu?"))
        if r[0] == 1:
            r[0] = "Wanita"
        elif r[0] == 2:
            r[0] = "Pria"
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    while r[1] == 0 or r[2] == 0:
        r[1] = int(input("Batas bawah usia yang dicari? "))
        r[2] = int(input("Batas atas usia yang dicari? "))
        if r[2] < r[1]:
            r[1],r[2] = r[2],r[1]
        if r[1] < 18:
            print("Tidak boleh mencari yang di bawah 18 tahun")
            exit()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    while r[3] == 0:
        r[3] = str(input("Ras yang dicari? (Pisahkan dengan koma jika lebih dari 1)"))
        r_m = r[3]
        r[3] = r[3].capitalize()
        r[3] = [x.strip().capitalize() for x in r[3].split(",")]
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    while r[4] == 0:
        r[4] = str(input("MBTI yang dicari? (Pisahkan dengan koma jika lebih dari 1)"))
        p_m = r[4]
        r[4] = [x.strip().upper() for x in r[4].split(",")]
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    while r[5] == 0:
        r[5] = str(input("ITB/UNPAR/UNPAD\nMau dari Universitas mana? (Pisahkan dengan koma jika lebih dari 1)"))
        u_m = r[5]
        r[5] = [x.strip().upper() for x in r[5].split(",")]
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    while r[8] == 0:
        r[8] = input("Teknik\n Sosial\n Seni\n Sastra\n Bisnis\n Kesehatan\n Hukum\n Preferensi Fakultas kamu? (Pisahkan dengan koma jika lebih dari 1)")
        f_m = r[8]
        r[8] = [x.strip().capitalize() for x in r[8].split(",")]
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Yang anda cari\n Range usia: {r[1]} - {r[2]}\n Ras: {r_m}\n MBTI: {p_m}\n Kampus: {u_m}\n Fakultas: {f_m}")
    yakin = input("Apakah anda sudah yakin? Y/N")
    if yakin == "Y" or yakin == "y":
        yakin = 1
    elif yakin == "N" or yakin == "n":
        yakin = 0
        r = [0 for p in range (10)]
    else:
        yakin = 0
        r = [0 for p in range (10)]

mul = [-1 for t in range(5)] #array untuk multiplier faktor
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
    while mul[4] < 0 or mul[4] > 1:    
        mul[4] = int(input("Masukkan faktor pengali Fakultas (per 100): "))/100
    gr = sum(mul)
    for q in range (5):
        mul[q] = (mul[q] * 1)/gr
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
jodh = 0
while jodh == 0:
    c = 0
    i = 0
    temp = 0
    jodoh = "NULL"
    while i < len(dt):
        if dt[i][2] >= r[1] and dt[i][2] <= r[2]:
            c = c + mul[0]*5
        if dt[i][3] in r[3]:
            c = c + mul[1]*5
        if dt[i][4] in r[4]:
            c = c + mul[3]*5
        if dt[i][5] in r[5]:
            c = c + mul[2]*5
        if dt[i][6] in r[8]:
            c = c + mul[4]*5
        if dt[i][1] != r[0]:
            c = 0
        if c > temp:
            temp = c
            jodoh = dt[i][0]
            profil = dt[i]
            jdh = i
        c = 0 
        i = i+1

    if jodoh == "NULL":
        print("Yah gak ada yang cocok 😞, semangat ya")
        exit()
    print("Selamat! Kamu paling cocok dengan:",jodoh+"!\nIni profilnya!\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++","\nNama:", profil[0],"\nGender:", profil[1],"\nUsia:",profil[2],"\nRas:",profil[3],"\nMBTI:",profil[4],"\nKampus:",profil[5],"\nFakultas:",profil[6],"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    confirm = str(input("Apakah anda terima? Y/N: "))
    if ((dt[jdh][6] == "Bisnis" and r[9] == "Teknik") or (dt[jdh][6] == "Teknik" and r[9] == "Bisnis")) and (confirm == "Y" or confirm == "y"):
            print("Wah, yakin nih?")
            an = input("(Y/N): ")
            if an == "N" or an == "n":
                del dt[jdh]
                jdh = 0
                confirm = "N"
            elif an == "Y" or an == "y":
                print("Oke, semangat!")
    if confirm == "Y" or confirm == "y":
        print(f"Selamat berbahagia!, {r[6]} dan {jodoh}!")
        jodh = 1
    elif confirm == "N" or confirm == "n":
        del dt[jdh]
        jdh = 0
        


