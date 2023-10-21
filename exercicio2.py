pontos_atleta_1 = int(input('Digite aqui os pontos que o 1° atleta marcou: '))
pontos_atleta_2 = int(input('Digite aqui os pontos que o 2° atleta marcou: '))
pontos_atleta_3 = int(input('Digite aqui os pontos que o 3° atleta marcou: '))



pontos_equipe = pontos_atleta_1 , pontos_atleta_2 , pontos_atleta_3

total_pontos = pontos_atleta_1 + pontos_atleta_2 + pontos_atleta_3

desc_pontos = sorted(pontos_equipe, reverse=True)

for pontos_equipe in desc_pontos:
    if total_pontos > 100:
        media = (pontos_atleta_1 + pontos_atleta_2 + pontos_atleta_3) / 3
        print(media)
else: print('Equipe Desclassificada')