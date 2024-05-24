# JOGO DE ADIVINHACAO
import random

# INFORMANDO SOBRE AS REGRAS DO JOGO
print("JOGO DE ADVINHAÇÃO - ESCOLHA UM NÚMERO E VOCÊ TEM 10 TENTATIVAS PARA ACERTÁ-LO!\n")
input("PRESSIONE ENTER PARA INICIAR\n")

tentativas: int = 10
valor_para_advinhar: int = random.randrange(1, 100)
resultado: bool = False

while tentativas > 0:
    valor_do_usuario: int = int(input("DIGITE UM NÚMERO ENTRE 1 E 100: "))

    if valor_do_usuario > valor_para_advinhar:
        print("\nO NÚMERO DIGITADO É MAIOR QUE O VALOR PARA ADVINHAR")

    if valor_do_usuario < valor_para_advinhar:
        print("\nO NÚMERO DIGITADO É MENOR QUE O VALOR PARA ADVINHAR")

    if valor_do_usuario == valor_para_advinhar:
        resultado = True
        break

    tentativas-=1
    print(f"QUANTIDADE DE TENTATIVAS RESTANTES: {tentativas}\n")


if resultado:
    print("\nVOCÊ ACERTOU O NÚMERO, PARABENS!\n")
else:
    print("\nINFELIZMENTE VOCÊ PERDEU!\n")
    
print(f"VOCÊ ESCOLHEU: {valor_do_usuario}")
print(f"NÚMERO PARA ADIVINHAR: {valor_para_advinhar}\n")