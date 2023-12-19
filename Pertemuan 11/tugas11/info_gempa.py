from Gempa import Gempa 

gempa_ke_1 = Gempa("banten", 1.2)
gempa_ke_2 = Gempa("palu", 6.1)
gempa_ke_3 = Gempa("cianjur", 5.6)
gempa_ke_4 = Gempa("jayapura", 3.3)
gempa_ke_5 = Gempa("garut", 4.0)

print("gempa banten:",gempa_ke_1.dampak())
print("gempa palu:", gempa_ke_2.dampak())
print("gempa cianjur:", gempa_ke_3.dampak())
print("gempa jayapura:", gempa_ke_4.dampak())
print("gempa garut:", gempa_ke_5.dampak())

# gempa_ke_1.dampak()
# gempa_ke_2.dampak()
# gempa_ke_3.dampak()
# gempa_ke_4.dampak()
# gempa_ke_5.dampak()
