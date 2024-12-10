while True:
    print("\nEnter two numbers you want to add, enter 'q' to quit")

    first_num = input("First number: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try: 
        sum = int(first_num) + int(second_num)
    except ValueError:
        print("Please, only enter numbers")
    else:
        print(sum)

    
