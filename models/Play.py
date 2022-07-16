import random
from PySide2.QtGui import QBrush, QColor
import numpy as np
from models.Solucion import Solucion


class Play():
    numeros = []

    tabla = []
    tablaAux = []

    # pool = Pool(processes=2)

    # pool = ThreadPool(processes=2)

    def __init__(self):
        self.tabla = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]
                      ]
        self.tablaAux = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0]
                         ]
        self.numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def start(self, tablero):

        for i in range(len(self.numeros)):
            for j in range(len(self.numeros)):
                tablero.item(i, j).setText("")
                tablero.item(i, j).setForeground(QBrush(QColor(0, 0, 0)))

        i = 1

        while i <= 31:

            existeEnfila = False
            existeEncolumna = False
            existeCuadrante = False

            # numero que sera aletorio en el tablero
            num = [random.uniform(0, 1) for i in self.numeros]
            maximo = max(num)
            indice = num.index(maximo)

            # posicion de la fila donde se colocara
            filas = [random.uniform(0, 1) for i in self.numeros]
            maximoFilas = max(filas)
            fila = filas.index(maximoFilas)

            # posicion de la colunma donde se colocara
            columnas = [random.uniform(0, 1) for i in self.numeros]
            maximoColumnas = max(columnas)
            columna = columnas.index(maximoColumnas)

            for j in range(len(self.numeros)):

                if self.tabla[fila][j] == self.numeros[indice]:
                    existeEnfila = True
                    break

            if not existeEnfila:
                for j in range(len(self.numeros)):

                    if self.tabla[j][columna] == self.numeros[indice]:
                        existeEncolumna = True
                        break

            if not existeEnfila and not existeEncolumna:
                corner_fila = fila - fila % 3
                corner_columna = columna - columna % 3
                for x in range(3):
                    for y in range(3):
                        if self.tabla[corner_fila + x][corner_columna + y] == self.numeros[indice]:
                            existeCuadrante = True

            if not existeEnfila and not existeEncolumna and not existeCuadrante:
                if self.tabla[fila][columna] == 0:
                    self.tabla[fila][columna] = self.numeros[indice]
                    self.tablaAux[fila][columna] = self.numeros[indice]
                    tablero.item(fila, columna).setText(str(self.numeros[indice]))
                    # tablero.item(fila, columna).setForeground(QBrush(QColor(0, 255, 0)))
                    i = i + 1

        # self.tablaAux = self.tabla
        return tablero

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

            # async_result = self.pool.apply_async(self.fi)
            # async_result2 = self.pool.apply_async(self.col)

            # contFilas = async_result.get()
            # contColum = async_result2.get()

            # filas
            for k in range(len(self.numeros)):
                fila = dict(zip(self.tablaAux[k], map(lambda x: self.tablaAux[k].count(x), self.tablaAux[k])))
                for c in fila.values():
                    if (c >= 1):
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
                    if (f >= 1):
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

    def fi(self):
        contFilas = 0
        for k in range(len(self.numeros)):
            fila = dict(zip(self.tablaAux[k], map(lambda x: self.tablaAux[k].count(x), self.tablaAux[k])))

            for c in fila.values():
                if (c >= 1):
                    contFilas += 1

        return contFilas

    def col(self):
        contColum = 0
        trans = []
        t = np.transpose(self.tablaAux)

        for l in range(len(self.numeros)):
            trans.append(list(t[l]))
        # columas
        for l in range(len(self.numeros)):
            columna = dict(zip(trans[l], map(lambda x: trans[l].count(x), trans[l])))
            for f in columna.values():
                if (f >= 1):
                    contColum += 1

        return contColum

    def resolver(self, tablero):
        soluciones = self.inicializacion()
        soluciones = self.verificar(soluciones)
        soluciones.sort(key=lambda x: x.fitness)
        mejor = self.validar(soluciones, tablero)

        cont = 0
        while cont != 5:
            seleccionados = self.seleccion(soluciones)
            cruza = self.cruza(seleccionados)
            mutacion = self.mutacion(cruza)
            mutacion = self.verificar(mutacion)
            soluciones = self.poda(soluciones, mutacion)
            soluciones.sort(key=lambda x: x.fitness)
            mejor = self.validar(soluciones, tablero)
            cont += 1
            print(cont)

        indice = 0
        for i in range(len(self.numeros)):
            for j in range(len(self.numeros)):
                if self.tabla[i][j] == 0:
                    tablero.item(i, j).setText(str(mejor.getGenes()[indice]))
                    tablero.item(i, j).setForeground(QBrush(QColor(0, 255, 0)))
                    indice += 1

        # for i in seleccionados:
        #     print(i)

        # num =1 
        # for i in cruza:
        #      print(num, "\t",i.getGenes())
        #      num += 1

        # print("\n")
        # for i in mutacion:
        #     print("fila: ",i.getRow()," Colum: ", i.getColum(), "Fitness", i.getFitness())

        # print("\n", mejor.getFitness())

        # for i in range(len(self.numeros)):
        #     for j in range(len(self.numeros)):
        #         print(self.tablaAux[i][j])

    def validar(self, soluciones, tablero):

        mejor = soluciones[-1]
        print("\n", mejor.getGenes())
        print(mejor.getFitness())
        # indice = 0
        # for i in range(len(self.numeros)):
        #      for j in range(len(self.numeros)):
        #          if self.tabla[i][j] == 0:
        #             tablero.item(i, j).setText(str(mejor.getGenes()[indice]))
        #             tablero.item(i, j).setForeground(QBrush(QColor(255, 0, 0)))
        #             indice += 1

        return mejor

    def inicializacion(self):

        soluciones = []
        pIncial = 500
        # 2500

        for i in range(pIncial):
            genes = []
            for j in range(50):
                s = random.choice(self.numeros)
                genes.append(s)

            solucion = Solucion(genes)
            soluciones.append(solucion)

        return soluciones

    def seleccion(self, soluciones):
        l = len(soluciones)
        items = int(l * 0.70)
        mitad = int(l / 2)

        bajo = soluciones[:mitad]
        alto = soluciones[mitad:]

        selec = []

        for i in range(items):
            m = [random.uniform(0, 1) for i in alto]
            maximo = max(m)
            indice1 = m.index(maximo)

            min = [random.uniform(0, 1) for i in alto]
            maximo2 = max(min)
            indice2 = min.index(maximo2)

            selec.append([alto[indice1], alto[indice2]])

        return selec

    def cruza(self, seleccionados):

        # bit = seleccionados[0][0].getGenes()
        # bit = len(bit) - 1
        # c = random.randint(1, bit)

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
            hijo1 = papa[0] + mama[1] + papa[2] + mama[3] + papa[4]
            hijo2 = mama[0] + papa[1] + mama[2] + papa[3] + mama[4]

            p1 = Solucion(hijo1)
            p2 = Solucion(hijo2)

            generacion.append(p1)
            generacion.append(p2)

        return generacion

    def mutacion(self, cruza):
        mutaInd = 0.40
        mutaGen = 0.20

        cont = 0

        for solucion in cruza:

            muta = random.uniform(0, 1)

            if muta <= mutaInd:
                cont += 1
                m = [random.uniform(0, 1) for i in solucion.getGenes()]
                for i in range(len(m)):
                    if m[i] <= mutaGen:
                        solucion.getGenes()[i] = random.choice(self.numeros)

        return cruza

    def poda(self, soluciones, hijos):

        pMax = 2000

        # 7000
        soluciones += hijos

        if len(soluciones) > pMax:
            soluciones.sort(key=lambda x: x.fitness, reverse=True)
            soluciones = soluciones[:pMax]

        return soluciones
