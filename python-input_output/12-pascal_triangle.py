#!/usr/bin/python3
""" defines module for a Pascal's triangle"""

def pascal_triangle(n):
    """ function returns a list of ints representing 'n' for a Pascal's tri"""
    if n <= 0:
        return []
    
    pascal_list = [[1]]
        
    for x in range(1, n):
        pre_row = pascal_list[-1]
        new_row = [1]
        
        for j in range(1, x):
            new_row.append(pre_row[j -1] + pre_row[j])
        
        new_row.append(1)
        pascal_list.append(new_row)

    return pascal_list
