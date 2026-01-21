print("to jest kalkulator")

a = float(input("podaj A: "))
b = float(input("podaj B: "))
operacja = input("podaj operacje: ")
if operacja == "+":
    print(str(a) + " + " + str(b) + " = " + str(a + b) )
elif operacja == '-':
    print ( f'{a} - {b} = {a-b}')
elif operacja == '*':
    print ( f'{a} * {b} = {a*b}')
elif operacja == '/':
    if(b != 0):
        print ( f'{a} / {b} = {a/b}')
    else:
        print ("błąd w działaniu")


