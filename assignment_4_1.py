#This program prints a table as shown below which lists powers of 2 and 1/x for numbers 1 to 10

def question_one():

    for i in range(1,11):

        print(i, "\t\t", i**2, "\t\t {0:0.2f}".format(1/i))






def question_two():
    u_sentence = input("Enter your sentence: ")
    encoded_string = " "
    for char in u_sentence:
        char_code = ord(char)
        encoded_char_code = char_code + 5
        encoded_char = chr(encoded_char_code)
        encoded_string = encoded_string + encoded_char
    print(encoded_string)


def question_three():
    first_num = int(input("Enter the first number:"))
    second_num = int(input("Enter the second number:"))
    product = first_num * second_num
    string_product = str(product)
    for char in string_product:
        print(char)



def question_four():
    alphabets = " abcdefghijklmnopqrstuvwxyz"
    user_string = input("Enter a string: ")
    sum = 0
    for char in user_string:
        char_position = alphabets.find(char)
        sum = sum + char_position

    print(sum)


def question_six():
    for i in range(1,101):
        print(i, "\t\t", i**2,  "\t\t {0:0.3f}".format(i**0.5))



def question_five():
    grade = int(input("Enter your grades:"))
    if grade == 1:
        print("Fail")
    elif grade == 2:
        print("Poor")
    elif grade == 3:
        print("Fair")
    elif grade == 4:
        print("Good")
    elif grade == 5:
        print("Excellent")
    else:
        print("Not applicable")


def question_five_b():
    marks = int(input("Enter your marks:"))
    if 90>=marks<=100:
        print("A")
    elif 80>=marks<=89:
        print("B")
    elif 70>=marks<=79 :
        print("C")
    elif 60>=marks<=69:
        print("D")
    elif 1>=marks<=59:
        print("E")
    else:
        print("Not Applicable")

question_five_b()