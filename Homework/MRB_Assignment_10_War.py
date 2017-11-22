from random import randint

suits = {
    0: 'Hearts',
    1: 'Spades',
    2: 'Diamonds',
    3: 'Clubs'
}

cards = {
    0: 'Ace',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'Jack',
    11: 'Queen',
    12: 'King'
}
total_cards=[]

def draw_cards(num_of_cards, list_dealt=[]): ##Edited Ashish's function so that it reutned the keys rather then a list of strings
    for z in range(num_of_cards):
        x = randint(0,3) #random integer 0 to 3 to pick suit
        y = randint(0,12) #random integer 0 to 12 to pick card
        mycard=[y,x]
        if mycard not in list_dealt:
            list_dealt.append(mycard) 
        else:
            num_of_cards = num_of_cards - z
            return draw_cards(num_of_cards,list_dealt)
            
    return list_dealt
play=True
while play==True:
    mydraw = draw_cards(6,total_cards)#call the function with the number of cards you want. 
    P1_hand=total_cards[0:3]
    P2_hand=total_cards[3:6]
    P1Sorted=sorted(P1_hand)
    P2Sorted=sorted(P2_hand)
    if P1Sorted[2][0]>P2Sorted[2][0]:
        print("Player 1 drew", end=' ')
        for i in P1Sorted:
            z="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(z, end=", ")
        print("Player 2 drew", end=' ')
        for i in P2Sorted:
            k="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(k, end=', ')
        print("Player 1 won!")
    elif P2Sorted[2][0]>P1Sorted[2][0]:
        print("Player 1 drew", end=' ')
        for i in P1Sorted:
            z="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(z, end=", ")
        print("Player 2 drew", end=' ')
        for i in P2Sorted:
            k="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(k, end=', ')
        print("Player 2 won!")
    elif P1Sorted[2][1]<P2Sorted[2][1]:
        print("Player 1 drew", end=' ')
        for i in P1Sorted:
            z="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(z, end=", ")
        print("Player 2 drew", end=' ')
        for i in P2Sorted:
            k="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(k, end=', ')
        print("Player 1 Won!")
    elif P2Sorted[2][1]<P1Sorted[2][1]:
        print("Player 1 drew", end=' ')
        for i in P1Sorted:
            z="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(z, end=", ")
        print("Player 2 drew", end=' ')
        for i in P2Sorted:
            k="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(k, end=', ')
        print("Player 2 Won!")
    else:
        print("Player 1 drew", end=' ')
        for i in P1Sorted:
            z="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(z, end=", ")
        print("Player 2 drew", end=' ')
        for i in P2Sorted:
            k="{0} of {1}".format(cards[i[0]],suits[i[1]])
            print(k, end=', ')
        print("Something broke because there was a tie")
    z=input("Do you want to play again?[Y/N] ")
    if z=='Y' or z=='y':
        play=True
    if z=='N' or z=='n':
        print("thanks for playing, please come again")
        play=False
    total_cards=[]
