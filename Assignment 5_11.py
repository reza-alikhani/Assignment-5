def khayam_triangle(n):

    triangle = [[1]]  

    for i in range(1, n):
      
        prev_row = triangle[i - 1]
        new_row = [1]  

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1) 
        triangle.append(new_row)

    for row in triangle:
        print(" ".join(map(str, row)).center(n * 3)) 


n = int(input("Enter the number of rows for Pascal's Triangle: "))
khayam_triangle(n)
