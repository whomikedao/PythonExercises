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
for i in range(5):
    star = '*'
    for j in range(i):
        star += '*'
    print(star)