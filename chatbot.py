# chatbot projesi,

import random
# sozluk = {key : value}
hobiler = [
    "Oyun Geliştirmek",
    "Aile ile zaman geçirmek",
    "Kitap okumak",
    "basketbol oynamak",
    "yüzmek",
    "tenis oynamak",
    "doğa yürüyüşü",
    "futbol oynamak",
    "voleybol oynamak",
    "kodlamak",
    "kitap okumak",
    "sohbet etmek",
    "arkadaşlar ile vakit geçirmek",
    "Yürüyüş yapmak",
    "Kitap okumak",
    "Müzik dinlemek",
    "Yoga yapmak",
    "Resim çizmek",
    "Film izlemek",
    "Bisiklete binmek",
    "Bahçe işleri yapmak",
    "Yemek yapmak",
    "Dans etmek"
]

yemekler = ["Pizza", "Hamburger", "Spaghetti", "Sushi", "Tacos", "Kebap", "Çin Yemeği", "Hint Yemeği", "Fransız Mutfağı", "İtalyan Mutfağı", "Meksika Mutfağı", "Japon Mutfağı", "Tay Mutfağı", "Yunan Mutfağı", "Kore Mutfağı", "Arap Mutfağı", "İspanyol Mutfağı", "Alman Mutfağı", "Rus Mutfağı", "Brezilya Mutfağı"]


cevaplar = {
    "merhaba" : "Merhaba. Size nasıl yardımcı olabilirim?",
    "nasılsın" : "Ben bir chatbotum, bu yüzden duygularımı söylemem ama size yardımcı olmaktan mutluluk duyarım!",
    "havalar nasıl" : "Üzgünüm, hava durumu hakkında bilgi veremem",
    "hobilerin nedir" : "Müzik çalabilirim, kod yazabilirim, cevap verebilirim",
    "bye bye" : "Görüşürüz. Sizinle konuşmak güzeldi",
    "yemek öner" : yemekler,
    "kahvaltı öner" : "",
    "film öner" : "",
    "hobi öner" : hobiler,
    "spor öner" : "",
    "oyun öner" : "",
    "müzik öner" : "",
    "ders çalışma programı öner" : "",
    "seyehat öner" : ""
}




# kullanıcıyla etkileşim
while True:
    soru = input("Sorunuz : ").lower() # büyük karakterleri küçültüyor

    
    if soru[-4:] == "öner":
        hobi = random.choice(cevaplar[soru])
        print(hobi)

    elif soru in cevaplar:
        print("Cevap : ", cevaplar[soru])

    elif soru == "çıkış":
        print("Oturumu kapatıyorum. İyi günler")
        break
    else:
        print("Üzgünüm. Bu soruyu cevaplayamadım. Başka nasıl yardımcı olabilirim?")

