print("Hesap makinesine Hoşgeldiniz")
while 1:
    print("*************************")
    print("Toplama için 1 e basın")
    print("Çıkarma için 2 ye basın")
    print("Çarpma için 3 basın")
    print("Bölme için 4 e basın")
    print("Hesap Makinesinden Çıkmak için 9 a basın")
    print("*************************")
    a=int(input("Seçiminizi Giriniz"))
    sonuc=0
    cikis=0

    if(a==1):
        print("Toplama işlemini seçtiniz")
        while 1:
            sonuc=0
            sayı=int(input("Kaç Sayı Toplamak İstediğinizi Giriniz"))
            while(sayı > 0):
                deger=int(input("{} . sayıyı giriniz".format(sayı)))
                sonuc=sonuc+deger
                sayı=sayı-1
            print("Sayıların toplamı : {}".format(sonuc))
            cikis=int(input("Toplama işleminden çıkmak için -1 e basınız"))
            if(cikis==(-1)):
                print("Toplama işleminden çıktınız")
                break
            else:
                print("Toplama işlemi yapmaya devam edebilirsiniz")
    if(a==2):
        print("Çıkarma işlemini seçtiniz")
        while 1:
            sonuc=0
            sayı=int(input("Kaç Sayı çıkarmak İstediğinizi Giriniz"))
            while(sayı > 0):
                deger=int(input("{} . sayıyı giriniz".format(sayı)))
                sonuc=sonuc-deger
                sayı=sayı-1
            print("Çıkarma işleminizi Sonucu : {}".format(sonuc))
            cikis=int(input("Çıkama işleminden çıkmak için -1 e basınız"))
            if(cikis==(-1)):
                print("Çıkarma işleminden çıktınız")
                break
            else:
                print("Çıkarma işlemi yapmaya devam edebilirsiniz")
    if(a==3):
        print("Çarpma işlemini seçtiniz")
        while 1:
            sonuc=1
            sayı=int(input("Kaç Sayı çarpmak İstediğinizi Giriniz"))
            while(sayı > 0):
                deger=int(input("{} . sayıyı giriniz".format(sayı)))
                sonuc=sonuc*deger
                sayı=sayı-1
            print("Çarpma işleminizi Sonucu : {}".format(sonuc))
            cikis=int(input("çarpma işleminden çıkmak için -1 e basınız"))
            if(cikis==(-1)):
                print("Çarpma işleminden çıktınız")
                break
            else:
                print("Çarpma işlemi yapmaya devam edebilirsiniz")
    if(a==4):
        print("Bölme işlemini seçtiniz")
        while 1:
            sayı=int(input("Kaç defa bölme işlemi yapmak İstediğinizi Giriniz"))
            sonuc=int(input("{}. sayıyı giriniz".format(sayı)))
            while(sayı > 1):
                deger=int(input("{} . sayıyı giriniz".format(sayı-1)))
                sonuc=sonuc/deger
                sayı=sayı-1
            print("Bölme işleminizi Sonucu : {}".format(sonuc))
            cikis=int(input("Bölme işleminden çıkmak için -1 e basınız"))
            if(cikis==(-1)):
                print("Bölme işleminden çıktınız")
                break
            else:
                print("Bölme işlemi yapmaya devam edebilirsiniz")
    if(a==9):
        print("Hesap makinesinde çıkış Yaptınız")
        break
    else:
        print("Yanlış bir tuşlama yaptınız....")