#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quantum Kedi Mazeret Üreteci v0.0.0.0.1
Schrödinger'ın kedisi işe geç kaldığında bu kodu çalıştırın.
Kedi kutunun içinde hem mazeret üretiyor hem de üretmiyor.
"""

import random
import time

def kuantum_superpozisyon():
    durumlar = ["ölü", "diri", "geç kaldı", "hiç gitmedi", "kutunun içinde uyuyor"]
    return random.choice(durumlar)

def mazeret_uret(isim="patron"):
    kedi_durumu = kuantum_superpozisyon()
    mazeretler = [
        f"Kuantum dolanıklığı yüzünden kedi hem evde hem işteydi, {isim} Bey/Hanım. Ölçüm yaptığımda geç kaldığı çıktı.",
        f"Schrödinger deneyi başarısız oldu çünkü kedi kutuyu açıp çay molasına çıktı. {kedi_durumu} durumda.",
        f"Heisenberg belirsizlik ilkesine göre konumumu ve momentumumu aynı anda bilemem. Dolayısıyla işe gelirken nerede olduğumu bilmiyordum.",
        f"Kedi gözlemci olduğu için dalga fonksiyonu çöktü ve ben geç kaldım. Bu tamamen fizik.",
        f"Paralel evrende zamanında geldim. Bu evrende kedi beni alıkoydu. {kedi_durumu} kanıt.",
        f"Kuantum tünelleme ile işe gelmeye çalıştım ama duvar kalın çıktı. Kedi de yardım etmedi."
    ]
    return random.choice(mazeretler)

if __name__ == "__main__":
    print("Kuantum Mazeret Motoru çalışıyor...")
    time.sleep(0.5)  # Kuantum gecikme
    print(mazeret_uret())
    print("\nNot: Bu mazeret hem geçerli hem geçersizdir. Gözlemleyene kadar.")

# Gizli not: VGF0aWsgdml6eW9uIHN1IGFsdGFueSBnb2xlciB5b2x1bmRhIGRpciBnaWJpdGxlciB0b3BsdW1hc2kgZ2VyZWtpci4=  # base64: Atatürk vizyonu su altına göler yolunda dir gibitler toplumasi gerekir. (yanlış yazılmış absürt)