#PROGRAM NOMOR 3
#MELAKUKAN PERHITUNGAN TERHADAP PERSAMAAN KUADRAT
#misalkan 0x+2x+3
a <- 0; b <- 2; c <-3
#Mengecek nilai koefisien a
if (a == 0){
  print("Bukan persamaan kuadrat")
}else {
  #Menghitung diskriminan
  diskriminan <- b^2 - 4*a*c
  #mengecek nilai diskriminan
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
}
# SKENARIO 1 (DUA AKAR REAL BERBEDA)
a <- 1; b <- -5; c <-6
#Mengecek nilai koefisien a
if (a == 0){
  print("Bukan persamaan kuadrat")
}else {
  #Menghitung diskriminan
  diskriminan <- b^2 - 4*a*c
  #mengecek nilai diskriminan
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
}
# SKENARIO 2 (DUA AKAR REAL KEMBAR)
a <- 1; b <- -4; c <- 4
#Mengecek nilai koefisien a
if (a == 0){
  print("Bukan persamaan kuadrat")
}else {
  #Menghitung diskriminan
  diskriminan <- b^2 - 4*a*c
  #mengecek nilai diskriminan
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
}
# SKENARIO 3 (AKAR IMAJINER)
a <- 1; b <- 2; c <- 5
#Mengecek nilai koefisien a
if (a == 0){
  print("Bukan persamaan kuadrat")
}else {
  #Menghitung diskriminan
  diskriminan <- b^2 - 4*a*c
  #mengecek nilai diskriminan
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
}
