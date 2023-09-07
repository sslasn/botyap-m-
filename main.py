import random

kazanilan_oyunlar = 0
toplam_oyunlar = 0
botlar = {
    "Bot1": ["Taş", "Kağıt", "Makas"],
    "Bot2": ["Kağıt", "Makas", "Taş"],
    "Bot3": ["Makas", "Taş", "Kağıt"],
    "Bot4": ["Kağıt", "Kağıt", "Makas"]
}
while toplam_oyunlar < 4:
    bot_secimi = random.choice(["Taş", "Kağıt", "Makas"])
    kullanici_secimi = input("Taş, Kağıt veya Makas seçin: ")
    if kullanici_secimi not in ["Taş", "Kağıt", "Makas"]:
        print("Geçersiz seçim! Lütfen Taş, Kağıt veya Makas seçin.")
        continue
    print(f"Bot'un seçimi: {bot_secimi}")
    print(f"Kullanıcının seçimi: {kullanici_secimi}")
    if bot_secimi == kullanici_secimi:
        print("Berabere!")
    elif (bot_secimi == "Taş" and kullanici_secimi == "Makas") or (bot_secimi == "Kağıt" and kullanici_secimi == "Taş") or (bot_secimi == "Makas" and kullanici_secimi == "Kağıt"):
        print("Bot kazandı!")
    else:
        print("Kullanıcı kazandı!")
        kazanilan_oyunlar += 1
    toplam_oyunlar += 1
kazanma_orani = kazanilan_oyunlar / 4
if kazanma_orani >= 0.6:
    print(f"Başarı! Programınız {kazanma_orani*100}% oranında kazandı.")
else:
    print(f"Başarısız! Programınız {kazanma_orani*100}% oranında kazandı.")


