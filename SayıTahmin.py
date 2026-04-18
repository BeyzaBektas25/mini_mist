import random 
print("(1-10 arası) Tuttuğum Sayıyı Tahmin Et Bakalım...")
r=random.randint(1,10)  #(1-10) arası random sayı üretir

tahminHakki=5  #tanınan hak sayısı
while tahminHakki>0:
    x=int(input(""))
    if x==r:
         print("TEBRİKLER! Doğru Bildiniz Tuttuğum Sayı",r,"idi")
    elif x<r:
         print("daha büyük bir sayı gerekiyor")
    else:
         print("daha küçük bir sayı gerekiyor")
    tahminHakki-=1 # tanınan hak sayısını 1 azalt
    print("kalan hakkınız:",tahminHakki)
if tahminHakki==0: #tüm ahkları bittiyse bildir
     print("Maalesef deneme hakkınız bitmiştir tuttuğum sayı",r,"idi")


