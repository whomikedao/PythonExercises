#1
numbers = [1, 2, 3, 4, 5]
sum = 0
for i in numbers:
    sum += i
print(sum)

#2
numbers = [1, 2, 3, 4, 5]
print(max(numbers))

#3
numbers = [1, 2, 3, 4, 5]
print(min(numbers))

#4
numbers = [1, 2, 3, 4, 5]
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
print(even)

#5
numbers = [-1. -2, 0, 1, 2, 3]
positive = []
for i in numbers:
    if i > 0:
        positive.append(i)
print(positive)

#6
#Same as number 5, I thought it was asking for a list

#7
numbers = [1, 2, 3, 4, 5]
result = []
for i in numbers:
    i = i * 2
    result.append(i)
print(result)

#8
numbers = [1, 2, 3]
numbers1 = [1, 2, 3]
result = []
for i in numbers:
    i = i * numbers1[numbers[index]]
    result.append(i)
print(result)

