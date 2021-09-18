lst_nums = [1,2,3,4,5]

def do_square(n):
    return n ** 2

lst_squares = map(do_square, lst_nums)
print(list(lst_squares))