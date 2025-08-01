aça uma função que receba uma cadeia de caracteres no formato “DD/MM/AAAA” e retorne o dia, mês e ano para 3 variáveis inteiras. Nessa função, verifique se as barras estão no lugar certo, e se DD, MM e AAAA são numéricos. Caso alguma verificação não seja válida, os retornos devem ser iguais a zero.


def funcao(texto):
    dia = 0
    mes = 0
    ano = 0

    if len(texto) == 10 and texto[2] == '/' and texto[5] == '/':
        val1 = texto[0:2]
        val2 = texto[3:5]
        val3 = texto[6:10]

        if val1.isdigit() and val2.isdigit() and val3.isdigit():
            dia = int(val1)
            mes = int(val2)
            ano = int(val3)
    
    return dia, mes, ano
