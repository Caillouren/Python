x = float(input())
fat = [None]*51
fat[0] = 1
elevaX = [None]*51
elevaX[0] = 1

for i in range(0, 50):
    elevaX[i + 1] = x * elevaX[i]
    fat[i + 1] = (i + 1) * (fat[i])

somatório = [None]*51
somatório[0] = 1

for i in range(0, 50):
    somatório[i + 1] = elevaX[i + 1] / fat[i + 1]

print(f"{sum(somatório):.2f}")