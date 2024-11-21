# Tugas Praktikum 5
## kode program data nilai mahasiswa

### Langkah 1
Buat dictionary kosong yang digunakan untuk menyimpan data mahasiswa. berisi antara lain nama, nim,  nilai tugas, UTS, UAS, dan nilai akhir.:
![Gambar 1](screenshot/coy1.png)

### Langkah 2
Cek apakah ada data mahasiswa yang tersedia. Jika tidak ada, menampilkan pesan "TIDAK ADA DATA".
Jika ada data, menampilkan tabel berisi NIM, nama, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir.
penggunaa  loop untuk menampilkan setiap data mahasiswa:
![Gambar 1](screenshot/coy2.png)

### Langkah 3
Tambahkan data mahaiswa dengan penggunaan tambah_data, program meminta Pengguna untuk memasukkan NIM, nama, nilai tugas, nilai UTS, dan nilai UAS. Nilai akhir akan dihitung berdasarkan ketentuan: 30% tugas + 35% uts + 35% uas. setelah data dimasukkan program akan menyimpan dalam dictionary dan ditambahkan ke dalam data_mahasiswa. Jika berhasil akan ditampilkan "data berhasil ditambahkan":
![Gambar 1](screenshot/coy3.png)

### Langkah 4
Jika kita ingin mengganti data dengan menggunakan ubah_data. Program meminta user untuk memilih nomor data yang ingin diubah. tujuan nomor itu bergunakan untuk mengakses dan mengubah data yang ada.
Data yang dipilih akan diubah sesuai (NIM, nama, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir).
Nilai akhir dihitung ulang berdasarkan ketentuan seperti pada fungsi tambah_data(). Menampilkan pesan bahwa data berhasil diubah.:
![Gambar 1](screenshot/coy4.png)

### Langkah 5
Jika kita ingin menghapus suatu data mahasiswa dengan menggunakan hapus_data. dengan melihat fungsi lihat_data() terlebih dahulu untuk menampilkan daftar data mahasiswa.
Pengguna diminta memilih nomor data yang ingin dihapus. data yang sudah dipilih akan dihapus menggunakan del. Menampilkan pesan bahwa data berhasil dihapus.:
![Gambar 1](screenshot/coy5.png)

### Langkah 6
Pengguna diminta untuk memasukkan keyword pencarian, yang bisa berupa nama atau NIM.
Program mencari data yang sesuai dengan keyword tersebut menggunakan list comprehension. Pencarian dilakukan secara case-insensitive untuk nama mahasiswa.
Jika data ditemukan, ditampilkan dalam bentuk tabel, mirip dengan fungsi lihat_data().
Jika data tidak ditemukan, menampilkan pesan "Data tidak ditemukan".:
![Gambar 1](screenshot/coy6.png)

### Langkah 7
Perulangan while, Fungsinya untuk perulangan data sampai user berhenti menggunakan, perulangan ini akan terus berjalan selama kondisi true atau tanpa henti. penggunaan elif dan if untuk menampilkan dan merubah data mahasiswa. program menampilkan "Program Input Nilai" lalu dibatasi dengan garis pemisah (===================) agar terlihat rapih, kemudian menampilkan pilihan menu dengan setiap pilihan yang dapat dilakukan oleh user:
![Gambar 1](screenshot/coy7.png)

### Hasil program
![Gambar 1](screenshot/coy8.png)
![Gambar 1](screenshot/coy9.png)

## Flowchart data nilai mahasiswa

### Langkah 1
Memulai dengan start:
![Gambar 1](screenshot/coy11.png)

### Langkah 2
Menampilkan opsi pilih menu:(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar:
![Gambar 1](screenshot/coy12.png)

### Langkah 3
Pengunaan Decision bagi penguna untuk memilih opsi pilih menuyang diinginkan:
![Gambar 1](screenshot/coy13.png)

### Langkah 4
Jika pengguna memilih tambah_data, input data berupa NIM,Nama,Nilai Tugas,UTS,UAS. setelah data diinput kemudian data akan disimpan oleh progrsm:
![Gambar 1](screenshot/coy14.png)

### Langkah 5
Pengguna memilih lihat_data, program akan menampilkan data yang telah ditambahkan. Jika tidak ada data menampilkan "Tidak Ada Data" dan jika ada data akan ditampilkan:
![Gambar 1](screenshot/coy15.png)

### Langkah 6
Jika memilih ubah_data, program akan meminta pengguna untuk mamilih data yang akan diubah. setelah diubah data akan diperbarui:
![Gambar 1](screenshot/coy16.png)

### Langkah 7
Jika memilih hapus_data, program meminta pengguna memilih data yang akan dihapus. setelah dihapups perubahan disimpan oleh sistem:
![Gambar 1](screenshot/coy17.png)

### Langkah 8
Jika pilih cari_data, pengguna meminta program untuk mencari data berdasarkan NIM dan Nama lalu tampilkan:
![Gambar 1](screenshot/coy18.png)

### Langkah 9
Program akan menampilkan Output nilai akhir data mahasiswa. jika pengguna memilih "(K)eluaar" maka program selesai:
![Gambar 1](screenshot/coy19.png)

### Langkah 10
Program berakhir:
![Gambar 1](screenshot/coy20.png)