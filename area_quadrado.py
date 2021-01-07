def area_do_quadrado(medida_aresta):
    medida_aresta = float(input("Digite a medida da aresta, em centímetros, do quadrado: "))
    area = medida_aresta * medida_aresta
    print("A área do quadrado vale: %3.2f cm² " % area)

    return area_do_quadrado


area = area_do_quadrado(5)
