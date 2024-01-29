def topla(x, y):
    result = x + y
    print(result)
    return result

def cikar(x, y):
    result = x - y
    print(result)
    return result

def carp(x, y):
    result = x * y
    print(result)
    return result

def bol(x, y):
    if y != 0:
        result = x / y
        print(result)
        return result
    else:
        print("Error: Division by zero!")
        return None

while True:
    islem = input("Yapılacak işlemi giriniz (+, -, *, /) veya 'exit' yazarak çıkış yapın: ").lower()

    if islem == 'exit':
        print("Programdan çıkılıyor.")
        break

    x = int(input("İlk sayıyı giriniz: "))
    y = int(input("İkinci sayıyı giriniz: "))

    if islem == '+':
        topla(x, y)
    elif islem == '-':
        cikar(x, y)
    elif islem == '*':
        carp(x, y)
    elif islem == '/':
        bol(x, y)
    else:
        print("Geçersiz işlem!")
