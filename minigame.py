from random import choice

comp_vitorias = 0
jogador_vitorias = 0

def Opcao_Jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    if esc_jogador in ["Pedra", "PEDRA", "pedra"]:
        esc_jogador = "pedra"
    elif esc_jogador in ["Papel", "PAPEL", "papel"]:
        esc_jogador = "papel"
    elif esc_jogador in ["Tesoura", "TESOURA", "tesoura"]:
        esc_jogador = "tesoura"
    else:
        print("Opcao invalida. Tente novamente")
        Opcao_Jogador()
    return esc_jogador

def Opcao_Computador():
    esc_computador = choice(["pedra", "papel", "tesoura"])
    return esc_computador

while True:

    print("-----------------------------")

    esc_computador = Opcao_Computador()
    esc_jogador = Opcao_Jogador()

    print("-----------------------------")

    #Jogador Ganha
    if(esc_jogador == "papel") and (esc_computador == "pedra") or (esc_jogador == "pedra") and (esc_computador == "tesoura") or (esc_jogador == "tesoura") and (esc_computador == "papel"):
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_computador}. Resultado: Voce ganhou!")
        jogador_vitorias += 1

    #Jogador empata com a maquina    
    elif esc_jogador == esc_computador:
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_computador}. Resultado: Empate!")
        
    #Jogador Perde    
    else:
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_computador}. Resultado: Voce perdeu!")
        comp_vitorias =+ 1

    print("-----------------------------")

    print(f"Vitorias do jogador: {jogador_vitorias}")
    print(f"Vitorias da Maquina: {comp_vitorias}")

    print("-----------------------------")

    esc_jogador = input("Voce quer jogar novamente (S/N): ")
    if esc_jogador in ["SIM", "sim", "Sim", "S", "s"]:
        pass
    elif esc_jogador in ["NAO", "nao", "Nao", "N", "n"]:
        break
    else:
        break

