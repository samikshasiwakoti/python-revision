try:
    print("Program started")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print(" Error: You cannot divide by zero")

except ValueError:
    print(" Error: Invalid input! Please enter numbers only")

else:
    print(" Division successful")
    print("Result:", result)

finally:
    print(" Program finished (this always runs)")


