from time import sleep

cores = {'verde':'\033[1;42m', 
         'azul':'\033[1;44m', 
         'branco':'\033[1;47m',
         'vermelho':'\033[1;41m',  
         'semCor':'\033[m'}


def titulo(msg, cor):
    print(cor)
    print('~' * (len(msg) +4))
    print(f'  {msg}  ')
    print('~' * (len(msg) + 4))
    print(cores['semCor'])

def ajuda(comando, cor):
    print(cor)
    print(help(comando))
    print(cores['semCor'])


while True:
    titulo('SISTEMA DE AJUDA PYTHON', cores['verde'])

    função = input('Função ou biblioteca => ')

    if função == 'FIM' or função == 'fim':
        break

    titulo('Analisando função...', cores['azul'])
    sleep(1)
    ajuda(função, cores['branco'])
    sleep(1)

titulo('ENCERRANDO... ATÉ MAIS', cores['vermelho'])
