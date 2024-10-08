import random

# Lista de jogadores com suas notas (nome, nota)
jogadores = [
    ("Matheus", 70), ("Mayquin", 70), ("Jimmy", 80), ("Felipe C.", 45),
    ("Pablo", 65), ("André", 65),("Marley", 65),
    ("Fábio", 60), ("Ferrari", 50), ("Caio", 60), ("Wanderson", 60),
    ("Marcelin", 65)
]
# Função para balancear os times
def balancear_times(jogadores):
    # Ordenar os jogadores pela nota (do maior para o menor)
    jogadores.sort(key=lambda x: x[1], reverse=True)
    
    # Inicializar times
    times = [[], [], [], []]

    # Alternar jogadores entre os 4 times para balancear
    for i, jogador in enumerate(jogadores):
        times[i % 3].append(jogador)

    return times

# Função para calcular o total de pontos de um time
def calcular_total(time):
    return sum([jogador[1] for jogador in time])

# Sorteia times balanceados
times = balancear_times(jogadores)

# Exibe os times e seus totais
for i, time in enumerate(times):
    print(f"Time {i + 1}: {time}")
    print(f"Total de pontos do Time {i + 1}: {calcular_total(time)}\n")
