# We need a function that can transform a number (integer) into a string.
#
# What ways of achieving this do you know?
# Examples (input --> output):
#
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

def number_to_string(num):
    number = str(num)
    return number

if __name__ == '__main__':
    print(number_to_string(67)) #-> '67'
    print(number_to_string(79585)) #-> '79585'
    print(number_to_string(7958)) #-> '7958'
    print(number_to_string(1+2)) #-> '3'
    print(number_to_string(1-2)) #-> '-1'



