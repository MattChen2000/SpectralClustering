from sklearn.cluster import KMeans
import numpy as np
import csv


class Algorithm:

    def __init__(self):
        self.graph = {'A': ['B'],
                      'B': ['C', 'F', 'G'],
                      'C': ['B', 'D'],
                      'D': ['C', 'H'],
                      'E': ['F'],
                      'F': ['B', 'E', 'H'],
                      'G': ['B'],
                      'H': ['D', 'F', 'I'],
                      'I': ['H'],
                      'J': ['F', 'O', 'M'],
                      'K': ['M'],
                      'L': ['M', 'P'],
                      'M': ['J', 'K', 'L', 'N', 'T', 'U'],
                      'N': ['O', 'M'],
                      'O': ['J', 'N'],
                      'P': ['L'],
                      'Q': ['R', 'X'],
                      'R': ['Q', 'X'],
                      'S': ['Y'],
                      'T': ['M', 'R', 'Y'],
                      'U': ['M', 'V'],
                      'V': ['U', 'Z'],
                      'W': ['Y'],
                      'X': ['Q', 'R'],
                      'Y': ['T', 'S', 'W', 'Z'],
                      'Z': ['V', 'Y']
                      }
        self.A = None
        self.D = None
        self.L = None

    def getAdjacencyMatrix(self):
        A = np.zeros((26, 26), dtype=np.int16)
        for key, value in self.graph.items():
            i = ord(key) - ord('A')
            for item in value:
                j = ord(item) - ord('A')
                A[i, j] = 1
        with open('AdjacencyMatrix.csv', mode='w') as adjacencyM_file:
            writer = csv.writer(adjacencyM_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for array in A:
                writer.writerow(array)
        self.A = A

    def getDegreeMatrix(self):
        D = np.diag(self.A.sum(axis=1))
        with open('DegreeMatrix.csv', mode='w') as degreeM_file:
            writer = csv.writer(degreeM_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for array in D:
                writer.writerow(array)
        self.D = D

    def getLaplacianMatrix(self):
        L = self.D - self.A
        with open('LaplacianMatrix.csv', mode='w') as LaplacianM_file:
            writer = csv.writer(LaplacianM_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for array in L:
                writer.writerow(array)
        self.L = L


if __name__ == '__main__':
    solution = Algorithm()
    solution.getAdjacencyMatrix()
    solution.getDegreeMatrix()
    solution.getLaplacianMatrix()
