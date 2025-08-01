Faça um programa que receba uma palavra e um caractere (vogal ou consoante) e imprima quantas vogais (a, e, i, o, u) possui essa palavra. Substitua todas as vogais da palavra dada pelo caractere dado, e imprima a nova palavra.

palavra=str(input())
letra=str(input())
cont=0
nova_palavra=''

for i in palavra:
    if i=='a' or i=='e'or i=='i' or i=='o' or i=='u':
        nova_palavra+=letra
        cont+=1
    elif i=='A' or i=='E'or i=='I' or i=='O' or i=='U':
        cont+=1
        nova_palavra+=letra
    else:
        nova_palavra+=i
print(cont)        
print(nova_palavra)      
