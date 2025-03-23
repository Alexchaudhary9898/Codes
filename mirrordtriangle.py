def mirroed_right_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
n = int(input("enter the number of rows: "))
mirroed_right_triangle(n)