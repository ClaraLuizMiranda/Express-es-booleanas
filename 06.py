Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
◦ Ter pelo menos 65 anos;
◦ Ou ter trabalhado pelo menos 30 anos;
◦ Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos


idade=int(input())
tempo=int(input())

if idade>=60 and tempo>=25:
    print('Pode se aposentar')
elif tempo>=30 or idade>= 65:
    print('Pode se aposentar')

else:
    print('Nao pode se aposentar')
