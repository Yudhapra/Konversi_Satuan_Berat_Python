#Yudha Prasetyo_TUGAS PRAKTIKUM MODUL 3

#Judul Program
print("\n=================================================")
print("##    Progam Konversi Satuan Berat Sederhana   ##")
print("=================================================")

#Menu Konversi
print("\n=================================================")
print("|  Pilih Konversi Satuan Berat :                |")
print("|  1. Konversi Gram ke Satuan Berat Lain        |")
print("|  2. Konversi Ons ke Satuan Berat Lain         |")
print("|  3. Konversi Kg ke Satuan Berat Lain          |")
print("|  4. Konversi Kwintal ke Satuan Berat Lain     |")
print("|  5. Konversi Ton ke Satuan Berat Lain         |")
print("=================================================")

#Input Nilai
pilih = input("\nPilih Konversi Berat : ")
print("_________________________________\n")

if  str(pilih) == '1':
    Grm = int(input("Masukan nilai berat dalam Gram : "))
    GON = Grm / 100
    GKG = Grm / 1000
    GKW = Grm / 100000
    GT = Grm / 1000000
    print("",Grm,"Gram","=",GON,"Ons\n",Grm,"Gram","=",GKG,"Kg\n",Grm,"Gram","=",GKW,"Kwintal\n",Grm,"Gram","=",GT,"Ton\n")
    
elif str(pilih) == '2':
    Ons = int(input("Masukan nilai berat dalam Ons : "))
    OG = Ons * 100
    OKG = Ons / 10
    OKW = Ons / 1000
    OT = Ons / 10000
    print("",Ons,"Ons","=",OG,"Gram\n",Ons,"Ons","=",OKG,"Kg\n",Ons,"Ons","=",OKW,"Kwintal\n",Ons,"Ons","=",OT,"Ton\n")
    
elif str(pilih) == '3':
    Kg = int(input("Masukan nilai berat dalam Kilogram : "))
    KGG = Kg * 1000
    KGO = Kg * 10
    KKW = Kg / 100
    KGT = Kg / 1000
    print("",Kg,"Kg","=",KGG,"Gram\n",Kg,"Kg","=",KGO,"Ons\n",Kg,"Kg","=",KKW,"Kwintal\n",Kg,"Kg","=",KGT,"Ton\n")

elif str(pilih) == '4':
    Kw = int(input("Masukan nilai berat dalam Kwintal : "))
    KWG = Kw * 100000
    KWO = Kw * 1000
    KKG = Kw * 100
    KWT = Kw / 10
    print("",Kw,"Kwintal","=",KWG,"Gram\n",Kw,"Kwintal","=",KWO,"Ons\n",Kw,"Kwintal","=",KKG,"Kg\n",Kw,"Kwintal","=",KWT,"Ton\n")

elif str(pilih) == '5':
    Ton = int(input("Masukan nilai berat dalam Ton: "))
    TG = Ton * 1000000
    TNS = Ton * 10000
    TKG = Ton * 1000
    TKW = Ton * 10
    print("",Ton,"Ton","=",TG,"Gram\n",Ton,"Ton","=",TNS,"Ons\n",Ton,"Ton","=",TKG,"Kg\n",Ton,"Ton","=",TKW,"Kwintal\n")

else :
    print("Input Yang Anda Masukan Salah!\nHanya Dapat Memilih Nomer 1 Sampai 5 Saja!")


