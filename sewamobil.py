import sqlite3
import os
import platform
from datetime import datetime, timedelta

bersihkanCmd = lambda: os.system('cls')
sesi = []

class Database:
	def __init__(self):
		self.mydb = sqlite3.connect("sewaMobil.db")
		self.mycursor = self.mydb.cursor()

class ManajemenSistem(Database):
	def __init__(self, query=None, data=None):
		Database.__init__(self)
		self.query = query
		self.data = data

	def create(self):
		self.mycursor.executemany(self.query, self.data)
		self.mydb.commit()

	def read(self):
		self.mycursor.execute(self.query)
		return self.mycursor.fetchall()

	def readSpecific(self):
		self.mycursor.execute(self.query, self.data)
		return self.mycursor.fetchall()

	def readOne(self):
		self.mycursor.execute(self.query, self.data)
		return self.mycursor.fetchone()

	def update(self):
		self.mycursor.execute(self.query, self.data)
		self.mydb.commit()

	def delete(self):
		self.mycursor.execute(self.query, self.data)
		self.mydb.commit()

class Akun(ManajemenSistem):
	__namaTabel = "tb_user"

	def __init__(self, query=None, data=None):
		ManajemenSistem.__init__(self, query, data)

	def login(self, username, password):
		self.query = f"SELECT id_user, username, nama, tipe_akun FROM {self.__namaTabel} WHERE username = ? AND password = ?"
		self.data = (username, password)

		hasil = self.readOne()

		bersihkanCmd()

		if(hasil):
			sesi.append(hasil)
		else:
			print("Username atau password salah")

		return hasil

	def register(self, data):
		self.query = f"INSERT INTO {self.__namaTabel} (username, password, nama, tipe_akun) VALUES (?, ?, ?, ?)"
		self.data = data

		self.create()
		print("Berhasil mendaftar")

class Peraturan(ManajemenSistem):
	__namaTabel = "tb_peraturan"

	def __init__(self, query=None, data=None):
		ManajemenSistem.__init__(self, query, data)

	def input(self, data):
		self.query = f"INSERT INTO {self.__namaTabel} (isi_peraturan) VALUES (?)"
		self.data = data

		self.create()
		print("Berhasil menginput data")

	def ambil(self):
		self.query = f"SELECT * FROM {self.__namaTabel}"
		hasil = self.read()

		if(hasil):
			print("=== Peraturan ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][1]} (ID: {hasil[x][0]})")
		else:
			print("=== Peraturan ===")
			print("Tidak ada data")

		return hasil

	def ambilUser(self):
		self.query = f"SELECT * FROM {self.__namaTabel}"
		hasil = self.read()

		if(hasil):
			print("=== Peraturan ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][1]}")
		else:
			print("=== Peraturan ===")
			print("Tidak ada peraturan saat ini")

		return hasil

	def ambilSatu(self, inputan):
		self.query = f"SELECT * FROM {self.__namaTabel} where id_peraturan = ?"
		self.data = (inputan,)

		return self.readOne()

	def ubah(self, inputan):
		self.query = f"UPDATE {self.__namaTabel} SET isi_peraturan = ? WHERE id_peraturan = ?"
		self.data = inputan

		self.update()
		print("Berhasil mengubah data")

	def hapus(self, inputan):
		self.query = f"DELETE FROM {self.__namaTabel} WHERE id_peraturan = ?"
		self.data = (inputan,)

		self.delete()
		print("Berhasil menghapus data")

