"""
Fizz Buzz - SE O PARÂMETRO DA FUNÇÃO FOR DIVISÍVEL POR 2, RETORNE FIZZ, SE O PARAMETRO DA FUNCAO FOR DIVISIVEL POR 5 RETORNE BUZZ. SE O PARAMETRO DA FUNCAO FOR DIVISIVEL POR 5 E 3, RETORNE FIZZBUZ, CASO CONTRARIO RETORNE O NUMERO ENVIADO
"""
while True:
    num = int(input('digite um numero: '))

    def analise(valor = num):
        if num % 3 == 0 and num % 5 ==0:
            return 'FizzBuzz'
        
        elif num % 2 == 0:
            return 'Fizz'

        elif num % 5 == 0:
            return 'Buzz'
        
        else:
            return num

    print(analise())