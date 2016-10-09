#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

karekok_kare_ico = """
#########################################################
#         PYTHON - KAREKÖK KARE - GH0ST S0FTWARE        #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

islemler_ico = """
(1) Karekök Bul
(2) Karsini Bul
(3) Çıkış
"""

star = "#########################################################"

print karekok_kare_ico

print islemler_ico

print star

islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")

def karekok():
		sayi_1_karekok = input("Karekökünü hesaplamak istediğiniz sayı: ")
		sonuc_karekok = int(sayi_1_karekok) ** 0.5
		print "Girilen sayının karekökü : ", sonuc_karekok

def kare():
		sayi_1_kare = input("Karesini hesaplamak istediğiniz sayı: ")
		sonuc_kare = int(sayi_1_kare) ** 2
		print "Girilen sayının karesi : ", sonuc_kare

if islem == 1:
	print star
	karekok()
	print star
	
elif islem == 2:
	print star
	kare()
	print star
	
elif islem == 3:
	sys.exit()
	print star
