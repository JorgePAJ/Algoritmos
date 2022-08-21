def cambio(money, moneyArray):
    if money >= 20:
        moneyArray[0] = money // 20
        cambio(money - moneyArray[0] * 20, moneyArray)
    elif money >= 10:
        moneyArray[1] = money // 10
        cambio(money - moneyArray[1] * 10, moneyArray)
    elif money >= 5:
        moneyArray[2] = money // 5
        cambio(money - moneyArray[2] * 5, moneyArray)
    elif money >= 2:
        moneyArray[3] = money // 2
        cambio(money - moneyArray[3] * 2, moneyArray)
    elif money >= 1:
        moneyArray[4] = money // 1
        cambio(money - moneyArray[4] * 1, moneyArray)


price = float(input("Ingrese el precio: "))
money = float(input("Ingrese la cuanto dinero usara para pagar: "))
moneyArray = [0, 0, 0, 0, 0]

if money < price:
    print("No se puede pagar el precio")
elif money == price:
    print("Pago exacto")
else:
    cambio(money - price, moneyArray)
print("$20|$10|$5|$2|$1")
print(moneyArray)
