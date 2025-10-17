def calculator_with_history():
    history = []  # List to store all calculations

    while True:
        try:
            print("\nMini Calculator with History")
            print("Options: +, -, *, /")
            print("Type 'exit' to quit or 'history' to see previous results.")
            
            num1 = input("Enter first number: ")
            if num1.lower() == "exit":
                break
            if num1.lower() == "history":
                print("\nCalculation History:")
                for item in history:
                    print(item)
                continue
            num1 = float(num1)
            
            op = input("Enter operator (+, -, *, /): ")
            if op.lower() == "exit":
                break
            if op.lower() == "history":
                print("\nCalculation History:")
                for item in history:
                    print(item)
                continue
            
            num2 = input("Enter second number: ")
            if num2.lower() == "exit":
                break
            if num2.lower() == "history":
                print("\nCalculation History:")
                for item in history:
                    print(item)
                continue
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
            # Save to history
            history.append(f"{num1} {op} {num2} = {result}")
        finally:
            print("Operation complete.\n")

calculator_with_history()
