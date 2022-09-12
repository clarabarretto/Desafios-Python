#  Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: - salário bruto. - quanto pagou ao INSS. - quanto pagou ao sindicato. - o salário líquido. - calcule os descontos e o salário líquido, conforme a tabela abaixo:

#             + Salário Bruto : R$
#             - IR (11%) : R$
#             - INSS (8%) : R$
#             - Sindicato ( 5%) : R$
#             = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


def salario():
  hora = float(input('quanto você ganha por hora?: '))
  numhora = int(input('quantas horas você trabalha por mês?: '))
  salariobruto = numhora*hora
  print('o salário bruto é: ', salariobruto)
  IR = (salariobruto)*0.11
  print('o valor pago ao IR é: ', IR)
  INSS = (salariobruto)*0.08
  print('o valor pago ao INSS é:', INSS)
  Sindicato = (salariobruto)*0.05
  print('o valor pago ao sindicato é: ', Sindicato)
  SL = salariobruto - (IR + INSS + Sindicato)
  print('o salário liquido é:', SL)

salario()