print("you can:")
print("1.get food")
print("2.get water")
print("3.work to get money")
print("4.get blocks")
print("5.make a home")
print("6.quit")
blocks = ""
money = 0
while True:
    answer = " "
    answer = input(">")

    if answer == "1":
        yesNo = "0"
        print("you got food eat it yes/no")
        yesNo = input()
        if yesNo == "yes":
            print("you lived")
        elif yesNo == "no":
            print("You did not survive from hunger Go back and try something else")

    
    elif answer == "2":
        print("got water")
        print("yes/no/filter")
        yesNo = input()
        if yesNo == "yes":
            print("it was poisoned You did not survive Try something else")
        if yesNo == "no":
            print("you did not survive from thirst try something else")
        if yesNo == "filter":
            print("you lived") 

    elif answer == "3":
        print("you got 25 dollers come back to get more")       
        money = money + 25

    elif answer == "4":
        print("you have " +str(money) +" dollers")
        print("a block is 5 dollers")
        print("how many do you want")
        blocks = input()
        print(blocks)
        money = money - int(blocks) * 5 
        print(f"you have $",money)


    elif answer =="5":
        if blocks == "":
            print("Sorry! you need more blocks!")
        elif int(blocks) >= 10 :
                print("you need more blocks")
        elif int(blocks) < 10:
            print("you got a house,the end")

        elif answer == "6":
            print("good bye")
            exit()       
                
