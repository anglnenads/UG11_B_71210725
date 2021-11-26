def hitung(an):
     tot_huruf = len(an)
     hasil = (2*tot_huruf)//3
     print(hasil)
     return(hasil)

#input
an = input("Masukkan kalimat untuk dihitung : ")

#pemanggil fungsi
hitung(an)