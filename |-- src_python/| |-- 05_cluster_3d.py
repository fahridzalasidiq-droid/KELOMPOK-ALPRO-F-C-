# PROGRAM 5
# Menentukan Cluster Terdekat

import math


# Fungsi Menghitung Jarak Euclidean

def hitung_jarak(x1, x2, x3, c1, c2, c3):

    return math.sqrt(
        (x1 - c1) ** 2 +
        (x2 - c2) ** 2 +
        (x3 - c3) ** 2
    )


# Fungsi Menghitung Semua Jarak

def hitung_semua_jarak(x1, x2, x3):

    jarakA = hitung_jarak(x1, x2, x3, 2, 1, 3)

    jarakB = hitung_jarak(x1, x2, x3, 1, -4, 6)

    jarakC = hitung_jarak(x1, x2, x3, -2, 3, -2)

    return jarakA, jarakB, jarakC


# SKENARIO 1 (NORMAL)
# Cluster A

x1 = 2
x2 = 1
x3 = 3

jarakA, jarakB, jarakC = hitung_semua_jarak(x1, x2, x3)

if jarakA < jarakB and jarakA < jarakC:

    cluster = "A"

elif jarakB < jarakA and jarakB < jarakC:

    cluster = "B"

elif jarakC < jarakA and jarakC < jarakB:

    cluster = "C"

else:

    cluster = "Tidak Diketahui"

print("Skenario 1")

print("Jarak Cluster A =", jarakA)

print("Jarak Cluster B =", jarakB)

print("Jarak Cluster C =", jarakC)

print("Titik U termasuk Cluster", cluster)

print()


# SKENARIO 2 (NORMAL)
# Cluster B

x1 = 1
x2 = -4
x3 = 6

jarakA, jarakB, jarakC = hitung_semua_jarak(x1, x2, x3)

if jarakA < jarakB and jarakA < jarakC:

    cluster = "A"

elif jarakB < jarakA and jarakB < jarakC:

    cluster = "B"

elif jarakC < jarakA and jarakC < jarakB:

    cluster = "C"

else:

    cluster = "Tidak Diketahui"

print("Skenario 2")

print("Jarak Cluster A =", jarakA)

print("Jarak Cluster B =", jarakB)

print("Jarak Cluster C =", jarakC)

print("Titik U termasuk Cluster", cluster)

print()


# SKENARIO 3 (KONDISI KHUSUS)
# Cluster C

x1 = -2
x2 = 3
x3 = -2

jarakA, jarakB, jarakC = hitung_semua_jarak(x1, x2, x3)

if jarakA < jarakB and jarakA < jarakC:

    cluster = "A"

elif jarakB < jarakA and jarakB < jarakC:

    cluster = "B"

elif jarakC < jarakA and jarakC < jarakB:

    cluster = "C"

else:

    cluster = "Tidak Diketahui"

print("Skenario 3")

print("Jarak Cluster A =", jarakA)

print("Jarak Cluster B =", jarakB)

print("Jarak Cluster C =", jarakC)

print("Titik U termasuk Cluster", cluster)
