class DaftarNilaiMahasiswa:
    def __init__(self):
        self.daftar_nilai = {}

    def tambah(self, nama, nilai):
        self.daftar_nilai[nama] = nilai
        print(f"Data {nama} berhasil ditambahkan")

    def tampilkan(self):
        if not self.daftar_nilai:
            print("Daftar nilai kosong")
        else:
            print("Daftar Nilai Mahasiswa:")
            for nama, nilai in self.daftar_nilai.items():
                print(f"{nama}: {nilai}")

    def hapus(self, nama):
        if nama in self.daftar_nilai:
            del self.daftar_nilai[nama]
            print(f"Data {nama} berhasil dihapus")
        else:
            print(f"Data {nama} tidak ditemukan")

    def ubah(self, nama, nilai_baru):
        if nama in self.daftar_nilai:
            self.daftar_nilai[nama] = nilai_baru
            print(f"Data {nama} berhasil diubah")
        else:
            print(f"Data {nama} tidak ditemukan")

# Contoh penggunaan:
daftar_nilai_mahasiswa = DaftarNilaiMahasiswa()

# Menambah data
daftar_nilai_mahasiswa.tambah("ridho", 85)
daftar_nilai_mahasiswa.tambah("abizar", 92)
daftar_nilai_mahasiswa.tambah("denta", 78)

# Menampilkan data
daftar_nilai_mahasiswa.tampilkan()

# Mengubah data
daftar_nilai_mahasiswa.ubah("abizar", 95)
daftar_nilai_mahasiswa.tampilkan()

# Menghapus data
daftar_nilai_mahasiswa.hapus("denta")
daftar_nilai_mahasiswa.tampilkan()
