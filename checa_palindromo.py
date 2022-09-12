#  Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”. Escreva um função que dado uma plavra verifique se ela é palindro.

def palindromo():
  palavra = input('insira uma palavra: ')
  if (palavra[::-1] == palavra):
    print('é um palíndromo')

  else: 
    print('não é um palíndromo')

palindromo() 