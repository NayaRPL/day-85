def soal():
    print(''' Nim D0221351
    Gaji Pokok = 5.000.000
    Gaji lembur/ jam = 1.000.000
    Lama Lembur = 30 di kurang sesuai angka terakhir  nim 
    Gaji Lembur = (gaji lembur /jam)* lama lembur
    pajak = 15%''')
jumlah_gaji_lembur= 1000000*21
gaji_kena_pajak=5000000*15/100
Gaji_kotor=5000000 + jumlah_gaji_lembur
gaji_bersih=Gaji_kotor-gaji_kena_pajak
soal()
print("gaji_kena_pajak : ",gaji_kena_pajak)
print("Gaji_kotor :",Gaji_kotor)
print("gaji_bersih:",gaji_bersih)

 
 


    