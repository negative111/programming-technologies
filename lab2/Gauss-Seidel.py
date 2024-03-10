import numpy as np
A=np.array([[10,3,0],[3,15,1],[0,1,7]])
f=np.array([[2],[12],[5]])
B=np.zeros((3,3))
D=np.diag(np.diag(A))
x=np.array([[1],[1],[1]])
r=f-np.dot(A,x)
x0=x
x00=x

for i in range(3):
    for j in range(3):
        if i <= j:
            B[i][j] = A[i][j]

for n in range(100):
    x = x + np.dot(np.linalg.inv(B), ((f - np.dot(A,x))))
    #r = np.linalg.norm(f - np.dot(A, x))
    if np.linalg.norm(A) * np.linalg.norm(np.linalg.inv(A))* np.linalg.norm(f - np.dot(A, x)) /np.linalg.norm(f)<= 10 ** -4:
        print('Количество итераций: ', n)
        print(x)
        break
    x0 = x