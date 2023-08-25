#!/usr/bin/python3
import random
import time
import sys
from string import printable


class Unbuffered(object):
  def __init__(self, stream):
    self.stream = stream
  def write(self, data):
    self.stream.write(data)
    self.stream.flush()
  def writelines(self, datas):
    self.stream.writelines(datas)
    self.stream.flush()
  def __getattr__(self, attr):
    return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

kamus = {}

def cekk(a):
    ind = a.index('?')
    a = a[ind:]
    for i in a:
        if i not in printable:
            print(i)
            return False
    return True   


db = open('database.txt', 'r').readlines()
flag = open('flag.txt', 'r').read()
for i in range(len(db)):
    # print(i)
    # print(db[i])
    assert '? ' in db[i] and db[i].count('? ') == 1 and cekk(db[i])
    db[i] = db[i].strip().split('? ')

def rule():
    print("Selamat datang di permainan Simulasi UTBK kami, ada beberapa peraturan yang harus kalian taati sebelum mulai")
    print("1. setiap jawaban benar akan menambahkan skormu sebesar 1")
    print("2. apabila jawaban kalian salah, skor akan direset dan nyawa anda berkurang")
    print("3. objektif anda adalah mengumpulkan skor hingga 100")
    print("4. kalian diberikan waktu sebesar 1 menit untuk menyelesaikan permainan")
    print("5. permainan dimulai dengan nyawa sebesar 3 dan skor sebesar 0")
    print("6. game berakhir apabila nyawa anda habis, waktu anda habis atau anda berhasil menyelesaikan objektif")
    print("7. jawaban dipastikan tidak memiliki huruf kapital")
    print("Akan ada hadiah apabila anda berhasil menyelesaikan objektif, selamat mengerjakan!!\n\n")
    
def main():
    rule()
    nyawa = 3
    benar = 0
    start = time.time()
    while True:
        if nyawa == 0:
            print("anda gagal, silahkan coba lagi dilain waktu")
            exit(-1)
        n = random.randrange(len(db)-2)
        print(f"nyawa kamu tersisa {nyawa} lagi dan skor kamu sekarang adalah {benar}")
        print(db[n][0]+'?')
        inp = input("jawaban kamu : ")
        if inp == db[n][1]:
            benar = benar + 1
            if 100-benar != 0:
                print(f"Selamat jawaban anda benar")
            else:
                print(f"selamat anda berhasil memenangkan permainan, ini hadiah kamu")
                print(flag)
                exit(-1)
        else:
            print(f"jawaban kamu salah, jawaban yang benar adalah {db[n][1]}")
            nyawa = nyawa - 1
            benar = 0
        print()
        end = time.time()
        # print(end - start)
        if end-start > 60:
            print("mohon maaf waktu anda habis, silahkan coba lagi dilain waktu")
        
if __name__ == "__main__":
    main()