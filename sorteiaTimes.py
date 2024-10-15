import random

# Lista de jogadores com suas notas (nome, nota)
jogadores = [
    ("Matheus", 70), ("Mayquin", 69), ("Felipe C.", 45),
    ("Pablo", 68), ("André", 67), ("Marley", 65), ("Caio", 60), ("Wanderson", 60),
    ("Xico", 62), ("Marcelin", 65), ("Biel", 70), ("Felipe Soares", 62),
    ("Ernani", 70), ("Artur", 70), ("Giovanni", 60), ("Guilherme", 68)
]

# Função para balancear os times
def balancear_times(jogadores):
    # Embaralhar a lista de jogadores aleatoriamente
    random.shuffle(jogadores)
    
    # Inicializar os 4 times
    times = [[], [], [], []]

    # Distribuir os jogadores entre os 4 times
    for i, jogador in enumerate(jogadores):
        times[i % 4].append(jogador)

    return times

# Função para calcular o total de pontos de um time
def calcular_total(time):
    return sum([jogador[1] for jogador in time])

# Sorteia e balanceia os times
times = balancear_times(jogadores)

# Exibe os times e seus totais
for i, time in enumerate(times):
    print(f"Time {i + 1}: {time}")
    print(f"Total de pontos do Time {i + 1}: {calcular_total(time)}\n")
