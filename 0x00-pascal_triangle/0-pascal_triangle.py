def pascal_triangle(n):
    y=n
    if n <= 0:
        return []
    for x in range(2, n+1):
        y=y*x
    return y

    def combination(m,n):
        result = pascal_triangle(m)//pascal_triangle(m-n)*fact