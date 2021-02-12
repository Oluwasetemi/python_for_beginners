is_hot = True
is_cold = True

# if is_hot:
#     print('hot day')
# else:
#     print('normal day')

# if is_hot:
#     print('hot day')
# elif is_cold:
#     print('cold day')
# else:
#     print('normal day')

# x = int(input("Please enter an integer: "))
# # Please enter an integer: 42
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# Assignment
price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = price * (10/100)
    print(f'You need to put down payment of {down_payment}')
else:
    down_payment = price * (20/100)
    print(f'You need tp put down payment of {down_payment}')
print(down_payment)
