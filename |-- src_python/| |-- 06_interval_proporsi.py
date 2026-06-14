# PROGRAM 6
# Menghitung Interval Konfidensi Proporsi Sampel
import math

def hitung_interval_konfidensi(p_hat, alpha, n):
    if p_hat < 0 or p_hat > 1:
        print("proporsi sampel harus bernilai antara 0 dan 1")
    elif n <= 0:
        print("ukuran sampel n harus lebih besar dari 0")
    elif alpha == 10:
        z = 1.645
        tk = 90
        margin = z * math.sqrt((p_hat * (1 - p_hat)) / n)
        batas_bawah = p_hat - margin
        batas_atas = p_hat + margin
        print(f"Interval Konfidensi")
        print(f"  {batas_bawah:.4f}  <  p  <  {batas_atas:.4f}")
    elif alpha == 5:
        z = 1.96
        tk = 95
        margin = z * math.sqrt((p_hat * (1 - p_hat)) / n)
        batas_bawah = p_hat - margin
        batas_atas = p_hat + margin
        print(f"Interval Konfidensi")
        print(f"  {batas_bawah:.4f}  <  p  <  {batas_atas:.4f}")
    else:
        print("nilai alpha hanya boleh 5 atau 10")

# SKENARIO 1 (NORMAL)

p_hat = 0.6
n = 100
alpha = 5

print("Skenario 1")
hitung_interval_konfidensi(p_hat, alpha, n)
print()

# SKENARIO 2 (DATA ALPHA BERBEDA - 10%)

p_hat = 0.6
n = 100
alpha = 10

print("Skenario 2")
hitung_interval_konfidensi(p_hat, alpha, n)
print()

# SKENARIO 3 (KONDISI EROR - PROPORSI TIDAK VALID)

p_hat = 1.5
n = 100
alpha = 5

print("Skenario 3")
hitung_interval_konfidensi(p_hat, alpha, n)
