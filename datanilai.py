data_mahasiswa = {}

def tampilkan_data():
    print("\nDaftar Nilai")
    print("="*66)
    print("|No  | NIM      | Nama       | Tugas  | UTS    | UAS    | Akhir|")
    print("="*66)
    if data_mahasiswa:
        for i, (nim, data) in enumerate(data_mahasiswa.items(), start=1):
            print(f"{i:<4}| {nim:<8} | {data['nama']:<10} | {data['tugas']:<6} | {data['uts']:<6} | {data['uas']:<6} | {data['akhir']:<5.2f}")
    else:
        print("Tidak Ada Data")
    print("="*66)

def tambah_data():
    nim = input("NIM: ")
    nama = input("Nama: ")
    try:
        tugas, uts, uas = float(input("Tugas: ")), float(input("UTS: ")), float(input("UAS: "))
        data_mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas,
                               'akhir': tugas*0.3 + uts*0.35 + uas*0.35}
        print("Data berhasil ditambahkan!")
    except ValueError:
        print("Nilai harus berupa angka!")

def ubah_data():
    nim = input("Masukkan NIM yang ingin diubah: ")
    if nim in data_mahasiswa:
        print("Data ditemukan. Masukkan data baru.")
        tambah_data()
    else:
        print("Data tidak ditemukan!")

def hapus_data():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if data_mahasiswa.pop(nim, None):
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")

def cari_data():
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        print(f"\nNIM: {nim}\nNama: {data['nama']}\nTugas: {data['tugas']}\nUTS: {data['uts']}\nUAS: {data['uas']}\nAkhir: {data['akhir']:.2f}")
    else:
        print("Data tidak ditemukan!")

def menu():
    while True:
        print("\n[L]ihat, [T]ambah, [U]bah, [H]apus, [C]ari, [K]eluar")
        pilihan = input("Pilih menu: ").lower()
        if pilihan == 'l': tampilkan_data()
        elif pilihan == 't': tambah_data()
        elif pilihan == 'u': ubah_data()
        elif pilihan == 'h': hapus_data()
        elif pilihan == 'c': cari_data()
        elif pilihan == 'k': break
        else: print("Pilihan tidak valid!")

menu()