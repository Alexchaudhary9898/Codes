password_length = 10
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
all_chars = lowercase + uppercase + digits
password = random.sample(all_chars, password_length)
random.shuffle(password)
final_password = ''.join(password)
print("generated password:", final_password)