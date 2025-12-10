# Importa o módulo 'random' para a escolha aleatória do computador
import random

def determinar_vencedor(utilizador, computador):
    """
    Função para determinar o vencedor de uma ronda de Pedra, Papel e Tesoura.
    R: Pedra | P: Papel | T: Tesoura
    """
    # Condição de Empate
    if utilizador == computador:
        return "Empate"

    # Condições de Vitória para o Utilizador
    # Pedra (R) ganha Tesoura (T)
    # Papel (P) ganha Pedra (R)
    # Tesoura (T) ganha Papel (P)
    if (utilizador == 'R' and computador == 'T') or \
       (utilizador == 'P' and computador == 'R') or \
       (utilizador == 'T' and computador == 'P'):
        return "Utilizador"
    else:
        # Se não é empate nem vitória do utilizador, é vitória do computador
        return "Computador"

def jogar_pedra_papel_tesoura():
    """
    Função principal que executa o jogo em loop.
    """
    # Mapeamento das opções para facilitar a leitura na saída
    opcoes = {
        "R": "Pedra",
        "P": "Papel",
        "T": "Tesoura"
    }
    # Lista de opções para o computador
    escolhas_validas = list(opcoes.keys())

    print("--- Jogo: Pedra, Papel e Tesoura ---")
    print("Regras: R = Pedra | P = Papel | T = Tesoura | Q = Sair")

    while True:
        # Pede a entrada do utilizador e converte para maiúsculas
        escolha_utilizador = input("\nFaça a sua escolha (R/P/T) ou 'Q' para sair: ").upper()

        if escolha_utilizador == 'Q':
            print("Obrigado por jogar! Até à próxima.")
            break

        # Validação da entrada
        if escolha_utilizador not in escolhas_validas:
            print("Escolha inválida. Por favor, use R, P, T, ou Q.")
            continue

        # Escolha aleatória do computador
        escolha_computador = random.choice(escolhas_validas)

        # Apresentar as escolhas
        print(f"\nA sua escolha: {opcoes[escolha_utilizador]}")
        print(f"Escolha do Computador: {opcoes[escolha_computador]}")

        # Determinar e apresentar o resultado
        resultado = determinar_vencedor(escolha_utilizador, escolha_computador)

        if resultado == "Empate":
            print("Resultado: Empate!")
        elif resultado == "Utilizador":
            print("Resultado: Parabéns! Você ganhou!")
        else:
            print("Resultado: O computador ganhou! Tente de novo.")

# Garante que a função principal é chamada quando o script é executado
if __name__ == "__main__":
    jogar_pedra_papel_tesoura()