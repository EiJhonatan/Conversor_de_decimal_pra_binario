numeroDecimal= int(input('digite um numero decimal pra saber seu numero binário correspondente: '))


def decimal_para_binario(numeroDecimal):

    binario = ""

    while numeroDecimal > 0:
        binario = str(numeroDecimal % 2)+ binario
        numeroDecimal = numeroDecimal // 2
    return binario

binario = decimal_para_binario(numeroDecimal)

print(f"O número decimal {numeroDecimal} em binário é {binario}")