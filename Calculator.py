def calculator():
    while True:
        try:
            print("\nMini Calculator")
            print("Options: +, -, *, /")
            print("Type 'exit' to quit.")
            
            num1 = input("Enter first number: ")
            if num1.lower() == "exit":
                break
            num1 = float(num1)
            
            op = input("Enter operator (+, -, *, /): ")
            if op.lower() == "exit":
                break
            
            num2 = input("Enter second number: ")
            if num2.lower() == "exit":
                break
            num2 = float(num2)
            
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue
            
        except ValueError:
            print("Please enter a valid number!")
            continue
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            continue
        except Exception as e:
            print("An unexpected error occurred:", e)
            continue
        else:
            print("Result:", result)
        finally:
            print("Operation complete.\n")

calculator()
