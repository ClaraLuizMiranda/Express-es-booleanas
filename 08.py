Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.

cont=0

for i in range(1, 1000):
    if i%5==0 or i%3==0:
        cont+=i
print(cont)        
