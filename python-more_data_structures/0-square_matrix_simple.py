#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    
    neo = []
    for row in matrix:
        fresh = []
        for number in row:
            fresh.append(number ** 2)
        neo.append(fresh)
    return neo

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    neo = square_matrix_simple(matrix)
    print(neo)
    print(matrix)