class Jenis(ManajemenSistem):
	__namaTabel = "tb_jenis"

	def __init__(self, query=None, data=None):
		ManajemenSistem.__init__(self, query, data)

	def input(self, data):
		self.query = f"INSERT INTO {self.__namaTabel} (nama_jenis) VALUES (?)"
		self.data = data

		self.create()
		print("Berhasil menginput data")

	def ambil(self):
		self.query = f"SELECT * FROM {self.__namaTabel}"
		hasil = self.read()

		if(hasil):
			print("=== Jenis Kendaraan ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][1]} (ID: {hasil[x][0]})")
		else:
			print("=== Jenis Kendaraan ===")
			print("Tidak ada data")

		return hasil

	def ambilSatu(self, inputan):
		self.query = f"SELECT * FROM {self.__namaTabel} where id_jenis = ?"
		self.data = (inputan,)

		return self.readOne()

	def ubah(self, inputan):
		self.query = f"UPDATE {self.__namaTabel} SET nama_jenis = ? WHERE id_jenis = ?"
		self.data = inputan

		self.update()
		print("Berhasil mengubah data")

	def hapus(self, inputan):
		self.query = f"DELETE FROM {self.__namaTabel} WHERE id_jenis = ?"
		self.data = (inputan,)

		self.delete()
		print("Berhasil menghapus data")

class Merk(ManajemenSistem):
	__namaTabel = "tb_merk"

	def __init__(self, query=None, data=None):
		ManajemenSistem.__init__(self, query, data)

	def input(self, data):
		self.query = f"INSERT INTO {self.__namaTabel} (nama_merk) VALUES (?)"
		self.data = data

		self.create()
		print("Berhasil menginput data")

	def ambil(self):
		self.query = f"SELECT * FROM {self.__namaTabel}"
		hasil = self.read()

		if(hasil):
			print("=== Merk ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][1]} (ID: {hasil[x][0]})")
		else:
			print("=== Merk ===")
			print("Tidak ada data")

		return hasil

	def ambilSatu(self, inputan):
		self.query = f"SELECT * FROM {self.__namaTabel} where id_merk = ?"
		self.data = (inputan,)

		return self.readOne()

	def ubah(self, inputan):
		self.query = f"UPDATE {self.__namaTabel} SET nama_merk = ? WHERE id_merk = ?"
		self.data = inputan

		self.update()
		print("Berhasil mengubah data")

	def hapus(self, inputan):
		self.query = f"DELETE FROM {self.__namaTabel} WHERE id_merk = ?"
		self.data = (inputan,)

		self.delete()
		print("Berhasil menghapus data")

class Kendaraan(ManajemenSistem):
	__namaTabel = "tb_kendaraan"
	__join1 = "tb_merk"
	__join2 = "tb_jenis"

	def __init__(self, query=None, data=None):
		ManajemenSistem.__init__(self, query, data)

	def input(self, data):
		self.query = f"INSERT INTO {self.__namaTabel} (id_merk, id_jenis, nama_kendaraan) VALUES (?, ?, ?)"
		self.data = data

		self.create()
		print("Berhasil menginput data")

	def ambil(self):
		self.query = f"SELECT a.id_kendaraan, b.nama_merk, c.nama_jenis, a.nama_kendaraan FROM {self.__namaTabel} a INNER JOIN {self.__join1} b using(id_merk) INNER JOIN {self.__join2} c using(id_jenis)"
		hasil = self.read()

		if(hasil):
			print("=== Kendaraan ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][3]} (ID: {hasil[x][0]} | Merk: {hasil[x][1]} | Jenis: {hasil[x][2]})")
		else:
			print("=== Kendaraan ===")
			print("Tidak ada data")

		return hasil

	def ambilSatu(self, inputan):
		self.query = f"SELECT * FROM {self.__namaTabel} WHERE id_kendaraan = ?"
		self.data = (inputan,)

		return self.readOne()

	def ubah(self, inputan):
		self.query = f"UPDATE {self.__namaTabel} SET id_merk = ?, id_jenis = ?, nama_kendaraan = ? WHERE id_kendaraan = ?"
		self.data = inputan

		self.update()
		print("Berhasil mengubah data")

	def hapus(self, inputan):
		self.query = f"DELETE FROM {self.__namaTabel} WHERE id_kendaraan = ?"
		self.data = (inputan,)

		self.delete()
		print("Berhasil menghapus data")

