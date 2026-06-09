from random import randint


def generate_matric_number():
    prefix = "26SE"
    number = randint(1000, 9999)
    return prefix + str(number)

print(generate_matric_number())