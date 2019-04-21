# #1
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for i in numbers:
#     sum += i
# print(sum)

# #2
# numbers = [1, 2, 3, 4, 5]
# print(max(numbers))

# #3
# numbers = [1, 2, 3, 4, 5]
# print(min(numbers))

# #4
# numbers = [1, 2, 3, 4, 5]
# even = []
# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
# print(even)

# #5
# numbers = [-1. -2, 0, 1, 2, 3]
# positive = []
# for i in numbers:
#     if i > 0:
#         positive.append(i)
# print(positive)

# #6
# #Same as number 5, I thought it was asking for a list

#7
# numbers = [1, 2, 3, 4, 5]
# result = []
# for i in numbers:
#     i = i * 2
#     result.append(i)
# print(result)

#8
# numbers = [1, 2, 4]
# numbers1 = [1, 3, 4]

# result = []
# for i in range(len(numbers)):
#     mulitply = numbers[i] * numbers1[i]
#     result.append(mulitply)
# print(result)

#9
# matrix1 = [[1, 3], [2, 4]]
# matrix2 = [[5, 2], [1, 0]]

# result = [[0, 0], [0, 0]]
# for i in range(len(matrix1)): #for every column i, visit every row j
#     for j in range(len(matrix1[0])): #index represents the element within the second list
#         result[i][j] = matrix1[i][j] + matrix2[i][j] 
#         #so now i and j represents the appropriate map to get the element and will correspond to matrix2 as well.
# print(result) #don't forget to not indent the print or else that will loop as well

#10

# result = [[0]]
# if len(matrix3[i]) == len(matrix4[i]):
#     for i in range(len(matrix3)):
#         for j in range(len(matrix3[0])):
#             result[i][j] = matrix3[i][j] + matrix4[i][j]
# print(result)
            



