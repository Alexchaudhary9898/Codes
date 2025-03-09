medical_cause=input("did u have a medical cause Y or N:")
atten = int(input("enter thbe attendance of the student:"))
if medical_cause == 'Y':
    print("You are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("not allowed")