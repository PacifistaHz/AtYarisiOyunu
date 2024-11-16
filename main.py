import tkinter as tk
import random
import time
from threading import Thread

class AtYarisiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("At Yarışı Uygulaması")
        self.root.geometry("820x500")  # Pencere boyutlarını ayarlayalım

        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack()

        self.track_height = 100
        self.bitis_cizgisi = 700
        self.canvas.create_line(self.bitis_cizgisi + 50, 20, self.bitis_cizgisi + 50, 380, fill="black", width=5)

        self.at1 = self.canvas.create_rectangle(20, 50, 70, 90, fill="red")
        self.at2 = self.canvas.create_rectangle(20, 50 + self.track_height, 70, 90 + self.track_height, fill="blue")
        self.at3 = self.canvas.create_rectangle(20, 50 + 2 * self.track_height, 70, 90 + 2 * self.track_height, fill="green")

        self.start_button = tk.Button(root, text="Yarışı Başlat", command=self.start_race, font=("Helvetica", 12))
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Yarışı Durdur", command=self.stop_race, font=("Helvetica", 12))
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Yarışı Sıfırla", command=self.reset_race, font=("Helvetica", 12))
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.winner_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.winner_label.pack(pady=20)

        self.stop_race_flag = False

    def move_at(self, at, step):
        self.canvas.move(at, step, 0)
        self.canvas.update()

    def start_race(self):
        self.stop_race_flag = False
        self.winner_label.config(text="")

        self.total_at1 = 0
        self.total_at2 = 0
        self.total_at3 = 0

        self.race_thread = Thread(target=self.run_race)
        self.race_thread.start()

    def run_race(self):
        while self.total_at1 < self.bitis_cizgisi and self.total_at2 < self.bitis_cizgisi and self.total_at3 < self.bitis_cizgisi:
            if self.stop_race_flag:
                break

            step1 = random.randint(1, 5)
            step2 = random.randint(1, 5)
            step3 = random.randint(1, 5)

            self.total_at1 += step1
            self.total_at2 += step2
            self.total_at3 += step3

            self.move_at(self.at1, step1)
            self.move_at(self.at2, step2)
            self.move_at(self.at3, step3)

            time.sleep(0.1)

        if not self.stop_race_flag:
            if self.total_at1 >= self.bitis_cizgisi:
                winner_text = "Kazanan: 1 numara!"
            elif self.total_at2 >= self.bitis_cizgisi:
                winner_text = "Kazanan: 2 numara!"
            else:
                winner_text = "Kazanan: 3 numara!"

            self.winner_label.config(text=winner_text)

    def stop_race(self):
        self.stop_race_flag = True
        self.winner_label.config(text="Yarış durduruldu!")

    def reset_race(self):
        self.stop_race_flag = True
        self.winner_label.config(text="")
        self.canvas.coords(self.at1, 20, 50, 70, 90)
        self.canvas.coords(self.at2, 20, 50 + self.track_height, 70, 90 + self.track_height)
        self.canvas.coords(self.at3, 20, 50 + 2 * self.track_height, 70, 90 + 2 * self.track_height)

if __name__ == "__main__":
    root = tk.Tk()
    app = AtYarisiApp(root)
    root.mainloop()
