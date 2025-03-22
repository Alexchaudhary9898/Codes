lower = int(input("enter a lower range:"))
upper = int(input("enter a upper range:"))
print("primt numbers bwtween", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5)+ 1):
            if num % i == 0:
             is_prime = False
            break
    if is_prime:
        print(num)