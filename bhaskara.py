from math import sqrt

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
print('')
delta = (b**2) - (4 * a * c)

if a == 0:
    print('A variavel A precisa ser um valor maior ou menor que 0')

elif delta < 0:
    print('Delta = {}'.format(delta))
    print('Não possui raizes reais!')

else:
    x1 = (-b + (sqrt(delta))) / (2 * a)
    x2 = (-b - (sqrt(delta))) / (2 * a)

    print('Delta = {}'.format(delta))
    print('x1 = {}'.format(x1))
    print('x2 = {}'.format(x2))

input("\nPressione <ENTER> para encerrar!")
