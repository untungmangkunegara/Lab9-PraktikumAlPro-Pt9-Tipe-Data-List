# Referensi Soal: UG 9 Grup C Nomor 2
# 7120619 _ Untung Mangkunegara

# Buatlah sebuah fungsi bernama pemetaan_nama_nim_umur. Fungsi ini akan memetakan 3 buah list
# yang masing-masing berisi daftar nama, daftar NIS (Nomor Induk Siswa), dan daftar
# usia. Pemetaan ini akan menghasilkan sebuah daftar siswa. 
# Input nama nim umur sesuai dengan yang di inputkan oleh user.
# output = NAMA: ....... || NIM: ......... || Umur: ........

lst_nama=[]
lst_nim=[]
lst_umur=[]

# input 
n=int(input("Banyak data yang akan dimasukkan :"))

# proses
for a in range (0,n):
    nama=input("Masukkan Nama :")
    lst_nama.append(nama)
    nim=input("Masukkan NIM :")
    lst_nim.append(nim)
    umur=input("Masukkan Umur :")
    lst_umur.append(umur)
    print("Data berhasil dimasukkan.")
    print("\n")

# proses 2
def pemetaan_nama_nim_umur(lst_nama,lst_nim,lst_umur):
    banyak_data=len(lst_nama)
    print("=====Daftar Siswa=====")
    for i in range (0,banyak_data):
        print("Nama :",lst_nama[i],"|| NIM :",lst_nim[i],"|| Umur :",lst_umur[i])

pemetaan_nama_nim_umur(lst_nama,lst_nim,lst_umur)