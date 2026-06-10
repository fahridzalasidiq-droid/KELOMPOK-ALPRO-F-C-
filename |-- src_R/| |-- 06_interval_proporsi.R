p_hat <- 0.6
n     <- 100
alpha <- 5

hitung_interval_konfidensi <- function(p_hat, alpha, n) {
  if (p_hat < 0 || p_hat > 1) {
    cat("Error: proporsi sampel harus bernilai antara 0 dan 1")
  } else if (n <= 0) {
    cat("Error: ukuran sampel n harus lebih besar dari 0")
  } else if (alpha == 10) {
    z           <- 1.645
    tk          <- 90
    margin      <- z * sqrt((p_hat * (1 - p_hat)) / n)
    batas_bawah <- p_hat - margin
    batas_atas  <- p_hat + margin
    cat(sprintf("Interval Konfidensi %d%%", tk))
    cat(sprintf("  %.4f  <  p  <  %.4f\n", batas_bawah, batas_atas))
  } else if (alpha == 5) {
    z           <- 1.96
    tk          <- 95
    margin      <- z * sqrt((p_hat * (1 - p_hat)) / n)
    batas_bawah <- p_hat - margin
    batas_atas  <- p_hat + margin
    cat(sprintf("Interval Konfidensi %d%%", tk))
    cat(sprintf("  %.4f  <  p  <  %.4f", batas_bawah, batas_atas))
  } else {
    cat("Error nilai alpha hanya boleh 5 atau 10")
  }
}

hitung_interval_konfidensi(p_hat, alpha, n) 
## Interval Konfidensi 95%  0.5040  <  p  <  0.6960
