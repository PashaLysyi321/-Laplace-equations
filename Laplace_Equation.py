import numpy as np

print('\nThis is a program for finding the temperature of a thin plate using the Laplace '+
 'equation\nprepared by student of KM-71 Lysyi Pavlo 13var\n\n')


n = 7
m = 6
down = 910
up = 610
left = 1010
right = 410
x = 17.3
y = 15.1

'''
n = 9
m = 9
down = 0
up = 100
left = 75
right = 50
x = 1
y = 1
'''

#малюємо графічне представлення пластинки
def draw(n, m, x, y, up, down, left, right):
    print('\n\t\t|'+'---|'*(m - 1))
    for i in range(0, n - 1):
        print('\t\t|   |'+'   |'*(m - 2))
        print('\t\t|'+'---|'*(m - 1))
    print('\nlength: {}, height: {}\nUpTemperature: {}, DownTemperature: {}\nLeftTemperature: {}, RightTemperature: {}\n'.format(x,y,up,down,left,right))

#вирішення рівняння Лапласса    
def TemperatureFound(n, m, x, y, up, down, left, right):

    c = x * x + y * y 
    
    #заповнюємо початкову матрицю
    matrix = np.zeros(shape = (n, m))
    matrix[0][:] = str(up)
    matrix[n-1][:] = down

    for i in range(0,m):
        matrix[i][0] = left
        matrix[i][m-1] = right
            
    string_list = np.array([list(map(str, x)) for x in matrix])

    for j in range (1, n - 1):
        for i in range (1, m - 1):
            string_list[j][i] = 'x['+str(j)+','+str(i)+']'
    
    #виводимо рівняння на екран
    print('\nOur matrix is:\n\n{}\n\nOur equations will be:\n'.format(string_list))

    for j in range (1, n - 1):
        for i in range (1, m - 1):
            print(' -2*{}*{} + {}*{} + {}*{} + {}*{} + {}*{} = 0'.format(string_list[j][i],c,y*y,string_list[j-1][i],y*y,string_list[j+1][i],x*x,string_list[j][i-1],x*x,string_list[j][i+1]))

    k = (n - 2) * (m - 2) #20
    
    #створюємо масив з елементами матриці для розв'язку рівняння
    summ = np.zeros(shape = (k, k))

    for i in range(0, k):
        summ[i][i] = -2 * c #-2*527.3

    for i in range(1, k):
        if i % (m-2) != 0:
            summ[i - 1][i] = x * x #299.29
            summ[i][i - 1] = x * x #299.29
        
    for i in range(0, (n-2)*(m-2)-m+2):
        summ[i][i + m-2] = y * y #228.01
        summ[i + m-2][i] = y * y #228.01

    solution = [] #вектор рішеннь
    solution.append(-y*y*up - x*x*left)

    if m-4 != 0:
        for i in range(0, m-4):
            solution.append(-y*y*up)
        
    solution.append(-y*y*up - x*x*right)

    for i in range(0, n-4):
        solution.append(-x*x*left)
        if n - 4 != 0:
            for j in range(0, m - 4):
                solution.append(0)
        solution.append(-x*x*right)
        
    solution.append(-y*y*down - x*x*left)

    if m-4 != 0:
        for i in range(0, m-4):
            solution.append(-y*y*down)
        
    solution.append(-y*y*down - x*x*right)
    solution = np.array(solution)
    ans = np.linalg.solve(summ, solution) #вирішуємо систему рівнянь
    ans = np.around(ans, decimals=4)
    print('\nOur solution will be this matrix:\n') #виводимо на екран матрицю
    i = 0
    
    while i < (m - 2)*(n - 2):
        print(ans[i : i + m - 2])
        i = i + m - 2
    
    print('\n')

#цикл для введення вхідних данних та обробки помилок 
while True:
    check1 = input('press 1 to run Laplace algoritm, press 2 to exit: ')
    if check1 == '1':    
        try:
            '''
            n = int(input('\nPleasa enter N number of Matrix: '))
            m = int(input('Pleasa enter M number of Matrix: '))
            down = int(input('Pleasa enter down temperature: '))
            up = int(input('Pleasa enter up temperature: '))
            left = int(input('Pleasa enter left temperature: '))
            right = int(input('Pleasa enter right temperature: '))
            x = float(input('Pleasa enter x(length): '))
            y = float(input('Pleasa enter y(height): '))  
            print('\n') '''
            draw(n, m, x, y, up, down, left, right)   
            TemperatureFound(n, m, x, y, up, down, left, right)
         
        except:
            print('Please enter a correct numbers')
    elif check1 == '2':
        break
    else:
        print('Please enter 1 or 2')