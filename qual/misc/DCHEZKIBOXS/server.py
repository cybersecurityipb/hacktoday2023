#!/usr/bin/env python3
from random import randint
from secret import get_password

def main():
    n=int(1e5)
    s=""
    for i in range(n):
        tm=randint(65,90)
        s+=chr(tm)
    print(s)
    real_password=get_password(s)
    print("\nItu stringku, mana passwordmu?")
    print("\npasswordnya adalah substring terpanjang pertama yang merupakan 'kata DCHEZKIBOXS'.\nSebuah string dikatakan 'kata DCHEZKIBOXS' jika dan hanya jika string tersebut dibelah dua secara horizontal kedua bagian string (atas dan bawah) akan membentuk bagian yang berimbang dan dapat dibentuk menjadi sama persis jika beberapa bagiannya dirotasi.")
    inp=input("password: ")
    if(inp==real_password):
        with open("flag.txt", "rb") as f:
            flag = f.read().strip()
            f.close()
        print("Congratsss, ini flag buatmu! :",flag.decode())
    else:
        print("TTP SMNGTT")

if __name__ == "__main__":
    main()
