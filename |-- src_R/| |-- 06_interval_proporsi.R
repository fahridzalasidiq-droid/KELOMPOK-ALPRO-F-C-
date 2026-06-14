# PROGRAM 6
# Menghitung Interval Konfidensi Proporsi Sampel

hitung_interval_konfidensi <- function(p_hat, alpha, n) {
  if (p_hat < 0 || p_hat > 1) {
    cat("proporsi sampel harus bernilai antara 0 dan 1")
  } else if (n <= 0) {
    cat("ukuran sampel n harus lebih besar dari 0")
  } else if (alpha == 10) {
    z           <- 1.645
    tk          <- 90
    margin      <- z * sqrt((p_hat * (1 - p_hat)) / n)
    batas_bawah <- p_hat - margin
    batas_atas  <- p_hat + margin
    cat(sprintf("Interval Konfidensi"))
    cat(sprintf("  %.4f  <  p  <  %.4f", batas_bawah, batas_atas))
  } else if (alpha == 5) {
    z           <- 1.96
    tk          <- 95
    margin      <- z * sqrt((p_hat * (1 - p_hat)) / n)
    batas_bawah <- p_hat - margin
    batas_atas  <- p_hat + margin
    cat(sprintf("Interval Konfidensi"))
    cat(sprintf("  %.4f  <  p  <  %.4f", batas_bawah, batas_atas))
  } else {
    cat("nilai alpha hanya boleh 5 or 10\n")
  }
}

# SKENARIO 1 (NORMAL)
p_hat <- 0.6
n     <- 100
alpha <- 5
cat("Skenario 1")
# SKENARIO 2 (DATA ALPHA BERBEDA)
p_hat <- 0.6
n     <- 100
alpha <- 10
cat("Skenario 2")
## Skenario 2
hitung_interval_konfidensi(p_hat, alpha, n)
# SKENARIO 3 (KONDISI EROR - PROPORSI TIDAK VALID)
p_hat <- 1.5
n     <- 100
alpha <- 5
cat("Skenario 3")
## Skenario 3
hitung_interval_konfidensi(p_hat, alpha, n)
