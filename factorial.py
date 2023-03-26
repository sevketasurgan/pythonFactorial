state = True
while state:
    factorial = 1
    num = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz : "))
    if (num > 10):
        print("Lütfen 10'dan küçük bir sayı giriniz ! ")
    else:
        for i in range(1, num+1):
            factorial *= i
        print(str(factorial))
        tekrar = int(
            input("Tekrar Hesaplamak ister misiniz ? (Evet '1' Hayır '0') : "))
        if tekrar == 1:
            state = True
        else:
            state = False
