#Atur cara menentukan penempatan kelas

nama=str(input("Masukkan nama anda:"))
markah=float(input("Masukkan markah anda"))

#Kategori kelas
if markah<=40:
    print("Anda ditempatakan di kelas Dedikasi")
elif markah<=60:
    print("Anda ditempatakan di kelas Cerdik")
elif markah<=80:
    print("Anda ditempatakan di kelas Bijak")
elif markah>80:
    print("Anda ditempatakan di kelas Amanah")
