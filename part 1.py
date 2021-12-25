while True:
    print("you can:")
    print("1.get food")
    print("2.get water")
    print("3.get bloks")
    print("4.make a home")
    input(">")
    answer = "0"
    answer = input()

    if answer == "1":
        yesNo = ""
        print("you got food eat it yes/no")
        yesNo = input()
        if yesNo == "yes":
            print("you lived")
        elif yesNo == "no":
            print("You died from hunger")

    
    if answer == "2":
        print("got water")
        print("yes/no/filter")
        if answer == "yes":
            print("it was posind")
        if answer == "no":
            print("you died from thirst")
        if answer == "filter":
            print("you lived")    