class Waktu(ManajemenSistem):
	__namaTabel = "tb_waktu_sewa"

	def __init__(self, query=None, data=None):
		ManajemenSistem.__init__(self, query, data)

	def input(self, data):
		self.query = f"INSERT INTO {self.__namaTabel} (durasi, harga) VALUES (?, ?)"
		self.data = data

		self.create()
		print("Berhasil menginput data")

	def ambil(self):
		self.query = f"SELECT * FROM {self.__namaTabel}"
		hasil = self.read()

		if(hasil):
			print("=== Durasi ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][1]} hari (ID: {hasil[x][0]} | Harga: Rp {hasil[x][2]})")
		else:
			print("=== Durasi ===")
			print("Tidak ada data")

		return hasil

	def ambilSatu(self, inputan):
		self.query = f"SELECT * FROM {self.__namaTabel} where id_waktu = ?"
		self.data = (inputan,)

		return self.readOne()

	def ubah(self, inputan):
		self.query = f"UPDATE {self.__namaTabel} SET durasi = ?, harga = ? WHERE id_waktu = ?"
		self.data = inputan

		self.update()
		print("Berhasil mengubah data")

	def hapus(self, inputan):
		self.query = f"DELETE FROM {self.__namaTabel} WHERE id_waktu = ?"
		self.data = (inputan,)

		self.delete()
		print("Berhasil menghapus data")

class Sewa(ManajemenSistem):
	__namaTabel = "tb_sewa"
	__join1 = "tb_kendaraan"
	__join2 = "tb_waktu_sewa"
	__join3 = "tb_user"

	def __init__(self, query=None, data=None):
		ManajemenSistem.__init__(self, query, data)

	def input(self, data):
		self.query = f"INSERT INTO {self.__namaTabel} (id_kendaraan, id_waktu, id_user, tanggal_pinjam, tanggal_kembali, status_peminjaman) VALUES (?, ?, ?, ?, ?, ?)"
		self.data = data

		self.create()
		print("Berhasil melakukan pemesanan")

	def ambil(self):
		self.query = f"SELECT a.id_sewa, b.nama_kendaraan, c.durasi, d.nama, a.tanggal_pinjam, a.tanggal_kembali, a.status_peminjaman, c.harga FROM {self.__namaTabel} a INNER JOIN {self.__join1} b using(id_kendaraan) INNER JOIN {self.__join2} c using(id_waktu) INNER JOIN {self.__join3} d using(id_user)"
		hasil = self.read()

		if(hasil):
			print("=== Riwayat Transaksi ===")	
			for x in range(0, len(hasil)):		
				if(hasil[x][6] == "1"):
					status = "Sudah Bayar"
				else:
					status = "Belum Bayar"

				print(f"{x+1}. (ID: {hasil[x][0]}) {hasil[x][3]} | Kendaraan: {hasil[x][1]} | Durasi: {hasil[x][2]} hari (Rp {hasil[x][7]}) | Tanggal Pinjam: {hasil[x][4]} | Tanggal Kembali: {hasil[x][5]} | Status: {status}")
		else:
			print("=== Riwayat Transaksi ===")
			print("Tidak ada data")

		return hasil

	def ambilSatu(self, inputan):
		self.query = f"SELECT a.id_sewa, a.id_kendaraan, b.harga, a.id_user, a.tanggal_pinjam, a.tanggal_kembali, a.status_peminjaman FROM {self.__namaTabel} a INNER JOIN {self.__join2} b using(id_waktu) WHERE id_sewa = ?"
		self.data = (inputan,)

		return self.readOne()

	def ambilTransaksiUser(self, inputan):
		self.query = f"SELECT a.id_sewa, b.nama_kendaraan, c.durasi, d.nama, a.tanggal_pinjam, a.tanggal_kembali, a.status_peminjaman, c.harga FROM {self.__namaTabel} a INNER JOIN {self.__join1} b using(id_kendaraan) INNER JOIN {self.__join2} c using(id_waktu) INNER JOIN {self.__join3} d using(id_user) WHERE id_user = ?"
		self.data = (inputan,)

		hasil = self.readSpecific()

		if(hasil):
			print("=== Riwayat Transaksi ===")	
			for x in range(0, len(hasil)):		
				if(hasil[x][6] == "1"):
					status = "Sudah Bayar"
				else:
					status = "Belum Bayar"

				print(f"{x+1}. (ID: {hasil[x][0]}) {hasil[x][3]} | Kendaraan: {hasil[x][1]} | Durasi: {hasil[x][2]} hari (Rp {hasil[x][7]}) | Tanggal Pinjam: {hasil[x][4]} | Tanggal Kembali: {hasil[x][5]} | Status: {status}")
		else:
			print("Tidak ada data")

		return hasil

	def prosesTransfer(self, inputan):
		self.query = "UPDATE tb_sewa SET status_peminjaman = ? WHERE id_sewa = ?"
		self.data = inputan

		self.update()
		print("Berhasil mengubah status")

	def prosesCash(self, inputan):
		self.query = "UPDATE tb_sewa SET status_peminjaman = ? WHERE id_sewa = ?"
		self.data = inputan

		self.update()
		print("Berhasil mengubah status")

	def hapus(self, inputan):
		self.query = f"DELETE FROM {self.__namaTabel} WHERE id_sewa = ?"
		self.data = (inputan,)

		self.delete()
		print("Berhasil menghapus data")

