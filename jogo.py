import random

def jogar():
    print("-" * 30)
    print("BEM-VINDO AO ADIVINHA-BOT!")
    print("-" * 30)
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        try:
            palpite = int(input("Chute um número entre 1 e 100: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Mais alto... Tente novamente!")
            elif palpite > numero_secreto:
                print("Mais baixo... Tente novamente!")
            else:
                print(f"\nPARABÉNS! Você acertou em {tentativas} tentativas.")
                acertou = True
        except ValueError:
            print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    jogar()