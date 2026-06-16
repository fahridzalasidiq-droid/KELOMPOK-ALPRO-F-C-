#PROGRAM NOMOR 3
#MELAKUKAN PERHITUNGAN TERHADAP PERSAMAAN KUADRAT
#misalkan 0x+2x+3
import math
# Input koefisien persamaan kuadrat
a, b, c = 0, 2, 3
#cek apakah persamaan merupakan persamaan kuadrat
if a == 0:
    print("Bukan persamaan kuadrat")
else:
#Hitung Diskriminan
    diskriminan = b**2 - 4*a*c
    #cek nilai deskriminan
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
# Input koefisien persamaan kuadrat
a, b, c = 1, -5, 6
#cek apakah persamaan merupakan persamaan kuadrat
if a == 0:
    print("Bukan persamaan kuadrat")
else:
#Hitung Diskriminan
    diskriminan = b**2 - 4*a*c
    #cek nilai deskriminan
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

# SKENARIO 2 (DUA AKAR REAL KEMBAR)
import math
# Input koefisien persamaan kuadrat
a, b, c = 1, -4, 4
#cek apakah persamaan merupakan persamaan kuadrat
if a == 0:
    print("Bukan persamaan kuadrat")
else:
#Hitung Diskriminan
    diskriminan = b**2 - 4*a*c
    #cek nilai deskriminan
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
# SKENARIO 3 (AKAR IMAJINER)
import math
# Input koefisien persamaan kuadrat
a, b, c = 1, 2, 5
#cek apakah persamaan merupakan persamaan kuadrat
if a == 0:
    print("Bukan persamaan kuadrat")
else:
#Hitung Diskriminan
    diskriminan = b**2 - 4*a*c
    #cek nilai deskriminan
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
