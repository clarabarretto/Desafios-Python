# Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra. Imprima a string resultante.

def ascii():
  palavra = input("escreva algo: ")
  base = ""
  for i in palavra:
    base += chr(ord(i)+1)
  print(base)

ascii()