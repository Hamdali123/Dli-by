# jawaban uts
# 1.  function adalah fungsi yang bisa di jalan kan kapan saja 
# 2. if digunakan untuk membuat keputusan berdasarkan suatu kondisi pertama true,  else fungsinya mengani kondisi yang tidak memenuhi atau (false), yang di gunakan untuk memriksa kondisi tamabahan jika kondisi pertama tersebut tidak terpenuhi (false),

# 3.
1# Harga makanan per porsi
harga_nasi_goreng = 20000
harga_mie_goreng = 15000
harga_sate = 30000

# Uang saku pembeli
uang_saku = 300000

# Input jumlah pembelian
print("\033[36mPilihan Makanan:")
print("\033[34m1. Nasi Goreng (Rp20.000 per porsi)")
print("\033[34m2. Mie Goreng (Rp15.000 per porsi)")
print("\033[34m3. Sate (Rp30.000 per porsi)")

# Input jumlah masing-masing makanan yang dibeli
nasi_goreng = int(input("\033[35mMasukkan jumlah porsi Nasi Goreng: "))
mie_goreng = int(input("\033[35mMasukkan jumlah porsi Mie Goreng: "))
sate = int(input("\033[35mMasukkan jumlah porsi Sate: "))

# Menghitung total belanja
total_belanja = (nasi_goreng * harga_nasi_goreng) + (mie_goreng * harga_mie_goreng) + (sate * harga_sate)

# Memeriksa apakah total belanja memenuhi syarat diskon
if total_belanja > 100000:
    diskon = 0.2 * total_belanja  # Diskon 20%
    total_belanja -= diskon
    print(f"\033[32mDiskon 20% applied! Total setelah diskon: Rp{total_belanja:.2f}")
else:
    print(f"Total belanja: Rp{total_belanja:.2f}")

# Menghitung uang kembalian
kembalian = uang_saku - total_belanja

# Menampilkan uang kembalian
if kembalian >= 0:
    print(f"\033[33mUang Kembalian: Rp{kembalian:.2f}")
else:
    print("Uang tidak cukup untuk membeli makanan ini.")


"""# 4. 
# tuple 
fruits = ("banana", "apple", "cherry")

# Mengubah tuple menjadi list
fruits_list = list(fruits)
fruits_list.sort()
fruits_list[fruits_list.index("banana")] = ["banana"]

# Menampilkan hasil akhir
print(fruits_list)
"""

# 5.

"""def intersect_sets(setA, setB):
    return setA & setB  

# menampilkan kedua set
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Memanggil fungsi dan menampilkan hasil
result = intersect_sets(setA, setB)
print(result)"""
print("\033[37m")
class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'
