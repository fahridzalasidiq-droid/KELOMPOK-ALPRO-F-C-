# PROGRAM 1
# Menghitung jumlah kata dan jumlah kalimat

# SKENARIO 1 (NORMAL)

teks = "Media sosial atau disebut juga dengan jejaring sosial, seperti Facebook, Twitter, Instagram, dan masih banyak lagi ternyata tidak hanya digunakan sebagai tempat berkumpul atau berbagi di dunia maya. Namun, media sosial kini juga bisa dimanfaatkan sebagai media untuk mengembangkan sebuah bisnis. Saat ini telah banyak para pengusaha yang beralih ke media sosial dalam memasarkan produk mereka baik barang ataupun jasa. Beralihnya para pelaku bisnis ke media ini dikarenakan jejaring sosial memiliki manfaat yang sangat banyak bagi usaha bisnis. Berikut ini adalah alasan mengapa jejaring sosial bisa menjadi alat promosi yang paling efektif."

jumlah_kata = len(teks.split())

jumlah_kalimat = len(teks.split(".")) - 1

print("Skenario 1")

print(
    "Teks tersebut memuat",
    jumlah_kalimat,
    "kalimat dan",
    jumlah_kata,
    "kata."
)

print()


# SKENARIO 2 (DATA LEBIH SEDIKIT)

teks = "Media sosial atau disebut juga dengan jejaring sosial, seperti Facebook, Twitter, Instagram, dan masih banyak lagi ternyata tidak hanya digunakan sebagai tempat berkumpul atau berbagi di dunia maya. Namun, media sosial kini juga bisa dimanfaatkan sebagai media untuk mengembangkan sebuah bisnis."

jumlah_kata = len(teks.split())

jumlah_kalimat = len(teks.split(".")) - 1

print("Skenario 2")

print(
    "Teks tersebut memuat",
    jumlah_kalimat,
    "kalimat dan",
    jumlah_kata,
    "kata."
)

print()


# SKENARIO 3 (DATA MENENGAH)

teks = "Media sosial atau disebut juga dengan jejaring sosial, seperti Facebook, Twitter, Instagram, dan masih banyak lagi ternyata tidak hanya digunakan sebagai tempat berkumpul atau berbagi di dunia maya. Namun, media sosial kini juga bisa dimanfaatkan sebagai media untuk mengembangkan sebuah bisnis. Saat ini telah banyak para pengusaha yang beralih ke media sosial dalam memasarkan produk mereka baik barang ataupun jasa."

jumlah_kata = len(teks.split())

jumlah_kalimat = len(teks.split(".")) - 1

print("Skenario 3")

print(
    "Teks tersebut memuat",
    jumlah_kalimat,
    "kalimat dan",
    jumlah_kata,
    "kata."
)


