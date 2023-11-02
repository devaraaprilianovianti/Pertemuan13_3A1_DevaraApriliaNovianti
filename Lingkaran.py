def hitung_luas(r):
    return 3.14 * (r ** 2)
def lingkaran_main():
    print("Menghitung Luas Lingkaran")
    r = float(input("Masukkan Jari-Jari : "))
    luas = hitung_luas(r)
    print("Luas Lingkaran adalah ", luas)
    print()
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        return True
    else :
       return False