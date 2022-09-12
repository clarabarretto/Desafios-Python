# Escreva um programa que verifique se determinada entrada de usuário é um número. Considere válido números interios e reais, positivos e negativos, como: 10, -20, 103.0, -12.5

def entrada():
  digi = '1'
  if(digi != '0'):
    digi = input('digite algo: ')
    try:
      print(float(digi),' é um número')
    except ValueError:
      print(digi, 'É uma string')

entrada()  