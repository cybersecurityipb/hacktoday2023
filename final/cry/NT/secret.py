import numpy as np

def isLinearDependence(matrix):
    n = len(matrix)
    return np.linalg.matrix_rank(matrix) != n


guessMatrix = np.identity(9, dtype=int)
