import PrimImp as PrimAlg
import json
import random
import networkx as nx
from networkx_viewer import Viewer


class PrimTests:

    def gerarMatrizAleatoria(self, tamanho):
        lista = []

        for y in range(tamanho):
            linha = []
            for x in range(tamanho):
                num = random.randint(0, 9)
                linha.append(num)
            lista.append(linha)

        return lista

    def gerarGrafoInterativo(self, matriz, parent, pesos):
        G = nx.Graph()

        for idx in range(0, len(matriz)):
            G.add_edge(str(idx), str(parent[idx]))
            G.node[str(idx)]['Peso'] = pesos[idx]
            G.node[str(idx)]['label_fill'] = 'red'
            G.node[str(idx)]['outline'] = 'green'

        app = Viewer(G, home_node='-1', levels=1)
        app.mainloop()

    def gerarGrafoCompleto(self, matriz, parent, pesos):
        G = nx.Graph()

        for idx in range(0, len(matriz)):
            G.add_edge(str(idx), str(parent[idx]))
            G.node[str(idx)]['Peso'] = pesos[idx]

        app = Viewer(G)
        app.mainloop()

    def imprimirResultados(self, parent, matriz):
        tamanho = len(matriz)
        # Exibir no console
        for idxp in range(1, tamanho):
            tx = "Aresta: " + str(parent[idxp]) + " - " + str(idxp) + "   //   Peso: " + str(matriz[idxp][parent[idxp]])
            print(tx)

    def dadosDoArquivo(self, arquivo):
        dados = self.loadData(arquivo)
        prim = PrimAlg.Prim()
        return prim.execute(dados, 0)

    def grafoInterativoDoArquivo(self, arquivo):
        dados = self.loadData(arquivo)
        parent, pesos = self.dadosDoArquivo(arquivo)
        self.imprimirResultados(parent, dados)
        print(pesos)
        self.gerarGrafoInterativo(dados, parent, pesos)

    def grafoCompletoAleatorio(self, quantidade):
        dados = self.gerarMatrizAleatoria(quantidade)
        prim = PrimAlg.Prim()
        parent, pesos = prim.execute(dados, 0)
        self.imprimirResultados(parent, dados)
        print(pesos)
        self.gerarGrafoCompleto(dados, parent, pesos)

    def loadData(self, fileName):
        with open(fileName) as data_file:
            data = json.load(data_file)
        return  data

    def executeQ1(self):
        pesos = []
        dados = self.loadData('dadosEx1.json')
        prim = PrimAlg.Prim()
        parent, pesos = prim.execute(dados, 0)
        self.imprimirResultados(parent, dados)
        print(pesos)

        G = nx.MultiGraph()

        alfabeto = "abcdefghijklmnopqrstuvxz"

        for idx in range(0, len(dados)):
            letra = alfabeto[idx]
            if(parent[idx] == -1):
                letraPai = '-1'
            else:
                letraPai = alfabeto[parent[idx]]
            G.add_edge(letra, letraPai)
            G.node[letra]['Peso'] = pesos[idx]

        app = Viewer(G, home_node='-1', levels=100)
        app.mainloop()

    def executeQ2(self):
        self.grafoInterativoDoArquivo('dadosEx2.json')

    def executeQ3(self):
        self.grafoInterativoDoArquivo('dadosEx2.json')

    def executeAl(self, quantidade):
        self.grafoCompletoAleatorio(quantidade)




if __name__ == "__main__":

    tests = PrimTests()
    tests.executeQ1()
    tests.executeQ2()
    tests.executeAl(10)
    tests.executeAl(50)