def peraturan():
	print("=========")
	print("Peraturan")
	print("=========")
	print("1. Tambah\n2. Tampilkan\n3. Ubah\n4. Hapus")
	menu = int(input("Pilih Menu: "))

	bersihkanCmd()

	if(menu == 1):
		data = []
		banyak_data = int(input("Masukkan banyak data yang akan diinput: "))

		for x in range(0, banyak_data):
			print(f"===== Peraturan #{x+1} =====")
			input1 = input("Input peraturan: ")

			data.append((input1,))

		bersihkanCmd()
		Peraturan().input(data)
	elif(menu == 2):
		Peraturan().ambil()
	elif(menu == 3):
		cek_data = Peraturan().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau diubah: "))
			data_ada = Peraturan().ambilSatu(inputan)

			if(data_ada):
				input1 = input("Input peraturan: ")

				data = (input1, inputan)

				bersihkanCmd()
				Peraturan().ubah(data)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	elif(menu == 4):
		cek_data = Peraturan().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau dihapus: "))
			data_ada = Peraturan().ambilSatu(inputan)

			if(data_ada):
				bersihkanCmd()
				Peraturan().hapus(inputan)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	else:
		pass

def jenisKendaraan():
	print("===============")
	print("Jenis Kendaraan")
	print("===============")
	print("1. Tambah\n2. Tampilkan\n3. Ubah\n4. Hapus")
	menu = int(input("Pilih Menu: "))

	bersihkanCmd()

	if(menu == 1):
		data = []
		banyak_data = int(input("Masukkan banyak data yang akan diinput: "))

		for x in range(0, banyak_data):
			print(f"===== Jenis #{x+1} =====")
			input1 = input("Input nama jenis: ")

			data.append((input1,))

		bersihkanCmd()
		Jenis().input(data)
	elif(menu == 2):
		Jenis().ambil()
	elif(menu == 3):
		cek_data = Jenis().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau diubah: "))
			data_ada = Jenis().ambilSatu(inputan)

			if(data_ada):
				input1 = input("Input nama jenis: ")

				data = (input1, inputan)

				bersihkanCmd()
				Jenis().ubah(data)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	elif(menu == 4):
		cek_data = Jenis().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau dihapus: "))
			data_ada = Jenis().ambilSatu(inputan)

			if(data_ada):
				bersihkanCmd()
				Jenis().hapus(inputan)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	else:
		pass

def merk():
	print("====")
	print("Merk")
	print("====")
	print("1. Tambah\n2. Tampilkan\n3. Ubah\n4. Hapus")
	menu = int(input("Pilih Menu: "))

	bersihkanCmd()

	if(menu == 1):
		data = []
		banyak_data = int(input("Masukkan banyak data yang akan diinput: "))

		for x in range(0, banyak_data):
			print(f"===== Jenis #{x+1} =====")
			input1 = input("Input nama merk: ")

			data.append((input1,))

		bersihkanCmd()
		Merk().input(data)
	elif(menu == 2):
		Merk().ambil()
	elif(menu == 3):
		cek_data = Merk().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau diubah: "))
			data_ada = Merk().ambilSatu(inputan)

			if(data_ada):
				input1 = input("Input nama merk: ")

				data = (input1, inputan)

				bersihkanCmd()
				Merk().ubah(data)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	elif(menu == 4):
		cek_data = Merk().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau dihapus: "))
			data_ada = Merk().ambilSatu(inputan)

			if(data_ada):
				bersihkanCmd()
				Merk().hapus(inputan)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	else:
		pass

