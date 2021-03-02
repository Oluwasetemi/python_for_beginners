tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

'''
apples Alice  dogs
oranges   Bob  cats
cherries Carol moose
banana David goose

'''


def print_table_data(data):
    """
    a fxn that print list inside list
    """
    for n in range(len(data[0])):
        print(f'{data[0][n]} {data[1][n]} {data[2][n]}')
        # continue


print_table_data(tableData)
