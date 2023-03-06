two_digit_number = input("Type a two digit number: ")

print(type(two_digit_number)) #type shows the data type the variable is in

f = two_digit_number[0]
s = two_digit_number[1]
result = int(f) + int(s)

print(result)