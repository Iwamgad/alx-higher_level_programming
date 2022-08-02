#!/usr/bin/python3
"""My Pascal's Triangle module"""

def pascal_triangle(n):
    """Pascal's Triangle of size n
    Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    else:
        triangle = []
        if n > 0:
            for i in range(n):
                L = [1 for _ in range(i+1)]
                for j in range(i):
                    if j != 0 and j != i:
                        L[j] = triangle[i-1][j] + triangle[i-1][j-1]
                triangle.append(L)
    return triangle
