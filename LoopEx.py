# #1
# for i in range(1, 11):
#     print(i)

# #2
# start = int(input('Start: '))
# end = int(input('End: '))
# for i in range(start, end + 1):
#     print(i)

# #3
# for i in range(1, 10, 2):
#     print(i)

# #4
# for i in range(5):
#     star = '* '
#     for i in range(4):
#         star += '* '
#     print(star)

# #5
# size = int(input("How big do you want the square?"))
# for i in range(size):
#     star = '* '
#     for i in range(size - 1):
#         star += '* '
#     print(star)

#6
# height = int(input("Height:" ))
# width = int(input("Width: "))

# for i in range(height):
#     if i == 0 or i == height -1:
#         print("*" * (width+2))
#     else:
#         print("*" + " "*width + "*")

#7
# for i in range(5):
#     star = '*'
#     for j in range(i):
#         star += '*'
#     print(star)

#8
# height = int(input("Height: "))
# for i in range(height):
#     star = '*'
#     for j in range(i):
#         star += '*'
#         height -= 1
#     print(" "*height+star)

#9
# for i in range(1, 13):
#     result = []
#     for j in range(1, 13):
#         multiply = i * j
#         result.append(multiply)
#     print(result)

#bonus 1
text = input("Text? ")

for i in range(1):
    border = "****"
    for j in range(len(text)):
        border += "*"
    print(border)
    print("* " + text + " *")
    print(border)