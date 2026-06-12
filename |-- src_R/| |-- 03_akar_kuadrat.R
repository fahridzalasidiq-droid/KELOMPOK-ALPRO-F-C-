# PROGRAM 3
# Akar-akar Persamaan Kuadrat
# Input koefisien persamaan kuadrat a,b,c
# Hitung diskriminan
#misalkan persamaan kuadratnya:x^2+6x-9
# a=1, b=6, c=9
a<-1;b<-6;c<- -9
diskriminan <- b^2 - 4*a*c
# Cek nilai diskriminan
if (diskriminan > 0) {
  x1 <- (-b + sqrt(diskriminan)) / (2*a)
  x2 <- (-b - sqrt(diskriminan)) / (2*a)
  cat("Persamaan memiliki dua akar real berbeda:\n")
  cat(sprintf("x1 = %.3f\n", x1))
  cat(sprintf("x2 = %.3f\n", x2))
} else if (diskriminan == 0) {
  x <- -b / (2*a)
  cat("Persamaan memiliki akar real kembar:\n")
  cat(sprintf("x1 = x2 = %.3f\n", x))
} else {
  cat("Persamaan hanya memiliki akar-akar imajiner.\n")
}
## Persamaan memiliki dua akar real berbeda:
## x1 = 1.243
## x2 = -7.243
# SKENARIO 1 (DUA AKAR REAL BERBEDA)
a <- 1; b <- -5; c <- 6
diskriminan <- b^2 - 4*a*c
cat("Skenario 1\n")
## Skenario 1
if (diskriminan > 0) {
  x1 <- (-b + sqrt(diskriminan)) / (2*a)
  x2 <- (-b - sqrt(diskriminan)) / (2*a)
  cat("Persamaan memiliki dua akar real berbeda.\n")
  cat(sprintf("x1 = %.3f\n", x1))
  cat(sprintf("x2 = %.3f\n", x2))
} else if (diskriminan == 0) {
  x <- -b / (2*a)
  cat("Persamaan memiliki dua akar real kembar.\n")
  cat(sprintf("x1 = x2 = %.3f\n", x))
} else {
  cat("Persamaan hanya memiliki akar-akar imajiner.\n")
}
## Persamaan memiliki dua akar real berbeda.
## x1 = 3.000
## x2 = 2.000
cat("\n")
# SKENARIO 2 (DUA AKAR REAL KEMBAR)
a <- 1; b <- -4; c <- 4
diskriminan <- b^2 - 4*a*c
cat("Skenario 2\n")
## Skenario 2
if (diskriminan > 0) {
  x1 <- (-b + sqrt(diskriminan)) / (2*a)
  x2 <- (-b - sqrt(diskriminan)) / (2*a)
  cat("Persamaan memiliki dua akar real berbeda.\n")
  cat(sprintf("x1 = %.3f\n", x1))
  cat(sprintf("x2 = %.3f\n", x2))
} else if (diskriminan == 0) {
  x <- -b / (2*a)
  cat("Persamaan memiliki dua akar real kembar.\n")
  cat(sprintf("x1 = x2 = %.3f\n", x))
} else {
  cat("Persamaan hanya memiliki akar-akar imajiner.\n")
}
## Persamaan memiliki dua akar real kembar.
## x1 = x2 = 2.000
cat("\n")
# SKENARIO 3 (AKAR IMAJINER)
a <- 1; b <- 2; c <- 5
diskriminan <- b^2 - 4*a*c
cat("Skenario 3\n")
## Skenario 3
if (diskriminan > 0) {
  x1 <- (-b + sqrt(diskriminan)) / (2*a)
  x2 <- (-b - sqrt(diskriminan)) / (2*a)
  cat("Persamaan memiliki dua akar real berbeda.\n")
  cat(sprintf("x1 = %.3f\n", x1))
  cat(sprintf("x2 = %.3f\n", x2))
} else if (diskriminan == 0) {
  x <- -b / (2*a)
  cat("Persamaan memiliki dua akar real kembar.\n")
  cat(sprintf("x1 = x2 = %.3f\n", x))
} else {
  cat("Persamaan hanya memiliki akar-akar imajiner.\n")
}
## Persamaan hanya memiliki akar-akar imajiner.

