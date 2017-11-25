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
    mydraw=[]
    mydraw=draw_cards(3,mydraw)
    hand=sorted(mydraw)
    for i in hand:
         z="{0} of {1}".format(cards[i[0]],suits[i[1]])
         print(z, end=", ")
    if hand[0][1]==hand[1][1] and hand[1][1]==hand[2][1]:
        if hand[1][0]==hand[0][0]+1 and hand[2][0]==hand[1][0]+1:
            print("You got a straight flush!")
        else:
            print("You got a flush!")
    elif hand[0][0]==hand[1][0] and hand[0][0]==hand[2][0]:
        print("You got three of a kind!")
    elif hand[0][0]==hand[1][0] or hand[0][0]==hand[2][0] or hand[1][0]==hand[2][0]:
        print("You got a pair!")
    elif hand[1][0]==hand[0][0]+1 and hand[2][0]==hand[1][0]+1:
        print("You got a straight!")
    else:
        print("You got a bad hand. :(")
    z=input("Do you want to play again?[Y/N] ")
    if z=='Y' or z=='y':
        play=True
    if z=='N' or z=='n':
        print("thanks for playing, please come again")
        play=False
        
