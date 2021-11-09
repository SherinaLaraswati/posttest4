#1. menambahkan list multidimensi

print("------------- MENU MAKANAN ARASH CAFE -------------\n")
menu_makanan = [
    ["Kentang + chicken: Rp 20.000","Nasi + ayam penyet: Rp 16.000","Mie goreng spesial: Rp 15.000"],
    ["Seblak: Rp 15.000","Onion ring: Rp 15.000"]
]
for menu in menu_makanan:
    for makanan in menu:
        print(makanan)

print("""
=========================================================================================================================""")

#2. menambahkan menu makanan di belakang
print("------------- MENU MAKANAN ARASH CAFE -------------\n")

menu_makanan = ["Kentang + chicken: Rp 20.000","Nasi + ayam penyet: Rp 16.000","Mie goreng spesial: Rp 15.000",
    "Seblak: Rp 15.000","Onion ring: Rp 15.000"]
menu_makanan.append("Burger: Rp 10.000")
print(menu_makanan)

print("""
=========================================================================================================================""")

#3. menambahkan menu makanan dari di tengah 
print("------------- MENU MAKANAN ARASH CAFE -------------\n")
menu_makanan = ["Kentang + chicken: Rp 20.000","Nasi + ayam penyet: Rp 16.000","Mie goreng spesial: Rp 15.000",
    "Seblak: Rp 15.000","Onion ring: Rp 15.000"]
#penambahan menu makanan pada indeks 1
menu_makanan.insert(1,"Burger: Rp 10.000")
print(menu_makanan)

print("""
=========================================================================================================================""")

#4. menghapus menu makanan menggunakan dell[index]
print("------------- MENU MAKANAN ARASH CAFE -------------\n")
menu_makanan = ["Kentang + chicken: Rp 20.000","Nasi + ayam penyet: Rp 16.000","Mie goreng spesial: Rp 15.000",
    "Seblak: Rp 15.000","Onion ring: Rp 15.000"]
#penghapusan menu makanan pada indeks 2
del menu_makanan[2]
print(menu_makanan)

print("""
=========================================================================================================================""")

#5. menghapus menu makanan menggunakan remove()
print("------------- MENU MAKANAN ARASH CAFE -------------\n")
menu_makanan = ["Kentang + chicken: Rp 20.000","Nasi + ayam penyet: Rp 16.000","Mie goreng spesial: Rp 15.000",
    "Seblak: Rp 15.000","Onion ring: Rp 15.000"]
#penghapusan menu makanan Seblak Rp 15.000
menu_makanan.remove("Seblak: Rp 15.000")
print(menu_makanan)