def kendaraan():
	print("==============")
	print("Data Kendaraan")
	print("==============")
	print("1. Tambah\n2. Tampilkan\n3. Ubah\n4. Hapus")
	menu = int(input("Pilih Menu: "))

	bersihkanCmd()

	if(menu == 1):
		data = []
		banyak_data = int(input("Masukkan banyak data yang akan diinput: "))

		Merk().ambil()
		Jenis().ambil()

		for x in range(0, banyak_data):
			print(f"===== Merk {x+1} =====")
			input1 = input("Input id merk: ")
			input2 = input("Input id jenis: ")
			input3 = input("Input nama kendaraan: ")

			data.append((input1, input2, input3))

		bersihkanCmd()
		Kendaraan().input(data)
	elif(menu == 2):
		Kendaraan().ambil()
	elif(menu == 3):
		cek_data = Kendaraan().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau diubah: "))
			data_ada = Kendaraan().ambilSatu(inputan)
			
			Merk().ambil()
			Jenis().ambil()

			if(data_ada):
				input1 = input("Input id merk: ")
				input2 = input("Input id jenis: ")
				input3 = input("Input nama kendaraan: ")

				data = (input1, input2, input3, inputan)

				bersihkanCmd()
				Kendaraan().ubah(data)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	elif(menu == 4):
		cek_data = Kendaraan().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau dihapus: "))
			data_ada = Kendaraan().ambilSatu(inputan)

			if(data_ada):
				bersihkanCmd()
				Kendaraan().hapus(inputan)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	else:
		pass

def durasi():
	print("=================")
	print("Durasi Peminjaman")
	print("=================")
	print("1. Tambah\n2. Tampilkan\n3. Ubah\n4. Hapus")
	menu = int(input("Pilih Menu: "))

	bersihkanCmd()

	if(menu == 1):
		data = []
		banyak_data = int(input("Masukkan banyak data yang akan diinput: "))

		for x in range(0, banyak_data):
			print(f"===== Jenis #{x+1} =====")
			input1 = input("Input durasi hari (berupa angka): ")
			input2 = input("Input harga (tanpa titik atau koma): ")

			data.append((input1, input2))

		bersihkanCmd()
		Waktu().input(data)
	elif(menu == 2):
		Waktu().ambil()
	elif(menu == 3):
		cek_data = Waktu().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau diubah: "))
			data_ada = Waktu().ambilSatu(inputan)

			if(data_ada):
				input1 = input("Input durasi hari (berupa angka): ")
				input2 = input("Input harga (tanpa titik atau koma): ")

				data = (input1, input2, inputan)

				bersihkanCmd()
				Waktu().ubah(data)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	elif(menu == 4):
		cek_data = Waktu().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau dihapus: "))
			data_ada = Waktu().ambilSatu(inputan)

			if(data_ada):
				bersihkanCmd()
				Waktu().hapus(inputan)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	else:
		pass

def riwayatSewa():
	print("=================")
	print("Riwayat Penyewaan")
	print("=================")
	print("1. Tampilkan\n2. Proses\n3. Hapus\n")
	menu = int(input("Pilih Menu: "))

	bersihkanCmd()

	if(menu == 1):
		Sewa().ambil()
	elif(menu == 2):
		cek_data = Sewa().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau diproses: "))
			data_ada = Sewa().ambilSatu(inputan)

			if(data_ada):
				input1 = int(input(f"Masukkan jumlah uang (tanpa titik atau koma): "))
				input2 = "1"

				if(input1 > data_ada[2]):
					bersihkanCmd()
					data = (input2, inputan)

					print(f"Harga: Rp {data_ada[2]}")
					print(f"Bayar: Rp {input1}")
					print("========================")
					print(f"Kembalian: Rp {input1 - data_ada[2]}")
					Sewa().prosesCash(data)
				else:
					print("Jumlah uang tidak mencukupi")
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	elif(menu == 3):
		cek_data = Sewa().ambil()

		if(cek_data):
			inputan = int(input("Masukkan id yang mau dihapus: "))
			data_ada = Sewa().ambilSatu(inputan)

			if(data_ada):
				bersihkanCmd()
				Sewa().hapus(inputan)
			else:
				bersihkanCmd()
				print(f"ID {inputan} tidak ada.")
		else:
			pass
	else:
		pass

