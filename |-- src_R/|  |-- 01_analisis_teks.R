# PROGRAM 1
# Menghitung Jumlah Kata dan Jumlah Kalimat

# Menghitung Jumlah Kata

hitung_kata <- function(teks){
  
  jumlah <- 1
  
  for(huruf in strsplit(teks, "")[[1]]){
    
    if(huruf == " "){
      
      jumlah <- jumlah + 1
      
    }
    
  }
  
  return(jumlah)
  
}


# Menghitung Jumlah Kalimat

hitung_kalimat <- function(teks){
  
  jumlah <- 0
  
  for(huruf in strsplit(teks, "")[[1]]){
    
    if(huruf == "."){
      
      jumlah <- jumlah + 1
      
    }
    
  }
  
  return(jumlah)
  
}


# SKENARIO 1 (NORMAL)

teks <- "Media sosial atau disebut juga dengan jejaring sosial, seperti Facebook, Twitter, Instagram, dan masih banyak lagi ternyata tidak hanya digunakan sebagai tempat berkumpul atau berbagi di dunia maya. Namun, media sosial kini juga bisa dimanfaatkan sebagai media untuk mengembangkan sebuah bisnis. Saat ini telah banyak para pengusaha yang beralih ke media sosial dalam memasarkan produk mereka baik barang ataupun jasa. Beralihnya para pelaku bisnis ke media ini dikarenakan jejaring sosial memiliki manfaat yang sangat banyak bagi usaha bisnis. Berikut ini adalah alasan mengapa jejaring sosial bisa menjadi alat promosi yang paling efektif."

jumlah_kata <- hitung_kata(teks)

jumlah_kalimat <- hitung_kalimat(teks)

cat("Skenario 1\n")
## Skenario 1
cat(
  "Teks tersebut memuat",
  jumlah_kalimat,
  "kalimat dan",
  jumlah_kata,
  "kata.\n\n"
)
# SKENARIO 2 (NORMAL)

teks <- "Media sosial atau disebut juga dengan jejaring sosial, seperti Facebook, Twitter, Instagram, dan masih banyak lagi ternyata tidak hanya digunakan sebagai tempat berkumpul atau berbagi di dunia maya. Namun, media sosial kini juga bisa dimanfaatkan sebagai media untuk mengembangkan sebuah bisnis."

jumlah_kata <- hitung_kata(teks)

jumlah_kalimat <- hitung_kalimat(teks)

cat("Skenario 2\n")
cat(
  "Teks tersebut memuat",
  jumlah_kalimat,
  "kalimat dan",
  jumlah_kata,
  "kata.\n\n"
)
## Teks tersebut memuat 2 kalimat dan 41 kata.
# SKENARIO 3 (KONDISI KHUSUS)

teks <- "Berikut ini adalah alasan mengapa jejaring sosial bisa menjadi alat promosi yang paling efektif."

jumlah_kata <- hitung_kata(teks)

jumlah_kalimat <- hitung_kalimat(teks)

cat("Skenario 3\n")
## Skenario 3
cat(
  "Teks tersebut memuat",
  jumlah_kalimat,
  "kalimat dan",
  jumlah_kata,
  "kata.\n"
)

