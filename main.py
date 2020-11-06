import numpy as np
import string

def readkamus(namafile):
    text_file = open(namafile, "r")
    lines = text_file.readlines()
    lines2 = []
    for i in lines:
        i = i.replace('\n', '')
        lines2.append(i)
    return lines2

def readstopword(namafile):
    text_file = open(namafile, "r")
    lines = text_file.readlines()
    lines2 = []
    for i in lines:
        i = i.replace('\n', '')
        lines2.append(i)
    return lines2



akhiran = ["i", "an", "kan", "ku", "mu", "nya", "lah", "kah", "tah", "pun"]
awalan = ["di","ke","se","me","be","pe", "te"]
# prefix = ['meng','per','ber','ter','di','ke','se','peng']
# suffix = ['kan','an','i']
# infix = ['el','er','em']
print("Term Loaded....")
kamus = readkamus('kata-dasar.txt')
print("Dictionary loaded....")
kamusstop = readkamus('StopWord.txt')
print("Stop Word Dictionary loaded....")
punctuation = set(string.punctuation)

kalimat = input("Masukan kalimat : ").lower()
kalimat = ''.join([i for i in kalimat if not i.isdigit()])
kalimat = ''.join(ch for ch in kalimat if ch not in punctuation)

listkalimat = [str(i) for i in kalimat.split()]
kalimatdasar = []
strkalimatdasar = ''

    # hapus stop word
listkalimat = np.array(listkalimat)
for i in kamusstop:
    listkalimat = np.delete(listkalimat, np.where(listkalimat == i))

# print(listkalimat)

for index, kata in enumerate(listkalimat):
    print("sesi kata ", kata)

    # cek langsung ke kamus
    if kata in kamus:
        print(kata, " = kata dasar murni")
        continue


    # cek akhiran
    for p in akhiran:
        if kata[-len(p):] == p and kata[:-len(p)] in kamus:
            print(kata, " = ", kata[:-len(p)], " + ", p)
            listkalimat[index] = kata[:-len(p)]
            break



    # cek awalan
    for x in awalan:
        if kata[:len(x)] == x and kata[len(x):] in kamus:
            print(kata, " = ",  x, " + ", kata[len(x):])
            listkalimat[index] = kata[len(x):]
            break


    if kata[:2] == "me":
        # print("cek men mem meng meny")
        if kata[2] == "m":
            # print("kata mem")
            if kata[3:] in kamus:
                print(kata, " = ",  "mem + ", kata[3:])
                listkalimat[index] = kata[3:]
            elif "p"+kata[3:] in kamus:
                print(kata, " = ", "mem + ", "p"+kata[3:])
                listkalimat[index] = "p"+kata[3:]
        elif kata[2:4] == "ng":
            if kata[4:] in kamus:
                print(kata, " = ", "meng + ",  kata[4:])
                listkalimat[index] = kata[4:]
            elif "k"+kata[4:] in kamus:
                print(kata, " = ", "meng + ", "k"+kata[4:])
                listkalimat[index] = "k"+kata[4:]
        elif kata[2:4] == "ny":
            if "s"+kata[4:] in kamus:
                print(kata, " = ", "meny + ", "s"+kata[4:])
                listkalimat[index] = "s"+kata[4:]
        elif kata[2] == "n":
            if kata[3:] in kamus:
                print(kata, " = ", "men + ", kata[3:])
                listkalimat[index] = kata[3:]
            elif "t" + kata[3:] in kamus:
                print(kata, " = ", "men + ", "t" + kata[3:])
                listkalimat[index] = "t" + kata[3:]

    if kata[:2] == "pe":
        if kata[2] == "r" and kata[:-2][3:] in kamus:
            print(kata, " = ", "per + ", kata[:-2][3:], "-an")
            listkalimat[index] = kata[:-2][3:]
        elif kata[2] == "n":
            if kata[3:] in kamus:
                print(kata, " = ", "pen + ", kata[3:])
                listkalimat[index] = kata[3:]
            elif "t" + kata[3:] in kamus:
                print(kata, " = ", "pen + ", "t" + kata[3:])
                listkalimat[index] = "t" + kata[3:]
            elif "s" + kata[4:] in kamus:
                print(kata, " = ", "peny + ", "s" + kata[4:])
                listkalimat[index] = "s" + kata[4:]
        elif kata[2] == "m":
            if kata[3:] in kamus:
                print(kata, " = ", "pem + ", kata[3:])
                listkalimat[index] = kata[3:]
            elif "p"+kata[3:] in kamus:
                print(kata, " = ", "pem + ", "p"+kata[3:])
                listkalimat[index] = "p"+kata[3:]


# for i in listkalimat:
#     i = penemuan_kata_dasar(i,kamus)
#     kalimatdasar.append(i)
#     strkalimatdasar = strkalimatdasar + ' ' + i


# engkaulah sang pujaan hatiku aku ingin berdua denganmu


# print("cek", any("abaktinal" in string for string in kamus))

print(listkalimat)
# print(kalimatdasar)
# print(strkalimatdasar)



# BENCHMARK WORD

# betah sebungkus senasib menginap mengasuh memberi membesuk mencinta mencaci mendidik mendengkur menggosok menghukum menjemput menjahit mengupas mengukus mempesona memukul menyapu menyatu menanam menukar melempar memasak kebawa keatas perhitungan perkantoran penukar penikam penjahit pendidik pemberi pembunuh pemikir pemotong penyiram penyabar pelamar pemakan
# sebungkus
# senasib
# menginap
# mengasuh
# memberi
# membesuk
# mencita
# mencaci
# mendidik
# mendengkur
# menggosok
# menghukum
# menjemput
# menjahit
# mengupas
# mengukus
# mempesona
# memukul
# menyapu
# menyatu
# menanam
# menukar
# melempar
# memasak
# kebawa
# keatas
# perhitungan
# perkantoran
# penukar
# penjahit
# pendidik
# pemberi
# pembunuh
# pemikir
# pemotong
# penyiram
# penyabar
# pelamar
# pemakan
