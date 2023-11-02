def hitung_luas(p,l):
    return p * l

def persegi_main():
    print("Menghitung Luas Persegi Panjang")
    p = float(input("Masukkan Panjang : "))
    l = float(input("Massukkan Lebar : "))
    luas = hitung_luas(p,l)
    print("Luas Persegi Panjang adalah ", luas)
    print()
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        return True
    else :
       return False