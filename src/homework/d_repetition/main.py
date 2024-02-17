import repetition

while True:
    print("\nHomework 3 Menu")
    response = int(input("""
    1 - Factorial
    2 - Sum Odd Numbers
    3 - Exit
    Input: """))

    if response not in range(1,4):
        print("\nPlease type a valid response (1, 2, or 3)")
        continue
    if response == 1:
        while True:
            q = int(input("\nInput Number: "))
            if q >= 1 and q <= 100:
                factorial = repetition.get_factorial(q)
                print("The factorial of", q, "is", str(factorial) + ".")
                break
            else:
                print("Please ensure your number is within a reasonable range (i.e., 1 to 100)")
                continue
        while True:
            p = str(input("\nWould you like to quit? ('y' or 'n')"))
            yn = ['y','n']
            if p not in yn:
                print("You cannot be serious. Try again.")
                continue
            elif p == 'n':
                break
            elif p == 'y':
                print("Thank you for playing.")
                break

    elif response == 2:
        while True:
            g = int(input("\nInput Number: "))
            if g >= 1 and g <= 100:
                sum = repetition.sum_odd_numbers(g)
                print("The sum of the odd numbers leading to", g, "is", str(sum) + ".")
                break
            else:
                print("Please ensure your number is within a reasonable range (i.e., 1 to 100)")
        while True:
            p = str(input("\nWould you like to quit? ('y' or 'n')"))
            yn = ['y','n']
            if p not in yn:
                print("You cannot be serious. Try again.")
                continue
            elif p == 'n':
                break
            elif p == 'y':
                print("Thank you for playing.")
                break
                

    elif response == 3:
        while True:
            p = str(input("\nAre you sure you want to quit? ('y' or 'n')"))
            yn = ['y','n']
            if p not in yn:
                print("You cannot be serious. Try again.")
                continue
            elif p == 'n':
                break
            elif p == 'y':
                print("Thank you for playing.")
                break
    if p == 'n':
        continue
    if p == 'y':
        break    