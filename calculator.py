from module import add

def multiply(num1, num2):
    return num1 * num2

def substract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1/num2

def exponential(num1, num2):
    return num1 ** num2

while True:
    try:
        number_1 = int(input("\nPlease enter the first number:"))
    except:
       print("Enter a number!\n")
       continue
    else:
        break

while True:
    try:
       number_2 = int(input("\nPlease enter the second number:"))
    except:
       print("Enter a number!")
       continue
    else:
        break


select_option = input("\nSelect one of the option below:\n+\t*\t-\t/\t^\n:")


if select_option == "+":
    print(number_1, "+" , number_2 , "=" , 
          add(number_1, number_2))

elif select_option == "*":
    print(number_1, "*", number_2 , "=" , 
          multiply(number_1, number_2))

elif select_option == "-":
    print(number_1 , "-" , number_2 , "=" , 
          substract(number_1, number_2))

elif select_option == "/":
    print(number_1 , "/" , number_2 , "=" , 
          divide(number_1, number_2))

elif select_option == "^":
    print(number_1 , "^" , number_2 , " = " , 
          exponential(number_1,number_2))

else:
    print("Invalid Value!")
