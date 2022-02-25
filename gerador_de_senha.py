def gerador_de_senha():
    import random
    letra_minuscula = 'abcdefhijkmnopqrstuvxwyz'
    letra_maiuscula =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '1234567890'
    simbolos = '<=>?!@[\/](^)_`{|}~.+-*&%$#'
    juncao = letra_minuscula + letra_maiuscula + numeros + simbolos

    tamanho = int(input('Você quer gerar uma senha com quantos caractéres? ')) 
    senha = ''.join(random.sample(juncao, tamanho))
    print(senha)

if __name__ == '__main__':
    gerador_de_senha()       
