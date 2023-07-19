class InvalidAgeException(Exception):
    pass
number = 18
try:
    input_num = int(input("Enter age:"))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("eligible to vote")
except InvalidAgeException:
    print("error occurred:Invalid age")
