#kode_promo=input("Masukan kode:")
#if "STATBIS" in kode_promo:
    #print("Kode promo valid")
#else:
    #print("Kode promo invalid")
#bedanya nasted if dan elif
#perbedaanya hanya dikondisi nasted if (if dalam if)
#match n case 
#nilai=99
#match nilai:
    #case nilai if  90:
        #print("A+")

#latsol ETS
bulan=input("Bulan menginap:")
lama=int(input("Lama menginap(hari) :"))
tipe=input("Tipe kamar(Studio/Apartemen):")

tarif_studio=0
tarif_apart=0

if bulan =="Mei" or bulan == "Oktober":
    tarif_studio=500000
    tarif_apart=650000
elif bulan == "Juni" or bulan == "September":
    tarif_studio=752000
    tarif_apart=687000
elif bulan == "Juli" or bulan == "Agustus":
    tarif_studio=760000
    tarif_apart=770000
else:
    print("Bulan Not aviliable")

total_tarif=0
if tipe == "Studio" :
    total_tarif=tarif_studio*lama
    if lama>3:
        diskon=total_tarif*0.85
        total_tarif-=diskon
elif tipe == "Apartemen" :
    total_tarif=tarif_apart*lama
    if lama>3:
        diskon=total_tarif*0.85
        total_tarif-=diskon
else:
    print("Tipe kamar invalid")

if total_tarif>0:
    print(f"Total tarif: Rp{total_tarif} dengan lama {lama} hari pada bulan {bulan} tipe kamar {tipe}")

#nomor 2a
data=[2,14,2,10,5,6,2]
data =[x for x in data if data.count(x) == 2]
print(data)

#nomor 2b
kalimat="Menjadi mahasiswa yang dapat mengelola waktu dengan baik"
kata2=kalimat.split()
kata_terpanjang=""
for kata in kata2:
    if len(kata)>len(kata_terpanjang):
        kata_terpanjang=kata
print(f"output 2b : {kata_terpanjang}")

#nomor 2c
Input=["aku",13,"ok",55,"lama",10]
output=Input[1:6:2]
print(f"Ouput : {sum(output)}")
#nomor 3
data_pengiriman = (("Laptop", 2.5, "Surabaya", 35000), 
                   ("Printer", 6.0, "Jakarta", 55000), 
                   ("Monitor", 4.2, "Bandung", 45000),
                    ("Keyboard", 1.2, "Surabaya", 30000), 
                    ("Mouse", 0.5, "Jakarta", 25000) )
list_pengiriman=list(data_pengiriman) 
#nomor 3a
print(list_pengiriman[0]+list_pengiriman[3])
#nomor 3b
total_berat=list_pengiriman[1][1]+list_pengiriman[4][1]
print(f"Total berat barang (Jakarta): {total_berat}")
#nomor 3c
bandung=list(list_pengiriman[2])
bandung[3]*=int(110/100)
list_pengiriman[2]=tuple(bandung)
data_pengiriman=tuple(list_pengiriman)
print(f"Tuple: {data_pengiriman}")
    
    
#nomor 4
a, b, c=4,10,4
D=(b**2-4*a*c)**0.5
root1=(-D-b)/2*a
print(f"root1:{root1}")
root2=(D-b)/2*a
print(f"root2:{root2}")
diff=[]
for x in range(1,11):
    fx=8*x+10
    diff.append(fx)
print(diff)

#nomor 5

nama_barang = input("Masukkan nama barang: ")
jumlah = int(input("Masukkan jumlah barang: "))
satuan_awal = input("Masukkan satuan awal (pcs/lusin/kodi): ").lower()
satuan_tujuan = input("Masukkan satuan tujuan (pcs/lusin/kodi): ").lower()

# a. Konversi satuan awal ke pcs
if satuan_awal == "pcs":
    total_pcs = jumlah
elif satuan_awal == "lusin":
    total_pcs = jumlah * 12
elif satuan_awal == "kodi":
    total_pcs = jumlah * 20
else:
    print("Error: Satuan awal tidak dikenal!")

#konversi ke satuan tujuan 
if satuan_tujuan == "pcs":
        hasil = total_pcs
elif satuan_tujuan == "lusin":
        hasil = total_pcs / 12
elif satuan_tujuan == "kodi":
        hasil = total_pcs / 20
else:
    print("Error: Satuan tujuan tidak dikenal!")

print(f"{'Barang':<23}:{nama_barang}")
print(f"{'Jumlah awal':<23}:{jumlah} {satuan_awal}")
print(f"{'Total dalam pcs':<23}:{total_pcs}")
print(f"{'Konversi ke '+ satuan_tujuan:<22} : {hasil} {satuan_tujuan}")
