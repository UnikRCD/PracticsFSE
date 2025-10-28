print('Выберите фигуру (Прямоугольник, Рамка или Треугольник)')
choice = str(input())
print('Введите кол-во строк')
n = int(input())
print('Введите кол-во столбцов')
m = int(input())

choices = ['Прямоугольник', 'Рамка', 'Треугольник']

if choice == choices[0]:
    def draw_rectangle(rows, columns, ch):
        for i in range(rows):
            for j in range(columns):
                print(ch, end=' ')
            print()

    print('Прямоугольник')
    draw_rectangle(n, m, '#')
    print()
    
elif choice == choices[1]:
    def draw_frame(rows, columns, ch):
        for i in range(rows):
            for j in range(columns):
                if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                    print(ch, end=' ')
                else:
                    print(' ', end=' ')
            print()
            
    print('Рамка')
    draw_frame(n, m, '#')
    print()
            
elif choice == choices[2]:
    def draw_triangle(height, ch):
        for i in range(height):
            for j in range(i + 1):
                print(ch, end=' ')
            print()
    
    print('Треугольник')
    draw_triangle(n, '#')
    print()
    
else:
    print('Введите одну из этих фигур: Прямоугольник, Рамка, Треугольник')