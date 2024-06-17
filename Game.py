import random

# Grupos
classes_disponiveis = ["Paladino", "Mago", "Tank", "Atirador", "Assassino"]
armas_disponiveis = ["Espada", "Varinha", "Escudo", "Canhão de mão", "Adaga", "Clava", "Arco encantado"]

# Tabela de pontuação base (classe + arma)
tabela_pontos = {
    "Paladino": {"Espada": 6000, "Varinha": 1000, "Escudo": 5000, "Canhão de mão": 1000, "Adaga": 1000, "Clava": 4000, "Arco encantado": 1000},
    "Mago": {"Espada": 1000, "Varinha": 6000, "Escudo": 1000, "Canhão de mão": 1000, "Adaga": 1000, "Clava": 1000, "Arco encantado": 5000},
    "Tank": {"Espada": 4000, "Varinha": 1000, "Escudo": 6000, "Canhão de mão": 1000, "Adaga": 1000, "Clava": 5000, "Arco encantado": 1000},
    "Atirador": {"Espada": 1000, "Varinha": 2000, "Escudo": 1000, "Canhão de mão": 6000, "Adaga": 1000, "Clava": 1000, "Arco encantado": 5000},
    "Assassino": {"Espada": 5000, "Varinha": 1000, "Escudo": 1000, "Canhão de mão": 1000, "Adaga": 6000, "Clava": 1000, "Arco encantado": 1000}
}

# Funções
def escolher_classe():
    print("Escolha uma classe")
    for i, classe in enumerate(classes_disponiveis, start=1):
        print(f"{i}. {classe}")
    escolha = int(input("Digite o número da classe escolhida: "))
    if 1 <= escolha <= len(classes_disponiveis):
        return classes_disponiveis[escolha - 1]
    else:
        print("Escolha inválida, tente novamente.")
        return escolher_classe()

def escolher_arma():
    print("Escolha uma arma")
    for i, arma in enumerate(armas_disponiveis, start=1):
        print(f"{i}. {arma}")
    escolha = int(input("Digite o número da arma escolhida: "))
    if 1 <= escolha <= len(armas_disponiveis):
        return armas_disponiveis[escolha - 1]
    else:
        print("Escolha inválida, tente novamente.")
        return escolher_arma()

def calcular_pontos(classe, arma):
    pontos_base = tabela_pontos.get(classe, {}).get(arma, 0)
    if pontos_base == 0:
        print("Combinação de classe e arma não dá pontos específicos, usando pontuação padrão.")
        pontos_base = 1000  # Pontuação padrão para combinações não especificadas
    return pontos_base

def adicionar_pontos_aleatorios(pontos):
    if pontos < 8000:
        pontos_aleatorios = random.choice([1000, 2000, 3000, 4000])
        pontos += pontos_aleatorios
    return pontos

# Configuração do Input
nome_heroi = input("Digite o nome do herói: ")
classe_heroi = escolher_classe()
arma_heroi = escolher_arma()

# Calcular os pontos
pontos_base = calcular_pontos(classe_heroi, arma_heroi)
xp_heroi = adicionar_pontos_aleatorios(pontos_base)

# Estrutura de decisão para determinar o nível do herói
if xp_heroi < 1000:
    nivel_heroi = "Ferro"
elif 1000 <= xp_heroi <= 2000:
    nivel_heroi = "Bronze"
elif 2001 <= xp_heroi <= 5000:
    nivel_heroi = "Prata"
elif 5001 <= xp_heroi <= 7000:
    nivel_heroi = "Ouro"
elif 7001 <= xp_heroi <= 8000:
    nivel_heroi = "Platina"
elif 8001 <= xp_heroi <= 9000:
    nivel_heroi = "Ascendente"
elif 9001 <= xp_heroi <= 10000:
    nivel_heroi = "Imortal"
else:
    nivel_heroi = "Radiante"

# Mensagem final
print(f"O Herói de nome {nome_heroi}, da classe {classe_heroi} , usando um(a): {arma_heroi} , está no nível de {nivel_heroi} com {xp_heroi} XP.")
