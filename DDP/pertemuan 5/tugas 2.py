while True : 
    print("""
(1)menghitung luas persegi
(2)menghitung luas lingkaran
(3)menghitung luas sefitiga
""")
    
    luasbangun = int(input("masukan pilihan (1,2,3)"))

    match luasbangun:
        case 1 :
            sisi = int(input("masukan panjang sisi persegi:  "))
            print("=============================")
            print("luas persegi adalah:  ", sisi * sisi , "n/")
            break
        case 2 :
            jari_jari = int(input("masukan jari jari lingkaran:  "))
            print("=============================")
            print("luas lingkaran adalah:  ", 3.14 * jari_jari * jari_jari , "n/")
            break
        case 3 :
            alas = int(input("masukan panjang alas segitiga:  "))
            tinggi = int(input("masukan panjang tinggi segitiga:  "))
            print("=============================")
            print("luas segitiga adalah:  ",  alas*tinggi, "\n")
            break