def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of n
    Args:
        n (int): size of triangle
    """

    left, current, right = [], [], []

    if n <= 0:
        return []

    current.append(1)
    left.append(current)
    for i in range(n - 1):
        if len(left) == 1:
            current = [1, n-1]
            left.append(current)
            continue

        right.append(1)
        for j in range(0, len(current) - 1):
            right.append(current[j] + current[j+1])
        right.append(1)
        left.append(right)
        current = right
        right = []
    return left