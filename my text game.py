print("you can:")
print("1.get food")
print("2.get water")
print("3.work to get money")
print("4.get blocks")
print("5.make a home")
blocks = ""
money = 0
while True:
    answer = "0"
    answer = input(">")

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
        yesNo = input()
        if yesNo == "yes":
            print("it was poisoned Try something else")
        if yesNo == "no":
            print("you died from thirst try something else")
        if yesNo == "filter":
            print("you lived") 

    if answer == "3":
        print("you got 5 dollers come back to get more")       
        money = money + 5

    if answer == "4":
        print("you have " +str(money) +" dollers")
        print("a block is 5 dollers")
        blocks = input()
        print(blocks)
        money = money - int(blocks) * 5 
        print(f"you have $",money)


    if answer =="5":
        print(blocks)
        if blocks == "":
            print("Sorry! you need more blocks!")
        elif int(blocks) >= 10 :
            print("you need more blocks")
        elif int(blocks) < 10:
            print("you got a house,the end")
            break
