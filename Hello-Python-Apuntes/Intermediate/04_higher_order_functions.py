# funciones de orden superior

#funciones que realizan cosas con funciones dentro

#mas o menos funciones anidadas


from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value +5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5,2,sum_one))
print(sum_two_values_and_add_value(5,2,sum_five))


#closures#

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
add_closure = sum_ten(1)
print (add_closure(5))

## map
numbers = [ 0, 5, 9, 7, 1, 2, 6, 11]

def multiply_two(number):
    return number * 2

print (list(map(multiply_two, numbers)))

#filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))


#reduce

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))