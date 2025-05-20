# 1 def soma (numeroA,numeroB,):
 resultado= numeroA + numeroB
 print(f"O resultado da soma é:{resultado}")

def subtracao (numeroA, numeroB ):
  resultado = numeroA - numeroB
  print(f'o resultado da subtração é: {resultado}')
 
def multiplicacao(numeroA, numeroB):
  resultado = numeroA * numeroB
  print(f"O resultado da multiplicacao é:{resultado}")

def divisao(numeroA, numeroB):
  resultado =  numeroA / numeroB
  print(f"O resultado da divisão é: {resultado}")

def raizquadrada( numeroA, numeroB):
  resultado = numeroA ** 0,5
  print(f"O resultado da raíz quadrada é: {resultado}")

opcao= int(input("Menu : 1. SOMA \n 2. SUBTRAÇÃO \n 3. MULTIPLICAÇÃO \n 4. DIVISÃO \n 5. RAIZQUADRADA"))

if (opcao == 1 ):
  numeroA = float(input("Digite o 1 º número:"))
  numeroB = float(input("Digite o 2ºnumero:"))
  soma ( numeroA, numeroB )

elif (opcao == 2 ) :
  numeroA = float(input("Digite o 1º número:"))
  numeroB = float(input("Digite o  2º numero:"))
  subtracao ( numeroA, numeroB)

elif (opcao == 3 ) :
  numeroA = float(input("Digite o 1º número:"))
  numeroB = float(input("Digite o 2º número:"))
  multiplicacao (numeroA, numeroB)

elif (opcao == 4 ) :
  numeroA = float( input("Digite o 1º número:"))
  numeroB = float(input("Digite o 2º número:"))
  divisao ( numeroA , numeroB)

elif (opcao == 5 ) :
  numeroA = float(input("Digite o 1º número:"))
  numeroB = float(input("Digite o 2º número"))
  raizquadrada( numeroA )
