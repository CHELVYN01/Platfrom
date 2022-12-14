# Pola 1 - Template matching
import numpy as np

# Data esktraksi ciri
A=np.array([[12.5,5.4,29,50],
            [11,5.5,28,34],
            [10.5,5,20.5,51.75],
            [14,6,33,58.65],
            [12,5.3,29,39.4],
            [12.3,5,26,38.875],
            [11.5,5.1,27,36.85],
            [10.5,5,25,32.225],
            [12.4,5,28,32],
            [12.3,5.8,28,43],
            [11,4.2,26,22.1],
            [12,4.4,27,26.125],
            [10.5,4,26,25.075],
            [10,4,25,17.125],
            [11,4,27,20.75],
            [10.5,3.8,28,21.125],
            [12,5,29,20.5],
            [12,5.5,30,29.4],
            [10.5,4,25,20.5],
            [12,5,30,32.25]])

B=np.array([[12.4,5.26,36.625],
            [14.5,4.5,26.5,18.125],
            [8.5,5,22,32.375],
            [10,4,21,25.5],
            [10,4.5,25,28],
            [10,4.5,21,26.75],
            [9,3.1,21,23.5],
            [10,4,24,23.2625],
            [8,4.5,20,22.25],
            [12.5,6,30,41.25],
            [11.5,5.5,27.43],
            [12.5,6,28,48.75],
            [11.5,27,40.5],
            [8.5,4.5,22,27.5],
            [11,5,26,39.625],
            [9.5,4,23,26.5],
            [10,3.5,24,27.25],
            [7.5,4,19,16.375],
            [12,4.5,27,32.75],
            [7.5,3.5,15,14.5]])

C=np.array([[12,4.5,26,36.625],
           [14.5,4.5,26.5,18.125],
           [10,4,21,25.5],
           [10,4.5,25,28],
           [10,4.5,21,26.75],
           [9,3.1,21,23.5],
           [10,4,24,23.2625],
           [8,4.5,20,22.25],
           [12.5,6,30,41.25],
           [11.5,5.5,27,43],
           [12.5,6,28,48.75],
           [11,5,27,40.5],
           [8.5,4.5,22,27.5],
           [11,5,26,39.625],
           [9.5,4,23,26.5],
           [10,3.5,24,27.25],
           [7.5,4,19,16.375],
           [12,4.5,27,32.75],
           [7.5,3.5,15,14.5]])

D=np.array([[ 13.5,7,31,45.575]
            [12,6.29,35.575,]
            [13.5,7,31, 45.575],
            [12,6.5,29,40.575],
            [13,7,30,450],
            [12,6,29.5,350],
            [13,7,31,45.445],
            [13,7,32,45.570],
            [14.5,6,27.5,50.323],
            [13,6,30,43.570],
            [11,4,21,23.575],
            [10.5,5,22,23.775],
            [8.5,3.3,19,16.55],
            [8,3.8,19,170],
            [10.5,4,25,25,875],
            [9,4,20,26.0],
            [10,4.5,21,28.125],
            [10.5,4.5,22,30.375],
            [9.5,4,19.9,20.375],
            [9.5,4,19.9,24.625]])






# 9,7,27,32.725
# 8,6,24,26.8
# 8.5,7,27,34.375
# 10,6.5,29,40.225
# 9,7,28,38.4
# 10,6.5,26,32.3
# 9,7,25,39.675
# 9.5,7,27,39
# 10.5,7,27.5,45
# 10,6.5,24.5,40
# 9,6.5,26,30.2
# 8,5.5,25.5,38.125
# 9,5.9,26,33.5
# 9,6.6,28	35.675
# 8.9	6.5	27	30.125
# 8.5	6	27	33.675
# 8.5	5	26	32
# 8	5	25	28.375
# 8.3	5.5	27	38.25
# 8	5.3	25	23.75

# 13.5,7	31	45,575
# 12	6	29	35.575
# 13.5	7	31	45,575
# 12	6.5	29	40,575
# 13	7	30	450
# 12	6	29.5	350
# 13	7	31	45,445
# 13	7	32	45,570
# 14.5	6	27.5	50,323
# 13	6	30	43,570
# 11	4	21	23,575
# 10,5	5	22	23,775
# 8,5	3,3	19	16.55
# 8	3,8	19	170
# 10.5	4	25	25,875
# 9	4	20	26,0
# 10	4.5	21	28,125
# 10.5	4.5	22	30,375
# 9.5	4	19.9	20,375
# 9.5	4	19.9	24,625
# Database
DB=np.array([A[1],B[1],C[1],D[1]])   # Database

# Opsi keluaran
daun=["A","B","C","D"]            

# Klasifikasi
JA1=sum(abs(A[0]-DB[0]))
JA2=sum(abs(A[0]-DB[1]))
JA3=sum(abs(A[0]-DB[2]))
JA4=sum(abs(A[0]-DB[3]))
JA=np.array([JA1,JA2,JA3,JA4])
SJA=np.argsort(JA)
out1=daun[SJA[0]]

JB1=sum(abs(B[0]-DB[0]))
JB2=sum(abs(B[0]-DB[1]))
JB3=sum(abs(B[0]-DB[2]))
JB4=sum(abs(B[0]-DB[3]))
JB=np.array([JB1,JB2,JB3,JB4])
SJB=np.argsort(JB)
out2=daun[SJB[0]]

JC1=sum(abs(C[0]-DB[0]))
JC2=sum(abs(C[0]-DB[1]))
JC3=sum(abs(C[0]-DB[2]))
JC4=sum(abs(C[0]-DB[3]))
JC=np.array([JC1,JC2,JC3,JC4])
SJC=np.argsort(JC)
out3=daun[SJC[0]]

JD1=sum(abs(D[0]-DB[0]))
JD2=sum(abs(D[0]-DB[1]))
JD3=sum(abs(D[0]-DB[2]))
JD4=sum(abs(D[0]-DB[3]))
JD=np.array([JD1,JD2,JD3,JD4])
SJD=np.argsort(JD)
out4=daun[SJD[0]]

# Keluaran
jarak=np.array([JA,JB,JC,JD])
keluaran=np.array([[out1],[out2],[out3],[out4]])
print('Database\n',DB)
print('Jarak\n',jarak)
print('Keluaran\n',keluaran)



