try:
    a =int(input("enter the first number : "))
    b =int(input("enter the second number : "))
    print("what kind of  operation you want to perform.press + for addition \n, - for substraction\n, * for multiplication \n,/ for division\n")
    o =input("enter operation: ")
    match o:
        case "+":
            print(f"the result is: { a + b} ")
    
        case "-":
            print(f"the result is: { a - b} ")
    
        case "*":
            print(f"the result is: { a * b} ")
    
        case "/":
            print(f"the result is: { a /b}")
        case default:
            print("there was an error")    

except Exception as e:
    print("enter a valid value  of a and b ")

