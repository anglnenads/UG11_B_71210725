def sisip(kal_awal,sisipan,index):
    index = index - 1
    hasil = f"{kal_awal[:index]}{sisipan}{kal_awal[index:]}"
    print(hasil)
    
#input
kal_awal = input("Masukkan kalimat awal : ")
sisipan = input("Masukkan kata untuk disisipkan : ")
index = int(input("Masukkan index : "))

#pemanggil fungsi
sisip(kal_awal,sisipan,index)