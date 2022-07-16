class Solucion():

    genes = []
    fitness = 0
    row = 0
    colum = 0

    def __init__(self, genes):
        self.genes = genes

    def setGenes(self, genes):
        self.genes = genes
    
    def getGenes(self):
        return self.genes
    
    def setFitness(self, fitness):
        self.fitness = fitness
    
    def getFitness(self):
        return self.fitness
    
    def setRow(self, row):
        self.row = row

    def getRow(self):
        return self.row
    
    def setColum(self, colum):
        self.colum = colum
    
    def getColum(self):
        return self.colum