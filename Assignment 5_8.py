def checkered_board(m, n):
    for i in range(m):
        if i % 2 == 0:
            row_str = '* ' if n % 2 == 1 else '*'
        else:
            row_str = '# ' if n % 2 == 1 else '#'

        for j in range(1, n):
            if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                row_str += '#'
            else:
                row_str += '*'
        
        print(row_str)

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
checkered_board(m, n)  
