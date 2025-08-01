Faça uma função que receba 2 números inteiros positivos e calcule o Máximo Divisor Comum (MDC).

def funcao(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1

    if num1 < num2:
        menor = num1
    else:
        menor = num2

    mdc = 1
    
    for div in range(menor, 0, -1):
        div1 = (num1 % div == 0)
        div2 = (num2 % div == 0)

        if div1 and div2:
            mdc = div
            break

    return mdc
