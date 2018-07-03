# -*- coding:utf-8 -*-
class Solution:
    '''
    Input(matrix): 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    Return: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
    '''
    # def printMatrix(self, matrix):
    #     # write code here
    #     #return matrix and list(matrix.pop(0) + self.printMatrix(zip(*matrix)[::-1]))
    #     array = []
    #     while matrix:
    #         for item in matrix[0]:
    #             array.append(item)
    #         del matrix[0]
    #         if len(matrix) == 0:
    #             break
    #         matrix = self.traverse(matrix)
    #     return array

    # def traverse(self, matrix):
    #     row_num = len(matrix)
    #     col_num = len(matrix[0])
    #     traversed = []
    #     # 添加顺序是倒的
    #     for c in range(col_num):
    #         row = []
    #         for r in range(row_num):
    #             row.append(matrix[r][c])
    #         traversed.append(row)
    #     # 倒转矩阵行
    #     traversed.reverse()
    #     return traversed

    def printMatrix(self, matrix):
        array = []
        while matrix:
            for i in matrix[0]:
                array.append(i)
            del matrix[0]
            if len(matrix) == 0:
                break
            matrix = self.traverse(matrix)
        return array
        
    def traverse(self, matric):
        row = len(matric)
        col = len(matric[0])
        tarversed = []
        for c in range(col):
            row1 = []
            for r in range(row):
                row1.append(matric[r][c])
            tarversed.append(row1)
        tarversed.reverse()
        return tarversed

x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

s = Solution()
print s.printMatrix(x)