def mutliply_tuple_elements(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
my_tuple = (7, 3, 5, 7)
result = mutliply_tuple_elements(my_tuple)
print("the product of the tuple element is:", result)