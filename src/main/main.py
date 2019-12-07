from sklearn.cluster import KMeans
import numpy as np
import csv


class Algorithm:

    def __init__(self):
        self.graph = {'A': ['B', 'G'],
                      'B': ['C', 'E', 'F', 'G'],
                      'C': ['B', 'D', 'H'],
                      'D': ['C', 'H', 'I'],
                      'E': ['F', 'B', 'G'],
                      'F': ['B', 'E', 'H', 'J', 'I'],
                      'G': ['B', 'A', 'E'],
                      'H': ['D', 'F', 'I'],
                      'I': ['H', 'D', 'F'],
                      'J': ['F', 'O', 'M', 'N', 'K'],
                      'K': ['M', 'J', 'L'],
                      'L': ['M', 'P', 'K'],
                      'M': ['J', 'K', 'L', 'N', 'T'],
                      'N': ['O', 'M', 'J'],
                      'O': ['J', 'N'],
                      'P': ['L'],
                      'Q': ['R', 'X'],
                      'R': ['Q', 'X', 'W', 'Y'],
                      'S': ['Y', 'U', 'V'],
                      'T': ['M', 'R', 'Y'],
                      'U': ['S', 'V'],
                      'V': ['S', 'U', 'Z'],
                      'W': ['Y', 'R'],
                      'X': ['Q', 'R'],
                      'Y': ['T', 'S', 'W', 'Z', 'R'],
                      'Z': ['V', 'Y']
                      }
        self.A = self.getAdjacencyMatrix()
        self.D = self.getDegreeMatrix()
        self.L = self.getLaplacianMatrix()
        self.eigenVals, self.eigenVecs = self.getEigenThings()

    def getAdjacencyMatrix(self):
        A = np.zeros((26, 26), dtype=np.int16)
        for key, value in self.graph.items():
            row = ord(key) - ord('A')
            for item in value:
                column = ord(item) - ord('A')
                A[row, column] = 1
        with open('AdjacencyMatrix.csv', mode='w') as adjacencyM_file:
            writer = csv.writer(adjacencyM_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for array in A:
                writer.writerow(array)
        return A

    def getDegreeMatrix(self):
        D = np.diag(self.A.sum(axis=1))
        with open('DegreeMatrix.csv', mode='w') as degreeM_file:
            writer = csv.writer(degreeM_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for array in D:
                writer.writerow(array)
        return D

    def getLaplacianMatrix(self):
        L = self.D - self.A
        with open('LaplacianMatrix.csv', mode='w') as LaplacianM_file:
            writer = csv.writer(LaplacianM_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for array in L:
                writer.writerow(array)
        return L

    def getEigenThings(self):
        vals, vecs = np.linalg.eig(self.L)
        vecs = vecs[:, np.argsort(vals)]
        vals = vals[np.argsort(vals)]
        return vals, vecs

    def k_means(self, clusters):
        kmeans = KMeans(n_clusters=clusters)
        kmeans.fit(self.eigenVecs[:, 1:clusters])
        colors = kmeans.labels_
        return colors


if __name__ == '__main__':
    solution = Algorithm()
    vals = solution.eigenVals
    print(vals)
    k_mean = solution.k_means(3)
    count = {0: [], 1: [], 2: []}
    for i in range(len(k_mean)):
        count[k_mean[i]].append(chr(i + ord('A')))
    print(count)