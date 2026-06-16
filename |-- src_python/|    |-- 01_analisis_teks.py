# PROGRAM 1
# Menghitung Jumlah Kata dan Jumlah Kalimat

# Menghitung Jumlah Kata

def hitung_kata(teks):

    jumlah = 1

    for huruf in teks:

        if huruf == " ":

            jumlah = jumlah + 1

    return jumlah

# Menghitung Jumlah Kalimat

def hitung_kalimat(teks):

    jumlah = 0

    for huruf in teks:

        if huruf == ".":

            jumlah = jumlah + 1

    return jumlah


# SKENARIO 1 (NORMAL)
# Teks Lengkap

teks = "Membaca buku merupakan kegiatan yang sangat bermanfaat. Buku dapat menambah wawasan dan pengetahuan pembacanya. Selain itu, membaca buku juga dapat meningkatkan kemampuan berpikir dan memperluas kosakata. Oleh karena itu, kebiasaan membaca perlu diterapkan sejak usia dini."

jumlah_kata = hitung_kata(teks)

jumlah_kalimat = hitung_kalimat(teks)

print("Skenario 1")

print(
    "Teks tersebut memuat",
    jumlah_kalimat,
    "kalimat dan",
    jumlah_kata,
    "kata."
)

print()

# SKENARIO 2 (NORMAL)
# Sebagian Teks

teks = "Membaca buku merupakan kegiatan yang sangat bermanfaat. Buku dapat menambah wawasan dan pengetahuan pembacanya."

jumlah_kata = hitung_kata(teks)

jumlah_kalimat = hitung_kalimat(teks)

print("Skenario 2")

print(
    "Teks tersebut memuat",
    jumlah_kalimat,
    "kalimat dan",
    jumlah_kata,
    "kata."
)

print()

# SKENARIO 3 (KONDISI KHUSUS)
# Satu Kalimat

teks = "Membaca buku merupakan kegiatan yang sangat bermanfaat."

jumlah_kata = hitung_kata(teks)

jumlah_kalimat = hitung_kalimat(teks)

print("Skenario 3")

print(
    "Teks tersebut memuat",
    jumlah_kalimat,
    "kalimat dan",
    jumlah_kata,
    "kata."
)
