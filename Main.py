import Menu
import Persegi
import Lingkaran
import Segitiga

def main():
    while True :
        pilihan = Menu.tampilkan_menu()
        if pilihan == "1" :
            if not Persegi.persegi_main():
                break
        elif pilihan == "2" :
            if not Lingkaran.lingkaran_main():
                break
        elif pilihan == "3" :
            if not Segitiga.segitiga_main():
                break
        elif pilihan == "4" :
            break
        else :
            print("Pilihan tidak valid. Silahkan pilih kembali.")

if __name__ == "__main__" :
    main()