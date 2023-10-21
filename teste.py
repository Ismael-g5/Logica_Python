def classificar_equipe():
    pontos = []

    for i in range(3):
        ponto = float(input(f"Digite os pontos do jogador {i + 1}: "))
        pontos.append(ponto)

    pontos.sort(reverse=True)

   
    soma = sum(pontos)

   
    if soma > 100:
        media = soma / 3
        print("Pontos em ordem decrescente:", pontos)
        print("A equipe está classificada. Média de pontos:", media)
    else:
        print("Pontos em ordem decrescente:", pontos)
        print("Equipe desclassificada")

classificar_equipe()
