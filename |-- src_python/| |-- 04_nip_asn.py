
# PROGRAM 4
# Menampilkan Tanggal Lahir ASN Berdasarkan NIP dengan Menggunakan Python


# SKENARIO 1 (NORMAL)

nip = "199301212019031010"

if nip == "":
    print("NIP belum diinput!")
elif len(nip) < 8:
    print("NIP harus terdiri dari minimal 8 digit!")
else: 
  tahun = nip[0:4]
  bulan = nip[4:6]
  tanggal = nip[6:8]

  if bulan == "01":
    nama_bulan = "Januari"
  elif bulan == "02":
    nama_bulan = "Februari"
  elif bulan == "03":
    nama_bulan = "Maret"
  elif bulan == "04":
    nama_bulan = "April"
  elif bulan == "05":
    nama_bulan = "Mei"
  elif bulan == "06":
    nama_bulan = "Juni"
  elif bulan == "07":
    nama_bulan = "Juli"
  elif bulan == "08":
    nama_bulan = "Agustus"
  elif bulan == "09":
    nama_bulan = "September"
  elif bulan == "10":
    nama_bulan = "Oktober"
  elif bulan == "11":
    nama_bulan = "November"
  elif bulan == "12":
    nama_bulan = "Desember"
  else:
    nama_bulan = "Bulan tidak valid"
  print("Tanggal lahir ASN adalah", int(tanggal), nama_bulan, tahun)



# SKENARIO 2 (KONDISI KHUSUS)

nip = "200613192019031010"

if nip == "":
    print("NIP belum diinput!")
elif len(nip) < 8:
    print("NIP harus terdiri dari minimal 8 digit!")
else: 
  tahun = nip[0:4]
  bulan = nip[4:6]
  tanggal = nip[6:8]

  if bulan == "01":
    nama_bulan = "Januari"
  elif bulan == "02":
    nama_bulan = "Februari"
  elif bulan == "03":
    nama_bulan = "Maret"
  elif bulan == "04":
    nama_bulan = "April"
  elif bulan == "05":
    nama_bulan = "Mei"
  elif bulan == "06":
    nama_bulan = "Juni"
  elif bulan == "07":
    nama_bulan = "Juli"
  elif bulan == "08":
    nama_bulan = "Agustus"
  elif bulan == "09":
    nama_bulan = "September"
  elif bulan == "10":
    nama_bulan = "Oktober"
  elif bulan == "11":
    nama_bulan = "November"
  elif bulan == "12":
    nama_bulan = "Desember"
  else:
    nama_bulan = "Bulan tidak valid"

  print("Tanggal lahir ASN adalah", int(tanggal), nama_bulan, tahun)


# SKENARIO 3 (KONDISI KHUSUS)

nip = "200705"

if nip == "":
    print("NIP belum diinput!")
elif len(nip) < 8:
    print("NIP harus terdiri dari minimal 8 digit!")
else: 
  tahun = nip[0:4]
  bulan = nip[4:6]
  tanggal = nip[6:8]

  if bulan == "01":
    nama_bulan = "Januari"
  elif bulan == "02":
    nama_bulan = "Februari"
  elif bulan == "03":
    nama_bulan = "Maret"
  elif bulan == "04":
    nama_bulan = "April"
  elif bulan == "05":
    nama_bulan = "Mei"
  elif bulan == "06":
    nama_bulan = "Juni"
  elif bulan == "07":
    nama_bulan = "Juli"
  elif bulan == "08":
    nama_bulan = "Agustus"
  elif bulan == "09":
    nama_bulan = "September"
  elif bulan == "10":
    nama_bulan = "Oktober"
  elif bulan == "11":
    nama_bulan = "November"
  elif bulan == "12":
    nama_bulan = "Desember"
  else:
    nama_bulan = "Bulan tidak valid"

  print("Tanggal lahir ASN adalah", int(tanggal), nama_bulan, tahun)


# SKENARIO 4 (KONDISI KHUSUS)

nip = ""

if nip == "":
    print("NIP belum diinput!")
elif len(nip) < 8:
    print("NIP harus terdiri dari minimal 8 digit!")
else: 
  tahun = nip[0:4]
  bulan = nip[4:6]
  tanggal = nip[6:8]

  if bulan == "01":
    nama_bulan = "Januari"
  elif bulan == "02":
    nama_bulan = "Februari"
  elif bulan == "03":
    nama_bulan = "Maret"
  elif bulan == "04":
    nama_bulan = "April"
  elif bulan == "05":
    nama_bulan = "Mei"
  elif bulan == "06":
    nama_bulan = "Juni"
  elif bulan == "07":
    nama_bulan = "Juli"
  elif bulan == "08":
    nama_bulan = "Agustus"
  elif bulan == "09":
    nama_bulan = "September"
  elif bulan == "10":
    nama_bulan = "Oktober"
  elif bulan == "11":
    nama_bulan = "November"
  elif bulan == "12":
    nama_bulan = "Desember"
  else:
    nama_bulan = "Bulan tidak valid"

  print("Tanggal lahir ASN adalah", int(tanggal), nama_bulan, tahun)
