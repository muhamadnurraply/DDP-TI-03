#Keliling = sisi 1 + sisi 2 + sisi 3 + sisi 4 atau AB + BC + CD + AD.
#Luas = (sisi sejajar 1 + sisi sejajar 2 /2) x tinggi atau 1/2 (a + b) x t.
def menghitung_luas_trapesium(a, b, t):
    return 1/2 * (a + b) * t

def menghitung_keliling_trapesium(a, b, t):
    return a + b + t


a = int(input("nilai sisi1:"))
b = int(input("nilai sisi2:"))
t = int(input("nilai tinggi:"))


luas = menghitung_luas_trapesium
keliling = menghitung_keliling_trapesium

print("Luas trapesium:", luas)
print("Keliling trapesium:", keliling)
