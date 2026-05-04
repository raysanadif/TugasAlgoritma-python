# ARRAY (LIST)
data = []

# LINKED LIST
class Node:
    def __init__(self, nim, nama, ipk):  # FIX __init__
        self.nim = nim
        self.nama = nama
        self.ipk = ipk
        self.next = None

head = None

# TAMBAH DATA
def tambah():
    global head
    nim = input("NIM  : ")
    nama = input("Nama : ")
    ipk = float(input("IPK  : "))

    # ARRAY
    data.append([nim, nama, ipk])

    # LINKED LIST
    baru = Node(nim, nama, ipk)
    if head is None:
        head = baru
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = baru

    print("Data berhasil ditambahkan!\n")

# TAMPILKAN DATA
def tampil():
    print("\n=== DATA (ARRAY) ===")
    print("NIM        Nama           IPK")
    print("--------------------------------")

    if len(data) == 0:
        print("Data kosong")
    else:
        for d in data:
            print(f"{d[0]:<10} {d[1]:<15} {d[2]}")

    # LINKED LIST
    print("\n=== DATA (LINKED LIST) ===")
    temp = head
    if temp is None:
        print("Data kosong")
    else:
        while temp:
            print(f"{temp.nim:<10} {temp.nama:<15} {temp.ipk}")
            temp = temp.next
    print()

# CARI DATA
def cari():
    nim = input("Cari NIM: ")
    for d in data:
        if d[0] == nim:
            print(f"Ditemukan: NIM={d[0]}, Nama={d[1]}, IPK={d[2]}\n")
            return
    print("Data tidak ditemukan\n")

# HAPUS DATA
def hapus():
    global data, head
    nim = input("Hapus NIM: ")

    # ARRAY
    data = [d for d in data if d[0] != nim]

    # LINKED LIST
    temp = head
    prev = None
    while temp:
        if temp.nim == nim:
            if prev is None:
                head = temp.next
            else:
                prev.next = temp.next
            print("Data berhasil dihapus\n")
            return
        prev = temp
        temp = temp.next

    print("Data tidak ditemukan\n")

# SORTING (Bubble Sort)
def urutkan():
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][2] > data[j+1][2]:  # sort berdasarkan IPK
                data[j], data[j+1] = data[j+1], data[j]

    print("Data berhasil diurutkan berdasarkan IPK\n")

# REKURSI MENU
def menu():
    print("=== DATA MAHASISWA ===")
    print("1. Tambah")
    print("2. Tampilkan")
    print("3. Cari")
    print("4. Hapus")
    print("5. Urutkan (IPK)")
    print("6. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        tambah()
    elif pilih == "2":
        tampil()
    elif pilih == "3":
        cari()
    elif pilih == "4":
        hapus()
    elif pilih == "5":
        urutkan()
    elif pilih == "6":
        print("Program selesai")
        return
    else:
        print("Pilihan salah\n")

    menu()

# JALANKAN PROGRAM
menu()