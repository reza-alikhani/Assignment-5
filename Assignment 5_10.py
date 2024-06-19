def draw_rhombus(n):

    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('* ' * (i + 1))

    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1), end='')
        print('* ' * (i + 1))

n = int(input("Enter the side length of the rhombus: "))
draw_rhombus(n)
