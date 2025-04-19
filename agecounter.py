def check_age():
    age_input = input("enter your age")
    if not age_input.isdigit():
        print("error: age should be positive num")
        return
    age = int(age_input)
    if age <= 0 or age > 130:
        print("error: age entered is not realistic")
        return
    if age % 2 == 0:
        print(f"your age ({age}) is even")
    else:
        print(f"your age ({age}) is odd")
check_age()