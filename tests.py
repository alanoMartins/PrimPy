import PrimImp as PrimAlg
import json
import random
import unittest


class PrimTests(unittest.TestCase):

    def gerarMatrizAleatoria(self, tamanho):
        lista = []

        for y in range(tamanho):
            linha = []
            for x in range(tamanho):
                num = random.randint(0, 9)
                linha.append(num)
            lista.append(linha)

        return lista

    def imprimirResultados(self, parent, matriz):
        tamanho = len(matriz)
        # Exibir no console
        for idxp in range(1, tamanho):
            tx = "Aresta: " + str(parent[idxp]) + " - " + str(idxp) + "   //   Peso: " + str(matriz[idxp][parent[idxp]])
            print(tx)

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

    def executeQ2(self):
        pesos = []
        dados = self.loadData('dadosEx2.json')
        prim = PrimAlg.Prim()
        parent, pesos = prim.execute(dados, 0)
        self.imprimirResultados(parent, dados)
        print(pesos)

    def executeQ3(self):
        pesos = []
        dados = self.loadData('dadosEx3.json')
        prim = PrimAlg.Prim()
        parent, pesos = prim.execute(dados, 0)
        self.imprimirResultados(parent, dados)
        print(pesos)


if __name__ == "__main__":

    tests = PrimTests()
    tests.executeQ1()
    tests.executeQ2()
    tests.executeQ3()