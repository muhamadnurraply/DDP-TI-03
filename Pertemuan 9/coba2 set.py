motor ={"beat" , "scopy", "aerok"}
#tambahan untuk union
mobil ={"lamborgini", "ferari","bemo","avanza"}
print(motor)

#Menambahkan item
motor.add("nmax")
print(motor)

#menghapus item
#  motor.pop(0)
#ini tidak bisa atau tidak bagus untuk set

#menghapus item bisa di gunakan dengan
motor.remove("beat")
print(motor)

#menggabungkan item set dengan  union
kendaraan = motor.union (mobil)
print(kendaraan)

#memasukan dengan set update
motor.update(mobil)
print(motor)

