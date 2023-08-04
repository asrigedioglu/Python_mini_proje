# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:55:37 2023

@author: agedioglu
"""

#KÖPRÜ GEÇİŞ ÜCRETİ

import datetime

hız_sınırı=120
otomobil_ücret=272.5
#hız = 112+ (x*2)

def köprü_gecis_ücreti(saat):
    
    hız = 112+(saat*2)
    print(f'Ortalama Hızınız: {hız}')
    
    arac=print(input("Araç çakarlı ise giriniz:(Y/N) "))
    
    if arac=="Y":
        print("Herhangi bir ücret ödemenize gerek yoktur.")
    
    else:
        if hız== hız<(hız_sınırı*0.10)+hız_sınırı:
            ücret=otomobil_ücret*0.50+otomobil_ücret
            print(f'Ortalama Hızınız: {hız}')
            print(f'Ödemeniz gereken ücret:{ücret}')
            
            
        elif hız==hız<(hız_sınırı*0.20)+hız_sınırı:
            ücret=otomobil_ücret*0.75+otomobil_ücret
            print(f'Ortalama Hızınız: {hız}')
            print(f'Ödemeniz gereken ücret:{ücret}')
            
        elif hız==hız>(hız_sınırı*0.20)+hız_sınırı:
            ücret=otomobil_ücret*0.150+otomobil_ücret
            print(f'Ortalama Hızınız: {hız}')
            print(f'Ödemeniz gereken ücret:{ücret}')
            
        elif hız== hız<hız_sınırı:
            print(f'Ortalama Hızınız: {hız}')
            print("Herhangi bir ücret ödemenize gerek yoktur.")

    return 

köprü = köprü_gecis_ücreti(22)
print(köprü)