import random


class Prim:
    # Matri de adjacencia
    def execute(self, matriz, noInicial):

        #Inicializando variáveis
        tamanho = len(matriz)
        infinito = 9999 #Representação do infinito
        jaVisitados = [False for idx in range(0, tamanho)] #Guarda flag se o vertice já foi visitado
        parent = [0 for idx in range(0, tamanho)] #Vertice para cada vertice da MST
        pesos = [infinito for idx in range(0, tamanho)] #Pesos de cada aresta da MST


        #Valor inicial do primeiro nó
        pesos[noInicial] = 0 # Primeiro nó
        parent[0] = -1 #Define nó raiz

        counter = 0

        #Montar ocupacao do MST :)
        for count in range(tamanho, -1, -1):
            minimo = self.menorNoRestante(pesos, jaVisitados, tamanho)
            jaVisitados[minimo] = True

            for idxLinha in range(0, tamanho):
                eAdjacente = matriz[minimo][idxLinha] != 0
                if eAdjacente and jaVisitados[idxLinha] is False and matriz[minimo][idxLinha] < pesos[idxLinha]:
                    parent[idxLinha] = minimo
                    pesos[idxLinha] = matriz[minimo][idxLinha]
                    counter += 1


        return (parent, pesos)

    # Procura menor no ainda não incluido na mst
    def menorNoRestante(self, arr, mstSet, size):
        min_v = 99999
        min_idx = -1

        for i in range(0, size):
            if mstSet[i] == False and arr[i] < min_v:
                min_v = arr[i]
                min_idx = i

        return min_idx

if __name__ == "__main__":
    prim = Prim()

    lista = []
    n = 50

    for y in range(n):
        linha = []
        for x in range(n):
            num = random.randint(0, 9)
            linha.append(num)
        lista.append(linha)

    X = [[0, 0, 0, 0],
         [1000, 0, 0, 100],
         [0, 6, 0, 299],
         [0, 0, 0, 0]]

    Q1 = [[0, 1, 0, 0, 4, 8, 0, 0],
         [1, 0, 2, 0, 0, 6, 6, 0],
         [0, 2, 0, 3, 0, 0, 2, 0],
         [0, 0, 3, 0, 0, 0, 1, 4],
         [4, 0, 0, 9, 0, 5, 0, 0],
         [8, 6, 0, 0, 5, 0, 1, 0],
         [0, 6, 2, 1, 0, 1, 0, 1],
         [0, 0, 0, 4, 0, 0, 1, 0]]

    Q2 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    Q3 = [[0, 2, 0, 6, 0],
          [2, 0, 3, 8, 5],
          [0, 3, 0, 0, 7],
          [6, 8, 0, 0, 9],
          [0, 5, 7, 9, 0]]


    W = [[0, 7, 0, 5, 0, 0, 0],
         [7, 0, 8, 9, 7, 0, 0],
         [0, 8, 0, 5, 0, 0, 0],
         [5, 9, 0, 0, 15, 6, 0],
         [0, 7, 5, 15, 0, 8, 9],
         [0, 0, 0, 6, 8, 0, 11],
         [0, 0, 0, 0, 9, 11, 0]]


    print(lista)

    prim.execute(lista, 6)
