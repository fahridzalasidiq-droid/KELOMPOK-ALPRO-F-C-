# PROGRAM 5
# Menentukan Cluster Terdekat


# Fungsi Menghitung Jarak Euclidean

hitung_jarak <- function(x1, x2, x3, c1, c2, c3){
  
  sqrt(
    (x1 - c1)^2 +
      (x2 - c2)^2 +
      (x3 - c3)^2
  )
  
}


# Fungsi Menghitung Semua Jarak

hitung_semua_jarak <- function(x1, x2, x3){
  
  jarakA <- hitung_jarak(x1, x2, x3, 2, 1, 3)
  
  jarakB <- hitung_jarak(x1, x2, x3, 1, -4, 6)
  
  jarakC <- hitung_jarak(x1, x2, x3, -2, 3, -2)
  
  return(list(jarakA, jarakB, jarakC))
  
}


# SKENARIO 1 (NORMAL)
# Cluster A

x1 <- 2
x2 <- 1
x3 <- 3

jarak <- hitung_semua_jarak(x1, x2, x3)

jarakA <- jarak[[1]]
jarakB <- jarak[[2]]
jarakC <- jarak[[3]]

if(jarakA < jarakB && jarakA < jarakC){
  
  cluster <- "A"
  
} else if(jarakB < jarakA && jarakB < jarakC){
  
  cluster <- "B"
  
} else if(jarakC < jarakA && jarakC < jarakB){
  
  cluster <- "C"
  
} else {
  
  cluster <- "Tidak Diketahui"
  
}

cat("Skenario 1\n")

cat("Jarak Cluster A =", jarakA, "\n")

cat("Jarak Cluster B =", jarakB, "\n")

cat("Jarak Cluster C =", jarakC, "\n")

cat("Titik U termasuk Cluster", cluster, "\n\n")


# SKENARIO 2 (NORMAL)
# Cluster B

x1 <- 1
x2 <- -4
x3 <- 6

jarak <- hitung_semua_jarak(x1, x2, x3)

jarakA <- jarak[[1]]
jarakB <- jarak[[2]]
jarakC <- jarak[[3]]

if(jarakA < jarakB && jarakA < jarakC){
  
  cluster <- "A"
  
} else if(jarakB < jarakA && jarakB < jarakC){
  
  cluster <- "B"
  
} else if(jarakC < jarakA && jarakC < jarakB){
  
  cluster <- "C"
  
} else {
  
  cluster <- "Tidak Diketahui"
  
}

cat("Skenario 2\n")

cat("Jarak Cluster A =", jarakA, "\n")

cat("Jarak Cluster B =", jarakB, "\n")

cat("Jarak Cluster C =", jarakC, "\n")

cat("Titik U termasuk Cluster", cluster, "\n\n")


# SKENARIO 3 (KONDISI KHUSUS)
# Cluster C

x1 <- -2
x2 <- 3
x3 <- -2

jarak <- hitung_semua_jarak(x1, x2, x3)

jarakA <- jarak[[1]]
jarakB <- jarak[[2]]
jarakC <- jarak[[3]]

if(jarakA < jarakB && jarakA < jarakC){
  
  cluster <- "A"
  
} else if(jarakB < jarakA && jarakB < jarakC){
  
  cluster <- "B"
  
} else if(jarakC < jarakA && jarakC < jarakB){
  
  cluster <- "C"
  
} else {
  
  cluster <- "Tidak Diketahui"
  
}

cat("Skenario 3\n")

cat("Jarak Cluster A =", jarakA, "\n")

cat("Jarak Cluster B =", jarakB, "\n")

cat("Jarak Cluster C =", jarakC, "\n")

cat("Titik U termasuk Cluster", cluster, "\n")

