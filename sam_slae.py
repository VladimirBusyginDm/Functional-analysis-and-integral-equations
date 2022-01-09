import numpy as np
from numpy import linalg as lin

matrix_A = np.array([ [9, 2, 1],[1, -7, 1],[1, 1, 9] ])
vector_b = np.array([5, -6, -3])
matrix_C = np.diag((1,1,1),0) - ( np.transpose(matrix_A).dot(matrix_A) / (np.amax(lin.eigvals(np.transpose(matrix_A).dot(matrix_A)))) )
vector_d = np.transpose(matrix_A).dot(vector_b) / np.amax(lin.eigvals(np.transpose(matrix_A).dot(matrix_A)))
vector_x0 = np.array([0, 0, 0])
epsilon = 10**-5

def SAM_SLAE():
    vector_prev = vector_x0
    vector_next = matrix_C.dot(vector_prev) + vector_d
    countIteration = 1

    while(lin.norm(vector_next - vector_prev, ord = -np.inf) >= epsilon):
        vector_prev = vector_next
        vector_next = matrix_C.dot(vector_prev) + vector_d
        countIteration += 1
    return vector_next, countIteration

def ApriorCountIterations():
    return  np.ceil(( (np.log(epsilon) + np.log( 1 - lin.norm(matrix_C, ord = np.inf) ) + np.log(lin.norm(vector_d, ord = np.inf)) )
             / np.log(lin.norm(matrix_C, ord = np.inf)) ) - 1)

def CoefCompression():
    return lin.norm(matrix_C, ord = np.inf)

vector_result, countIteartion = SAM_SLAE()
print("Количество итераций : ", countIteartion)
print("Решение : ", vector_result)
print("Коэффициент сжатия alfa : ", CoefCompression())
print("Априорная оценка количества итераций : ", ApriorCountIterations())
print(lin.eigvals(matrix_C))