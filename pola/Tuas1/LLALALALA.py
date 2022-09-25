# Pola 1 - Template matching
import numpy as np

# Data esktraksi ciri
A=np.array([[11,8,5],
           [12,7,4],
           [11,9,5]])

B=np.array([[15,11,8],
           [13,11,9],
           [14,12,7]])

C=np.array([[5,15,12],
           [4,14,12],
           [4,13,11]])

# Database
DB=np.array([A[1],B[1],C[1]])   # Database

# Opsi keluaran
daun=["A","B","C"]            

# Klasifikasi
JA1=sum(abs(A[0]-DB[0]))
JA2=sum(abs(A[0]-DB[1]))
JA3=sum(abs(A[0]-DB[2]))
JA=np.array([JA1,JA2,JA3])
SJA=np.argsort(JA)
out1=daun[SJA[0]]

JB1=sum(abs(B[0]-DB[0]))
JB2=sum(abs(B[0]-DB[1]))
JB3=sum(abs(B[0]-DB[2]))
JB=np.array([JB1,JB2,JB3])
SJB=np.argsort(JB)
out2=daun[SJB[0]]

JC1=sum(abs(C[0]-DB[0]))
JC2=sum(abs(C[0]-DB[1]))
JC3=sum(abs(C[0]-DB[2]))
JC=np.array([JC1,JC2,JC3])
SJC=np.argsort(JC)
out3=daun[SJC[0]]

# Keluaran
jarak=np.array([JA,JB,JC])
keluaran=np.array([[out1],[out2],[out3]])
print('Database\n',DB)
print('Jarak\n',jarak)
print('Keluaran\n',keluaran)



