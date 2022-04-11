import random

rus = ["Аа","Бб","Вв","Гг","Дд","Ее","Ёё","Жж","Зз","Ии","Йй","Кк","Лл","Мм","Нн","Оо","Пп","Рр","Сс","Тт","Уу","Фф","Хх","Цц","Чч","Шш","Щщ","Ъъ","Ыы","Ьь","Ээ","Юю","Яя"]
latin = ["a","b","v","g","d","ye","yo","j","z","i","iy","k","l","m","n","o","p","r","s","t","u","f","h","ts","ç","şe","şa","sertleştirme","ı","yumuşatma","e","yu","ya"]


def _harf_tahmin():
    devam = 'e'
    while devam != ('h' or 'H' or "hayır" or "Hayır" or "HAYIR" or "hayir" or "Hayir" or "HAYİR"):
        harf = rus[random.randrange(33)]
        print(harf)
        tahmin = input("Tahminin: ")
        try:
            if latin.index(tahmin) == rus.index(harf):
                print("Dogru cevap!\n----------------------------------------------------")
            else:
                print('Ding dong... Yanlış cevap\nDoğru cevap "{}" idi..."'.format(latin[rus.index(harf)]))
                devam = input("Devam etmek ister misin? (e/h)")
        except ValueError:
                print('Ding dong... Yanlış cevap\nDoğru cevap "{}" idi..."'.format(latin[rus.index(harf)]))
                devam = input("Devam etmek ister misin? (e/h)")

def switch_demo(argument):
    switcher = {
    1: _harf_tahmin()
}
tercih = input("""
----------------------------------------------------
Mod seçin:
1 - Harf Tahmin
2 - Kelime Okuma
3 - Sık Kullanılan Kelime Tahmin
Tercihiniz: """)
switch_demo(tercih)