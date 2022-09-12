# Crie um programa que criptografe um texto segundo a Cifra de Cesar.

def cesar():
  alfabeto = 'abcdefghijklmnopqrstuvwyz'
  texto = (input('digite algo: '))
  chave = int(input('escolha a chave: '))
  b = ' '
  for letra in texto:
    index = alfabeto.find(letra)
    if index == -1:
      b += letra
    else: 
      cripto = index + chave 
      cripto = cripto % len(alfabeto)
      b += alfabeto[cripto:cripto+1]
  return b  

cesar()