# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 19:36:53 2022

@author: nodir
"""

juft_sonlar=list(range(120,1201,2))
katta=max(juft_sonlar)
kichik=min(juft_sonlar)
ayirma=katta-kichik


davlatlar=["Anglya","Ispanya","Italia","Germanya","Amerika","Korea","Iroq","Kanada","Fransiya","Malayziya"]
taomlar=["osh","manti","sho'rva","somsa","shashlik"]
nonushta=taomlar[:]
nonushta.remove("shashlik")
nonushta.remove("sho'rva")
nonushta.append("sut")
nonushta.append("tost non")
nonushta[0]="qaymoq va non"
print(nonushta)
