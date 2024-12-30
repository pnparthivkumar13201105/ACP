def count_digits(number):
    number = abs(number)
    return len(str(number))

user_input = int(input("Enter a number: "))
total_digits = count_digits(user_input)
print(f"The total number of digits in {user_input} is: {total_digits}")
