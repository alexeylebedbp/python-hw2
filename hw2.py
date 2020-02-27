import numpy as np
#1 Include a section with your name
name = 'Alexey Lebed'
#2 Create matrix A with size (3,5) containing random numbers
A = np.random.rand(3, 5)
print(A)
#3 Find the size and length of matrix A
print('Size:', A.size)
print('Lenght:', len(A))
#4 Resize (crop/slice) matrix A to size (3,4)
print('Sliced:')
A = A[:, :4]
print(A)
print(A.size)
#5 Find the transpose of matrix A and assign it to B
print('Transposed:')
B = np.transpose(A)
print(B)
#6 Find the minimum value in column 1 of matrix B
print('Min of the column 1 in B', np.min(B[:, 1]))
#7 Find the minimum and maximum values for the entire matrix A
print('Min of A', np.min(A))
print('Max of A', np.max(A))
#8 Create vector X (an array) with 4 random numbers
X = np.random.rand(4)
print("X", X)
#9 Create a function and pass vector X and matrix A in it
def multiplier(matrix, vector):
    return  np.matmul(matrix, vector)
#10 In the new function multiply vector X with matrix A and assign the result to D
D = multiplier(A, X)
print(D)

#11 Create a complex number Z with absolute and real parts != 0
Z = np.random.rand() + 1j*np.random.rand()
print(Z)

#12 Show its real and imaginary parts as well as it’s absolute value
print('real', Z.real)
print('imag', Z.imag)
print('absolute', np.absolute(Z))

#13 Multiply result D with the absolute value of Z and record it to C
C = np.absolute(Z) * D
print('Vector C', C)

#14 Convert matrix B from a matrix to a string and overwrite B
result_str = ""
for element in B.reshape(1, B.size)[0]:
    result_str += str(element)
B = result_str
print(B)

#15 Display a text on the screen: ‘Nameis done with HW2‘, but pass your ‘Name’ as a string variable
print(f"{name} is done with HW2")