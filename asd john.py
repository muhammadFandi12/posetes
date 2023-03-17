from prettytable import PrettyTable


class Hotel_traveloka:
    def __init__(self, Nama, Tanggal, no_kamar):
        self.Nama = Nama
        self.Tanggal = Tanggal
        self.no_kamar = no_kamar
        self.next = None


class Hotel_travelokaLinkedList:
    def __init__(self):
        self.head = None

    def tambah_booking(self, Nama, Tanggal, no_kamar):
        new_Hotel_traveloka = Hotel_traveloka(Nama, Tanggal, no_kamar)

        if not self.head:
            self.head = new_Hotel_traveloka
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_Hotel_traveloka


    def tampilkan_pesanan(self):
        if not self.head:
            print("Tidak ada nama yang terdaftar.")
        else:
            current = self.head
            table = PrettyTable(["Nama", "Tanggal", "No kamar"])
            while current:
                table.add_row([current.Nama, current.Tanggal, current.no_kamar])
                current = current.next
            print(table)

    def cari_pesanan(self, Nama):
        current = self.head
        while current is not None:
            if current.Nama == Nama:
                return current
            current = current.next
        return None




    def hapus_pesanan(self, Nama):
        current = self.head
        if current and current.Nama == Nama:
            self.head = current.next
            current = None
            print("Pesanan berhasil dihapus")
            return
        prev = None
        while current and current.Nama != Nama:
            prev = current
            current = current.next
        if current is None:
            print("Pesanan dengan Nama tersebut tidak ditemukan.")
            return
        prev.next = current.next
        current = None
        print("Pesanan berhasil dihapus!")




def tampilan_pesanan():
    print("""
    |========================================|
    |------------DATA PESANAN HOTEL----------|
    |========================================|
    |1. Tambah pesanan                       |
    |2. Tampilkan pesanan                    |
    |3. Cari pesanan                         |
    |4. Hapus pesanan                        |
    |5. Keluar                               |
    |========================================|""")


tampilan_pesanan()
list1 = Hotel_travelokaLinkedList()

while True:
    input_menu_pesanan = input("Masukan pilihan anda: ")

    if input_menu_pesanan == "1":
        Nama = input("Masukan Nama          : ")
        Tanggal = input("Masukan Tanggal    : ")
        no_kamar = input("Masukan No kamar  : ")
        list1.tambah_booking(Nama, Tanggal, no_kamar)
        print("Data pesanan berhasil ditambahkan!")
    
    elif input_menu_pesanan == "2":
        list1.tampilkan_pesanan()

    elif input_menu_pesanan == "3":
        Nama = input("Masukan Nama yang ingin dicari: ")
        Hotel_traveloka = list1.cari_pesanan(Nama)
        if Hotel_traveloka:
            print(f"Pesanan dengan Nama {Nama} ditemukan")
            print(f"Nama : {Hotel_traveloka.Nama}")
            print(f"Tanggal : {Hotel_traveloka.Tanggal}")
            print(f"No_Kamar : {Hotel_traveloka.no_kamar}")
        else:
            print(f"Pesanan dengan Nama {Nama} tidak ditemukan.")


    elif input_menu_pesanan == "4":
        list1.tampilkan_pesanan()
        Nama = input("Masukan Nama yang ingin dihapus: ")
        Hotel_traveloka = list1.cari_pesanan(Nama)
        if Hotel_traveloka:
            list1.hapus_pesanan(Nama)
        else:
            print(f"pesanan dengan Nama {Nama} tidak ditemukan.")

    elif input_menu_pesanan == "5":
        exit()




