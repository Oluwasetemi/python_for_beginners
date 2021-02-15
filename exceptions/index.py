try:
    age = int(input('Age: '))
    print(1000 / age)
except ZeroDivisionError as e:
    print(e.__str__())
except ValueError:
    print('Invalid value')
