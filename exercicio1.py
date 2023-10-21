num1 = int(input("Digete o 1° numero: "))
num2 = int(input("Digete o 2° numero: "))
num3 = int(input("Digete o 3° numero: "))


if num1 > num2 and num1 > num3:
    maior = num1
    print('o maior numero é: ', num1)
elif num2 > num1 and num2 > num3:
     maior = num2
     print('o maior numero é: ', num2)
else:
     print('o maior numero é: ', num3)