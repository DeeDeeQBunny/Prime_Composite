# while loop to keep it running
while True:
    # make a number to check for
    check_num = 1
    # make a list for factors
    factors = []
    # user's input
    number = int(input("Enter a positive number: "))
    # check if check_num is less than or equal to number
    while check_num <= number:
        # check if check_num is divisible into number
        if number % check_num == 0:
            # print check_num
            print(check_num, "is a factor")
            # add check_num to the factors list
            factors.append(check_num)
            # print factors list
            print(f"Here is the list of factors for {number}:", factors)
            # add one to check num so that it can go again
            check_num += 1
        # if check_num is not divisible into number
        else:
            # print check_num is not a factor
            print(check_num, "is not a factor")
            # add one to check num so that it can go again
            check_num += 1
    # check if the length of factors is 2
    if len(factors) == 2:
        print("This number is prime.")
    # check if the length of factors is 1
    elif len(factors) == 1:
        print("This number is neither prime nor composite.")
    # check if the length of factors is not 2 or 1
    else:
        print("This number is composite.")        