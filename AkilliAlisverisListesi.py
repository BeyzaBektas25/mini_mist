AlısverisListesi=[]#boş liste
print("Alisveris listesine eklemek istediginiz urunleri yaziniz.")
print("Listeden urun çıkarmak için (-) ile urun adını yazınız. Cikmak isterseniz bitti yaziniz")

while True:#sonsuz döngü için
    urun=input("Ürün_Adı=")
    if urun=="bitti":
        break
    if urun in AlısverisListesi: #eğer ürün alişveriş listesi içinde ise bildir
        print(urun,"listede zaten mevcut")
        continue
    if urun.startswith("-"): # ürün (-) ile başlıyorsa o ürünü alışveriş listesinden sil
        silinecekUrun=urun[1:]
        if silinecekUrun in AlısverisListesi:
         AlısverisListesi.remove(silinecekUrun)
         print(silinecekUrun,"listeden silindi. Güncel liste->",AlısverisListesi)
    else:
        AlısverisListesi.append(urun)
    continue
print("Liste->",AlısverisListesi)