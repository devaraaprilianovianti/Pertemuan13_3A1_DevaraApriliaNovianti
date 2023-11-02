def hitung_luas(a, t):
    return (a * t) / 2

def segitiga_main():
    print("Menghitung Luas Segitiga")
    a = float(input("Masukkan Alas :"))
    t = float(input("Masukkan Tinggi :"))
    luas = hitung_luas(a,t)
    print("Luas Segitiga adalah", luas)
    print()
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        return True
    else :
        return False