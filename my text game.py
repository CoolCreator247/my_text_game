while True:
    print("you can:")
    print("1.get food")
    print("2.get water")
    print("3.get blocks")
    print("4.make a home")
    input(">")
    answer = "0"
    answer = input()

    # hello faris
    if answer == "1":
        yesNo = ""
        print("you got food eat it yes/no")
        yesNo = input()
        if yesNo == "yes":
            print("you lived")
        elif yesNo == "no":
            print("You died from hunger Go back and try something elseelseelse")

    
    if answer == "2":
        print("got water")
        print("yes/no/filter")
        if answer == "yes":
            print("it was poisoned Try something else")
        if answer == "no":
            print("you died from thirst try something else")
        if answer == "filter":
            print("you lived") 


    if answer == "3":
        print("you have 20 dollers")
        print("a block is 5 dollers")
        blocks = input()
        money = 0
        money = money - int(blocks)
        print(f"you have",money)


    if answer =="4":
        if blocks == ">10":
            print("you need more blocks")
        elif blocks == "<10":
            print("you got a house,the end")
