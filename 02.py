Faça um programa que receba do usuário uma string. O programa imprime a string sem suas vogais.

p=str(input())
p2=''

for i in p:
    if i=='a' or i=='e'or i=='i' or i=='o' or i=='u':
        i=''
    elif i=='A' or i=='E'or i=='I' or i=='O' or i=='U':
        i=''
    
        p2+=i
    else:
        p2+=i
print(p2)        
        
        
 
