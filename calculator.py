

def Operations(USER_CHOICE_OPERATION ):
    user_input = input(USER_CHOICE_OPERATION) 
    print(user_input)
    while user_input != 'q':
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        
        if user_input == 'a':
            print(f"Addition is:  {add(a, b)}")
        elif user_input == 's':
            print(f"Subtraction is: {subtract(a, b)}")
        elif user_input == 'm':
            print(f"Multiplication is: {multiply(a, b)}")
        elif user_input == 'd':
            print(f"Division is: {divide(a, b)}")
        user_input = input(USER_CHOICE_OPERATION) 
    print("-----THANKYOU FOR USING OUR APP-----")    

def add(a, b):
    return a + b
    
    
def subtract(a, b):
   return a - b
    

def multiply(a, b):
    return a * b
    

def divide(a, b):
    return a / b

def main():
    print("-----WELCOME TO CALCULATOR APP-----")

    USER_CHOICE_OPERATION = """
    Enter:
    - 'a' for addition
    - 's' for subtraction
    - 'm' for multiplation
    - 'd' for division
    - 'q' for quit

    YOUR_CHOICE:"""

    Operations(USER_CHOICE_OPERATION )

main()