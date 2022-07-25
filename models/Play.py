import random
from PySide2.QtGui import QBrush, QColor
import numpy as np
from models.Solucion import Solucion
import matplotlib.pyplot as plt


class Play:
    numeros = []

    tabla = []
    tablaAux = []

    def __init__(self):
        self.tabla = [[0, 2, 9, 0, 3, 0, 0, 1, 8],
                      [8, 1, 0, 2, 4, 0, 0, 7, 0],
                      [7, 5, 3, 6, 0, 0, 9, 4, 0],
                      [2, 0, 8, 0, 0, 6, 0, 0, 0],
                      [5, 0, 1, 0, 9, 2, 8, 0, 7],
                      [9, 6, 7, 0, 8, 0, 5, 2, 3],
                      [1, 0, 4, 8, 0, 5, 0, 3, 6],
                      [3, 0, 5, 4, 0, 1, 0, 8, 9],
                      [6, 8, 2, 0, 0, 3, 4, 5, 1]
                      ]
        self.tablaAux = [[0, 2, 9, 0, 3, 0, 0, 1, 8],
                         [8, 1, 0, 2, 4, 0, 0, 7, 0],
                         [7, 5, 3, 6, 0, 0, 9, 4, 0],
                         [2, 0, 8, 0, 0, 6, 0, 0, 0],
                         [5, 0, 1, 0, 9, 2, 8, 0, 7],
                         [9, 6, 7, 0, 8, 0, 5, 2, 3],
                         [1, 0, 4, 8, 0, 5, 0, 3, 6],
                         [3, 0, 5, 4, 0, 1, 0, 8, 9],
                         [6, 8, 2, 0, 0, 3, 4, 5, 1]
                         ]
        self.numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def start(self, tablero, resolver, nuevo):

        nuevo.setDisabled(True)
        for i in range(len(self.numeros)):
            for j in range(len(self.numeros)):
                tablero.item(i, j).setText("")
                tablero.item(i, j).setForeground(QBrush(QColor(0, 0, 0)))

        for i in range(len(self.numeros)):
            for j in range(len(self.numeros)):
                if self.tabla[i][j] != 0:
                    tablero.item(i, j).setText(str(self.tabla[i][j]))

        resolver.setDisabled(False)

    def verificar(self, soluciones):

        for solucion in soluciones:

            indice = 0
            contColum = 0
            contFilas = 0
            fit = 0

            for i in range(len(self.numeros)):
                for j in range(len(self.numeros)):

                    if self.tablaAux[i][j] == 0:
                        self.tablaAux[i][j] = solucion.getGenes()[indice]
                        indice += 1
            # filas
            for k in range(len(self.numeros)):
                fila = dict(zip(self.tablaAux[k], map(lambda x: self.tablaAux[k].count(x), self.tablaAux[k])))
                for c in fila.values():
                    if c >= 1:
                        contFilas += 1

            # transpuesta para las columnas
            trans = []
            t = np.transpose(self.tablaAux)

            for l in range(len(self.numeros)):
                trans.append(list(t[l]))
            # columas
            for l in range(len(self.numeros)):
                columna = dict(zip(trans[l], map(lambda x: trans[l].count(x), trans[l])))
                for f in columna.values():
                    if f >= 1:
                        contColum += 1

            fit = contColum + contFilas

            # se pasa los valores de la solucion
            solucion.setRow(contFilas)
            solucion.setColum(contColum)
            solucion.setFitness(fit)

            for i in range(len(self.numeros)):
                for j in range(len(self.numeros)):
                    self.tablaAux[i][j] = self.tabla[i][j]

        return soluciones

    def resolver(self, tablero, resolver, nuevo):

        resolver.setDisabled(True)
        mejores = []
        peores = []
        promedios = []
        soluciones = self.inicializacion()
        soluciones = self.verificar(soluciones)
        soluciones.sort(key=lambda x: x.fitness)
        mejor, peor, promedio = self.validar(soluciones)
        mejores.append(mejor.getFitness())
        peores.append(peor.getFitness())
        promedios.append(promedio)

        cont = 1
        while mejor.getFitness() != 162:
            seleccionados = self.seleccion(soluciones)
            cruza = self.cruza(seleccionados)
            mutacion = self.mutacion(cruza)
            mutacion = self.verificar(mutacion)
            soluciones = self.poda(soluciones, mutacion)
            soluciones.sort(key=lambda x: x.fitness)
            mejor, peor, promedio = self.validar(soluciones)
            print(mejor.getFitness())
            print(peor.getFitness())
            print(promedio)
            mejores.append(mejor.getFitness())
            peores.append(peor.getFitness())
            promedios.append(promedio)
            cont += 1
            print(cont)

        indice = 0
        for i in range(len(self.numeros)):
            for j in range(len(self.numeros)):
                if self.tabla[i][j] == 0:
                    tablero.item(i, j).setText(str(mejor.getGenes()[indice]))
                    tablero.item(i, j).setForeground(QBrush(QColor(0, 255, 0)))
                    indice += 1

        self.graficar(mejores, cont, peores, promedios)
        nuevo.setDisabled(False)

    def validar(self, soluciones):

        mejor = soluciones[-1]
        peor = soluciones[0]

        m = sum(p.getFitness() for p in soluciones)
        promedio = int(m/len(soluciones))
        print("\n", mejor.getGenes())

        return mejor, peor, promedio

    def inicializacion(self):

        soluciones = []
        pIncial = 200
        # 100

        for i in range(pIncial):
            genes = []
            for j in range(30):
                s = random.choice(self.numeros)
                genes.append(s)

            solucion = Solucion(genes)
            soluciones.append(solucion)

        return soluciones

    def seleccion(self, soluciones):
        l = len(soluciones)
        items = int(l * 0.20)
        mitad = int(l / 2)

        bajo = soluciones[:mitad]
        alto = soluciones[mitad:]

        selec = []

        for i in range(items):
            m = [random.uniform(0, 1) for i in alto]
            maximo = max(m)
            indice1 = m.index(maximo)

            min = [random.uniform(0, 1) for i in bajo]
            maximo2 = max(min)
            indice2 = min.index(maximo2)

            selec.append([alto[indice1], bajo[indice2]])

        return selec

    def cruza(self, seleccionados):

        generacion = []

        for cruce in seleccionados:
            # se divide los genes del padre y madre
            papa = cruce[0].getGenes()
            mama = cruce[1].getGenes()
            papa = [papa[i:i + 10] for i in range(0, len(papa), 10)]
            mama = [mama[i:i + 10] for i in range(0, len(mama), 10)]

            random.shuffle(papa)
            random.shuffle(mama)

            # se generan los hijos con los genes de los padres
            hijo1 = papa[0] + mama[1] + papa[2]
            hijo2 = mama[0] + papa[1] + mama[2]

            p1 = Solucion(hijo1)
            p2 = Solucion(hijo2)

            generacion.append(p1)
            generacion.append(p2)

        return generacion

    def mutacion(self, cruza):
        mutaInd = 0.20
        mutaGen = 0.15

        # mutaInd = 0.40   0.20
        # mutaGen = 0.20   0.15

        cont = 0

        for solucion in cruza:

            muta = random.uniform(0, 1)

            if muta <= mutaInd:
                cont += 1
                m = [random.uniform(0, 1) for i in solucion.getGenes()]
                for i in range(len(m)):
                    if m[i] <= mutaGen:
                        m2 = [random.uniform(0, 1) for i in self.numeros]
                        maximo = max(m2)
                        indice = m2.index(maximo)
                        solucion.getGenes()[i] = self.numeros[indice]

        return cruza

    def poda(self, soluciones, hijos):

        pMax = 500

        # 500
        soluciones += hijos

        if len(soluciones) > pMax:

            while len(soluciones) > pMax:
                soluciones.sort(key=lambda x: x.fitness, reverse=True)
                indice = random.randint(150, len(soluciones) - 1)
                soluciones.pop(indice)

            # soluciones = soluciones[:pMax]

        return soluciones

    def graficar(self, finales, cont, peores, promedios):

        epoca = range(cont)

        plt.subplot()
        plt.plot(epoca, finales, label='Mejores')
        plt.plot(epoca, peores, label='Peores')
        plt.plot(epoca, promedios, label='Promedio')
        plt.ylabel("Valor del Fitness")
        plt.xlabel("Generaciones")
        plt.title("Evolucion del Individuo")
        plt.legend()
        plt.savefig("Sudoku.png")
        plt.show()
