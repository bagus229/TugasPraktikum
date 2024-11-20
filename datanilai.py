data_mahasiswa = []

def lihat_data():
    if len(data_mahasiswa) == 0:
        print("\nDaftar Nilai")
        print("="*60)
        print("|NO |   NIM   |    NAMA    | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("="*60)
        print("|                        TIDAK ADA DATA                    |")
        print("="*60)
    else:
        print("\nDaftar Nilai")
        print("="*72)
        print("|NO |   NIM   |    NAMA    | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("="*72)
        for i, data in enumerate(data_mahasiswa, start=1):
            print(f"{i:<3}| {data['nim']:<7} | {data['nama']:<10} | {data['tugas']:<5} | {data['uts']:<5} | {data['uas']:<5} | {data['akhir']:<5.2f} |")
        print("="*72)

def tambah_data():
    print("\nTambah Data")
    nim = input("NIM         : ")
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))
    akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa.append({
        'nim': nim,
        'nama': nama,
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'akhir': akhir
    })
    print("Data berhasil ditambahkan!")

def ubah_data():
    lihat_data()
    try:
        no = int(input("\nMasukkan nomor data yang ingin diubah: ")) - 1
        if no < 0 or no >= len(data_mahasiswa):
            print("Nomor tidak valid!")
        else:
            print("\nUbah Data")
            data_mahasiswa[no]['nim'] = input("NIM         : ")
            data_mahasiswa[no]['nama'] = input("Nama        : ")
            data_mahasiswa[no]['tugas'] = float(input("Nilai Tugas : "))
            data_mahasiswa[no]['uts'] = float(input("Nilai UTS   : "))
            data_mahasiswa[no]['uas'] = float(input("Nilai UAS   : "))
            data_mahasiswa[no]['akhir'] = (data_mahasiswa[no]['tugas'] * 0.3) + \
                                           (data_mahasiswa[no]['uts'] * 0.35) + \
                                           (data_mahasiswa[no]['uas'] * 0.35)
            print("Data berhasil diubah!")
    except ValueError:
        print("Input tidak valid!")

def hapus_data():
    lihat_data()
    try:
        no = int(input("\nMasukkan nomor data yang ingin dihapus: ")) - 1
        if no < 0 or no >= len(data_mahasiswa):
            print("Nomor tidak valid!")
        else:
            del data_mahasiswa[no]
            print("Data berhasil dihapus!")
    except ValueError:
        print("Input tidak valid!")

def cari_data():
    keyword = input("\nMasukkan nama atau NIM yang dicari: ")
    hasil = [data for data in data_mahasiswa if keyword.lower() in data['nama'].lower() or keyword in data['nim']]
    if len(hasil) == 0:
        print("Data tidak ditemukan!")
    else:
        print("\nHasil Pencarian")
        print("="*60)
        print("|NO |   NIM   |    NAMA    | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("="*60)
        for i, data in enumerate(hasil, start=1):
            print(f"{i:<3}| {data['nim']:<7} | {data['nama']:<10} | {data['tugas']:<5} | {data['uts']:<5} | {data['uas']:<5} | {data['akhir']:<5.2f} |")
        print("="*60)

while True:
    print("\nProgram Input Nilai")
    print("===================")
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    menu = input("Pilih menu: ").lower()

    if menu == 'l':
        lihat_data()
    elif menu == 't':
        tambah_data()
    elif menu == 'u':
        ubah_data()
    elif menu == 'h':
        hapus_data()
    elif menu == 'c':
        cari_data()
    elif menu == 'k':
        print("Keluar dari program...")
        break
    else:
        print("Menu tidak valid!")