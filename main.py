n = 36
m = 22
i = 0
j = 0

IfPositiveNumber = 0
CountColumnOne = 0
CountColumnTwo = 0
MaxNumber = 0
ColumnIdTwo =[]
SumQuadModTwo = 0


print("Введите Y для третьего задания: ")
Y = input()


a = []
for i in range(n):
    b = []
    for j in range(m):
        if i < n/2: b.append(min(-n-i, m-j))
        if i > n/2-1: b.append(max(-n-i, m-j))
        print("%3d" % b[j], end='')
    a.append(b)
    print(' ')

for i in range(m):
    print("", end='')
print()

for i in range(m):
    for j in range(n):
        if a[j][i] < 0:
            IfPositiveNumber = 1

    if IfPositiveNumber == 0:
        CountColumnOne += 1

for i in range(m):
    for j in range(n):
        if a[j][i] >= MaxNumber:
            MaxNumber = a[j][i]

    if MaxNumber == a[n-1][i]:
        CountColumnTwo += 1
        ColumnIdTwo.append(i)


    MaxNumber = 0


for i in range(n):
    for j in range(m):
      if i % 2 != 0:
        if a[i][j] < int(Y):
            SumQuadModTwo += a[i][j]*a[i][j]


print("Количество столбцов матрицы, в которых нет положительных элементов: ", CountColumnOne)

if CountColumnTwo == 1:
    print("Да, в матрице есть столбец, в котором на последнем месте стоит максимальный элемент столбца")

if CountColumnTwo > 0:
    print("Да, в матрице есть столбцы, в которых на последнем месте стоит максимальный элемент столбца")
    print("Таких столбцов:", CountColumnTwo)
    print("Их номера: ")
    for i in range(len(ColumnIdTwo)): print(i,"", end=" ")

if CountColumnTwo <=0:
    print("В матрице нец столбца/столбцов, в которых на последнем месте стоит максимальный элемент столбца")

print("\n")
print("Сумма квадратов элементов меньших Y расположенных в строках с нечетными номерами: ", SumQuadModTwo)

input()