numbers = [1, 2, 4, 5, 8, 9]

numbers.append(0)
numbers.insert(2, 3)
res = numbers.__add__([2, 4])
print(res.count(2))
print(1 in res)
print(numbers)

print(res)
print('--' * 10)
del res[len(res) - 1]
print(res)
