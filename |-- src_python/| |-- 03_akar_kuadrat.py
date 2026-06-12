# PROGRAM 3
# Akar-akar Persamaan Kuadrat
import math

# Input koefisien persamaan kuadrat
#memasukan nilai misalnya pesamaan kuadaratnya x**2+6x-9
#sehingga a=1, b=6, c=-9
a, b, c, = 1,2,-6

# Hitung diskriminan
diskriminan = b**2 - 4*a*c

# Cek nilai diskriminan
if diskriminan > 0:
    x1 = (-b + math.sqrt(diskriminan)) / (2*a)
    x2 = (-b - math.sqrt(diskriminan)) / (2*a)
    print(f"Persamaan memiliki dua akar real berbeda:")
    print(f"x1 = {x1:.3f}")
    print(f"x2 = {x2:.3f}")
elif diskriminan == 0:
    x = -b / (2*a)
    print(f"Persamaan memiliki akar real kembar:")
    print(f"x1 = x2 = {x:.3f}")
else:
    print("Persamaan hanya memiliki akar-akar imajiner.")
  # SKENARIO 1 (DUA AKAR REAL BERBEDA)
import math
a, b, c = 1, -5, 6
diskriminan = b**2 - 4*a*c
print("Skenario 1")
if diskriminan > 0:
    x1 = (-b + math.sqrt(diskriminan)) / (2*a)
    x2 = (-b - math.sqrt(diskriminan)) / (2*a)
    print(f"Persamaan memiliki dua akar real berbeda.")
    print(f"x1 = {x1:.3f}")
    print(f"x2 = {x2:.3f}")
elif diskriminan == 0:
    x = -b / (2*a)
    print(f"Persamaan memiliki dua akar real kembar.")
    print(f"x1 = x2 = {x:.3f}")
else:
    print("Persamaan hanya memiliki akar-akar imajiner.")
  # SKENARIO 2 (DUA AKAR REAL KEMBAR)
import math
a, b, c = 1, -4, 4
diskriminan = b**2 - 4*a*c
print("Skenario 2")
if diskriminan > 0:
    x1 = (-b + math.sqrt(diskriminan)) / (2*a)
    x2 = (-b - math.sqrt(diskriminan)) / (2*a)
    print(f"Persamaan memiliki dua akar real berbeda.")
    print(f"x1 = {x1:.3f}")
    print(f"x2 = {x2:.3f}")
elif diskriminan == 0:
    x = -b / (2*a)
    print(f"Persamaan memiliki dua akar real kembar.")
    print(f"x1 = x2 = {x:.3f}")
else:
    print("Persamaan hanya memiliki akar-akar imajiner.")
print()
# SKENARIO 3 (AKAR IMAJINER)
import math
a, b, c = 1, 2, 5
diskriminan = b**2 - 4*a*c
print("Skenario 3")
if diskriminan > 0:
    x1 = (-b + math.sqrt(diskriminan)) / (2*a)
    x2 = (-b - math.sqrt(diskriminan)) / (2*a)
    print(f"Persamaan memiliki dua akar real berbeda.")
    print(f"x1 = {x1:.3f}")
    print(f"x2 = {x2:.3f}")
elif diskriminan == 0:
    x = -b / (2*a)
    print(f"Persamaan memiliki dua akar real kembar.")
    print(f"x1 = x2 = {x:.3f}")
else:
    print("Persamaan hanya memiliki akar-akar imajiner.")
