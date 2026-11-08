while True:
    user_input = input("Enter a number: ")

    try:
        num = float(user_input)

        if num < 1:
            print("Please use a number greater than 1.")
        elif num == 5:
            print("Program stopped.")
            
        else:
            display_num = int(num) if num.is_integer() else num

            print("\n" + "=" * 30)
            print(f"Multiplication Table of {display_num}")
            print("=" * 30)

            for i in range(1, 13):
                result = num * i
                print(f"{display_num}  x  {i:2}  =  {result}")
            

    except ValueError:
        print("Invalid input! Please enter a valid number.")
