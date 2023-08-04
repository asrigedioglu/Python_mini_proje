#KREDİ FAİZİ HESAPLAMA

import numpy_financial as npf


#TAKSİT TUTAR = KREDİ TUTARI * FAİZ * (1+ FAİZ)^TAKSİT SAYISI /
 #(1+ FAİZ)^TAKSİT SAYISI) - 1 
 
 '''
 KREDİ TUTARI = A
 FAİZ = r
 TAKSİT SAYISI = t
 
 '''
 
 class banka():
     
     def __init__(self,a,r,t):
         self.a=a
         self.r=r
         self.t=t
         
     def taksit(self):
         
         taksit_tutarı = self.a*self.r*(1+self.r)**self.t/(1+self.r)**(self.t-1)
         print(f'Ödemeniz gereken aylık taksit : {taksit_tutarı}')
      
     def total_faiz(self):
         taksit_tutarı = self.a*self.r*(1+self.r)**self.t/(1+self.r)**(self.t-1)
         print(f'Total geri ödemeniz : {taksit_tutarı*self.t}')
          
akbank=banka(100000, 0.015, 52)

akbank.total_faiz(()
akbank.taksit()   


          
    
     
