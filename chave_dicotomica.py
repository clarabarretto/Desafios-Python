# Construa uma pequena chave dicotômica para identificar uma determinada planta como membro de um dos principais grupos: Bryophyta, Pteridophyta, Gymnospermae ou Angiospermae. A identificação se dá com base na presença (1) ou ausência (0) de três caracteres: vascularização, sementes e flores. Utilize a tabela abaixo como referência.

# Grupo	        Vascularização	Sementes	Flores
# Bryophyta	           0	       0	      0
# Pteridophyta	       1	       0	      0
# Gymnospermae	       1	       1	      0
# Angiospermae	       1	       1	      1

def plantas():
  print('0 = ausente e 1 = presente')
  vasc = int(input('sua planta é vascularizada?: '))
  if (vasc == 0):
    return('bryophyta')
  semente = int(input('sua planta tem sementes?:'))
  if (vasc == 1 and semente == 0):
    return('pteridophyta')
  flores = int(input('sua planta tem flores?: '))
  if (semente == 1 and flores == 0):
    print('gymnosperme')

  else:
    print('angiospermaee')  
    

plantas()
