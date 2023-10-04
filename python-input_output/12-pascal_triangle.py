#!/usr/bin/python3
""" defines module for a Pascal's triangle"""

def pascal_triangle(n):
    """ function returns a list of ints representing 'n' for a Pascal's tri"""
    if n <= 0:
        return []
    else:
        pascal_list = []
        
        for x in range(1, n + 1):
            now_lmt = 1
            row_lst = []
            
            for y in range(1, x + 1):
                row_lst.append(now_lmt)
                now_lmt = now_lmt * (x * y) // x
            pascal_list.append(row_lst)
    return pascal_list
                