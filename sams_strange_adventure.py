


def chapter1():
    print("\033c", end = "")
    print ("welkom to sam's strange advanture")
    print ("this is a small game made by kees brown, enjoy!")
    print ("pres enter to continue")
    input() 
    print ("""The adventure begins with sam entering a bar after he has left his home country
    he had been robbed of all his belongings by a strange boxer and now finds himself in a country unknown to him
    Sam heads to a bar and sits down.
    de bartender goes up to him and asks him wat Sam wants
    A = Ask for a gals of water 
    B = Ask for information
    C = Ask for the strongest stuff they have
     type A, B or C""")
chapter1()
while 1:    
    i = input(">")
    if i == "A":
        print("a drunk man next to you moves over next to you and loudly says that you get somthing stronger")
        r = 1
        break
    elif i == "B":
        print("the barman tels you about two things. there's talk about a big festival that wil be held in the capital in two weeks, he also tels you about a figthing ring near by.")
        r = 4
        break
    elif i == "C":
        print("a drunk man moves up next to you and loudly offers to get you somthing even stronger.")
        r = 1
        break

if r == 1:
    print("pres enter to continue")
    input() 
    print("the man bugs Sam for a bit and keeps drinking to, after a while he offers you a nother drink") 
    print("A = tel him your running low on money and can't pay for it.")
    print("B = refuse the offer saying please just leave me alone i'm tired.")
    while 1: 
        i = input(">") 
        if i == "A":
            print("he laughs and says that he will pay for it as long as you do him a favor later. then you drink for a while")
            r = 2
            break
        elif i == "B":
            print("he stops bugging you about drinking but dose offer to show you something interesting later")
            r = 2
            break
if r == 2: 
    print("pres enter to continue")
    input()
    print("""the man from the bar leads you to a allyway near the back of the bar and then down into a sewer area. 
    you then walk into a large fighting ring where people gamble on the winner""")
    print("""the same man from the bar wil ask you
    A = will you fight?
    B = will you gamble?""")
    while 1: 
        i = input(">")
        if i == "A":
            print("you end up winning two fights in a row! you have now become quit populair.")
            print("however you next opponent turns out to be the same guy who robbed you way bach when.")
            print("you end up winning and making a LOT of money")
            r = 3
            break
        elif i == "B":
            print("you end up gambling on the wrong person and lose all you remaining mony.")
            print("failed ending")
            break
if r == 3:
    print("pres enter to continue")
    input()
    print("""after the fight the same man from the bar reveals himself to be the leader of this place
    he then offers you a choice
    A = join him in running this place and make an name for your self
    B = Decline the offer""") 
    while 1: 
        i = input(">")
        if i == "A":
            print("after two years of living in this country sam has become a very richt man.")
            print("he is now the leader of a large crime organisation and lives happy and richt")
            print("The crime ending!")
            break
        elif i == "B ":
            print("you decline the offer and try and live a normal life in the city.")
            print("but you wil live forever thinking back on that offer")
            print("failed ending")
            break
if r == 4:
    print("A = travel to the festival")
    print("B = ask about the fighting ring")
    while 1: 
        i = input(">")
        if i == "A":
            print("you set out to travel to the festival wondering whaht hyou wil find there.")
            r = 5
            break
        elif i == "B ":
            print("the man next to you who offerd you the drinks has a big smile.")
            r = 2
            break
if r == 5:
    print("after taiking a ride with some travelers Sam maneges to make it some distance")
    print("but he is not there yet and its getting dark so he decides to stop at bar to sleep")
    print("this is a much nicer bar then the last one and sam is once again asked what he wants.")
    print("A = ask if there are any houses for sale")
    print("B = ask for information")
    while 1: 
        i = input(">")
        if i == "A":
            print("pres enter to continue")
            r = 6
            break
        elif i == "B ":
            print("the man seems to be crazy and calls the cops on you")
            print("failed ending")            
            break
if r == 6:
    print("the bartender tells you that he has a dauther that lives in the capital")
    print("he also says that she is looking fo a roomate and that if you help out working")
    print("at the bar for the next three days he will give you her adress and a recomondation")
    print("A = accept the offer (you might not make it tho)")
    print("B = refuse ")
    while 1:
        i = input(">") 
        if i =="A":
            print("you end up working the three days there and they go very well")
            r = 7
            break
        elif i == "B":
            print("you dont make it to the festival int the capital in time")
            print("failed ending")

if r == 7:
    print("pres enter to continue")
    input()
    print("you and the bartender have become good freinds and he even offers to have a freind")
    print("give you a ride to the festival")
    print("sam then visits the adress of the daugther. she i super happy to have you as a roomate")
    print("and even offers you a job in the up comming festival")
    print("A = work as security")
    print("B = work behind the scenes")
    while 1:
        i = input(">")
        if i == "A":
            print("you end up saving the life of the president of the country and are awarded citenzishp")
            print("the lucky ending")
            break
        elif i == "B":
            print("everything seems to be going wel into you see your roomate being harased by two guys")
            r = 8 
            break
if r == 8:
    print("A = don't do a thing")
    print("B = try and help her")
    print("C = get help")
    while 1:
        i = input(">")
        if i == "A":
            print("the next day your kicked out of the appartment and rightfully so")
            print("and now you are back to square one")
            print("the ULTIMATE failed ending")
            break
        elif i == "B":
            r = 10 
            break
        elif i == "C":
            print("you cant seem to find anyone")
            r = 9
            break
if r == 10:
    print("you get beat up but help dose arrive. you and your roomate live together a good freinds for many years")
    print("the basic ending")
if r == 9:
    print("A = keep searching")
    print("B = go back")
    while 1:
        i == input(">")
        if i == "A":
            print("you keep searching and then run into the same guy who robbed you of your past life a year ago")
            print("you then end up having a awsome fight on the rooftop of the stadium like its the final fight in a anime.")
            print("the music roars and you manage to win with a epic drop kick(he's probobly fine)")
            print("your roomate has been kidnaped tho")
            print("the sad ending")
            break
        elif i == "B":
            r = 10 
            break


