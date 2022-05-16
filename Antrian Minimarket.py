# untuk memasukan program Queue
import queue

# kerangka untuk membuat objek
class myQueue:
    def __init__(self):
        self.items = queue.Queue()

    # memeriksa apakah antrian sedang kosong
    def isEmpty(self):
        return self.items.empty()

    # memasukan data ke antrian
    def enqueue(self, items):
        self.items.put(items)

    # mengeluarkan data dari antrian
    def dequeue(self, items):
        if not self.items.empty():
            return self.items.get()
        else:
            return "Data Antrian Kosong"
 
    # panjang dari antrian
    def size(self):
        return self.items.qsize()

    # main menu dari aplikasi
    def mainmenu(self):
        pilih = "mainmenu"
        # untuk pengulangan suatu blok kode program
        while (pilih == "mainmenu"):
            print("==============================")
            print("         Toko Herry           ")
            print("==============================")
            print("1. Masuk Antrian")
            print("2. Keluar Antrian")
            print("3. Cek Antrian")
            print("4. Banyak Antrian")
            print("5. Keluar")
            print("==============================")
            pilihan = str(input("Silahkan Masukan Pilihan Anda :"))   
            # variable pilihan akan dipanggil melalui fungsi if elif else
            # sebagai pengambilan keputusan 
            if(pilihan == "1"):
                object = str(input("Masukan Nama Anda :"))
                self.enqueue(object)
                print("Nama " + object+ " Telah Masuk Antrian")
                x = input("")
            elif(pilihan == "2"):
                object = self.dequeue ( object)
                if object != "Data Antrian Kosong":
                    print("Nama " + object + " Telah Keluar Antrian")
                else:
                    print("Antrian Kosong")
                x = input("")
            elif(pilihan == "3"):
                print(self.isEmpty())
                x = input("")
            elif(pilihan == "4"):
                print("panjang Antrian adalah : " +str(self.size()))
                x = input("")
            elif(pilihan == "5"):
                print("Terima Kasih Sudah Mampir Di Toko Kami")
                print(quit())
            else:
                pilih="mainmenu"

# untuk mendefinisikan class agar objek terbentuk
if __name__ == "__main__":
         q=myQueue()
         q.mainmenu()



