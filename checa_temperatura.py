# Implemente um programa que possa receber do usuário a temperatura em graus Celsius ou Fahrenheit. Antes de receber a temperatura, pergunte ao usuário se ele deseja inserir em Celsius ou em Fahrenheit. Se a entrada for em graus Celsius, o programa deverá retornar a temperatura em Fahrenheit. Se a entrada for em Fahrenheit, o programa deverá retornar a temperatura em Celsius.

def temp():
  print('digite 1 para celsius ou 0 para fahrenheit')
  medidor = int(input('a temperatura será em celsius ou fahrenheit?: '))
  if (medidor == 1):
    cel = float(input('a temperatura é: '))
    print('a temperatura em fahrenheit é: ', (cel * 1.8) + 32 )

  elif (medidor == 0):
    fa = float(input('a temperatura é'))
    print('a temperatura em celsius é: ', (fa - 32)/ 1.8)  

temp() 