def sewaKendaraan():
	hasil = Kendaraan().ambil()
	
	if(hasil):
		data = []
		input1 = int(input("Pilih id kendaraan yang ingin disewa: "))

		hasil_waktu = Waktu().ambil()

		if(hasil_waktu):
			input2 = int(input("Pilih durasi sewa (Berdasarkan ID): "))
			input3 = sesi[0][0]

			durasiAmbil = Waktu().ambilSatu(input2)

			tanggal_sewa = datetime.today().strftime('%Y-%m-%d')
			initialDate = datetime.strptime(str(tanggal_sewa), '%Y-%m-%d')
			modifiedDate = initialDate + timedelta(days=durasiAmbil[1])
			tanggal_kembali = datetime.strftime(modifiedDate, '%Y-%m-%d')

			data.append((input1, input2, input3, tanggal_sewa, tanggal_kembali, "0"))

			bersihkanCmd()
			Sewa().input(data)
		else:
			bersihkanCmd()
			print("Tidak ada durasi yang tersedia")
	else:
		bersihkanCmd()
		print("Tidak ada kendaraan yang tersedia")

while True:
	if(len(sesi) == 0):
		print("=============================")
		print("Selamat Datang di Admin Panel")
		print("=============================")
		print("1. Login")
		print("2. Registrasi")
		menu = int(input("Pilih menu: "))

		bersihkanCmd()

		if(menu == 1):
			username = input("Input username: ")
			password = input("Input password: ")

			bersihkanCmd()
			Akun().login(username, password)
		elif(menu == 2):
			username = input("Input username: ")
			password = input("Input password: ")
			nama = input("Input nama: ")
			tipe_akun = "User"

			data = [(username, password, nama, tipe_akun)]

			bersihkanCmd()
			Akun().register(data)
		else:
			print("Menu tidak valid")
	else:
		if(sesi[0][3] == "Admin"):
			print("====================")
			print("Selamat Datang Admin")
			print("====================")
			print("1. Manajemen Peraturan")
			print("2. Manajemen Jenis Kendaraan")
			print("3. Manajemen Merk Kendaraan")
			print("4. Manajemen Kendaraan")
			print("5. Manajemen Durasi Sewa")
			print("6. Manajemen Penyewaan")
			print("7. Logout")
			menu = int(input("Pilih menu: "))

			bersihkanCmd()

			if(menu == 1):
				peraturan()
			elif(menu == 2):
				jenisKendaraan()
			elif(menu == 3):
				merk()
			elif(menu == 4):
				kendaraan()
			elif(menu == 5):
				durasi()
			elif(menu == 6):
				riwayatSewa()
			elif(menu == 7):
				sesi = []

				bersihkanCmd()
				print("Berhasil logout")
			else:
				exit()
		else:
			print("===========================")
			print("Selamat Datang di YukRental")
			print("===========================")
			print("1. Sewa Kendaraan")
			print("2. Transaksi Saya")
			print("3. Logout")
			menu = int(input("Pilih menu: "))

			bersihkanCmd()

			if(menu == 1):
				print("Dimohon untuk membaca peraturan berikut sebelum menyewa!")
				Peraturan().ambilUser()
				print()
				sewaKendaraan()
			elif(menu == 2):
				Sewa().ambilTransaksiUser(sesi[0][0])
			elif(menu == 3):
				sesi = []

				bersihkanCmd()
				print("Berhasil logout")
			else:
				exit()