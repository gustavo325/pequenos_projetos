import random

lista_numeros = []

def sorteio(x, n,n_min, n_max): 
    
    while x >= 1:
        lista = list(range(n_min,(n_max+1)))
        
        while len(lista_numeros) < n: 
            numero_sorteado = random.randint(n_min,n_max)
            
            for numero in lista:
                if numero == numero_sorteado:         
                    lista_numeros.append(numero)
                    lista.remove(numero_sorteado)
                    
        print('-'*(n*4))
        print(sorted(lista_numeros, key=int))
        lista_numeros.clear()
        x -=1
    print('-'*(n*4))
    

def questionario(): 
    
    x = int(input('Digite a quantidade de sorteios desejada\n'))
    return x

def questionario2(minimo, maximo):

    n = int(input("Digite a quantidade de números desejados nos jogos\n"\
                  f"mín: {minimo} e máx: {maximo}.\n"))
    while n < minimo or n > maximo: 
        n = int(input('Número inválido!\nDigite a quantidade de números '\
                     f'entre {minimo} e {maximo}.\n'))
    return n


def mensagem(jogo,
             minimo, 
             maximo, 
             max_acertos, 
             min_acertos,
             n_sort_min, 
             n_sort_max):
        print(f'Você escolheu {jogo}!\n'\
              f'Regra: Você escolhe no mínimo {minimo} e no máximo {maximo}'\
              f' números e ganha com {max_acertos} à {min_acertos} acertos.\n'\
              f'Números sorteados entre {n_sort_min} e {n_sort_max}')


# Início do programa... 

resposta = int(input('Bem vindo ao sorteador de números da loteria!\n'\
      'Abaixo estão os jogos disponíveis:\n'\
          'Selecione a opção desejada:\n'\
          '1 - Mega-sena\n'\
              '2 - Lotofacil\n'\
                  '3 - Quina\n'\
                      '4 - Lotomania\n'\
                          '5 - Timemania\n'\
                          '0 - Sair\n'))

# Menu do programa...    
    
while resposta != 0:     
    if resposta == 1: 
            
        mensagem(jogo = 'Mega-Sena',
                 minimo = 6, 
                 maximo = 20,
                 max_acertos = 6,
                 min_acertos = 4, 
                 n_sort_min = 1, 
                 n_sort_max = 60)
        
        sorteio(x = questionario(),
                n = questionario2(6,20), 
                n_min = 1,
                n_max = 60)
    
    if resposta == 2: 
        mensagem(jogo = 'Lotofacil',
                 minimo = 15, 
                 maximo = 20,
                 max_acertos = 15,
                 min_acertos = 11,
                 n_sort_min = 1,
                 n_sort_max = 25)
        
        sorteio(x = questionario(),
                n = questionario2(15,20),
                n_min = 1, 
                n_max = 25)
        
    if resposta == 3: 
        mensagem(jogo = 'Quina',
                 minimo = 5,
                 maximo = 15, 
                 max_acertos = 5, 
                 min_acertos = 2,
                 n_sort_min = 1,
                 n_sort_max = 80)
        
        sorteio(x = questionario(),
                n = questionario2(5,15),
                n_min = 1, 
                n_max = 80)
    
    if resposta == 4: 
        
        mensagem(jogo = 'Lotomania',
                 minimo = 50,
                 maximo = 50, 
                 max_acertos = 20, 
                 min_acertos = 15,
                 n_sort_min = 0,
                 n_sort_max = 99)
        
        sorteio(x = questionario(),
                n = questionario2(50,50),
                n_min = 0, 
                n_max = 99)
    
    if resposta == 5: 
        mensagem(jogo = 'Timemania',
                 minimo = 10,
                 maximo = 10, 
                 max_acertos = 7, 
                 min_acertos = 3,
                 n_sort_min = 1,
                 n_sort_max = 80)
        
        sorteio(x = questionario(),
                n = questionario2(10,10),
                n_min = 1, 
                n_max = 80)
        
        print('Agora basta escolher o time do coração em cada jogo do '\
              'timemania e apostar!')
        
    
    resposta = int(input('Escolha uma das opções abaixo:\n'\
          '1 - Mega-sena\n'\
              '2 - Lotofacil\n'\
                  '3 - Quina\n'\
                      '4 - Lotomania\n'\
                          '5 - Timemania\n'\
                          '0 - Sair\n'))



