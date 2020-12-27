#!/bin/python3
import os
from time import sleep
from sty import fg, Style, RgbFg

# Controllers
from lib import Bot

# Custom colors
fg.orange = Style(RgbFg(255, 150, 50))

os.system("clear")
sleep(1)
print(f"{fg.green} Selamat datang di Discord Logger")
sleep(0.5)
print(f"Ini adalah latihan menggunakan API dan belajar bahasa Python3{fg.rs}")
sleep(0.5)
print(f"\n{fg.cyan} Selamat mencoba!{fg.rs}")
sleep(2)
user_ops = input(f"\n\n[selfbot|bot] Konfirmasi user: ")
if user_ops.lower() == "bot":
  sleep(0.5)
  print(f"{fg.orange}Kamu memilih bot!{fg.rs}")
  sleep(0.5)
  print(f"Mohon tunggu 3 detik untuk proses ke menu bot!")
  sleep(3)
  Bot.start()
elif user_ops.lower() == "selfbot":
  print("Kamu memilih selfbot!")
  sleep(0.5)
  print(f"{fg.yellow}WARNING, Kamu harus menerima konsekuensi dari {fg.rs}{fg.cyan}https://discord.com/terms{fg.rs}")
  sleep(2)
  os.system("clear")
  print(f"{fg.red}SelfBot Maintenance!")
else:
  print(f"{fg.red}Kesalahan!\nMengulangi")
  sleep(0.5)
  os.system("python3 main.py")