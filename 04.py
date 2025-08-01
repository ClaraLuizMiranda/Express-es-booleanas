Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.

numero=int(input())

if numero%5==0 and numero%3==0:
    print('False')

elif numero%5==0 or numero%3==0:
    print('True')

else:
    print('False')
