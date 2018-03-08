##This is the homework for week 4, as created by Mark Burrell, and Everything Runs
import random ##imports the liabrary that allows use of random functions
print("HW4_MRB_09_26_17")
Correct_Answers = 0
Incorrect_Answers = 0
questions = 0
def questionGen(info): ##A function for the creation of multiple choice questions with 4 possible option
    global Correct_Answers ##calls the program-wide variable
    global Incorrect_Answers
    global questions
    questions +=1
    ##begin answer list creation and randomization
    answerList=[]
    answerList.append(info[1])
    answerList.append(info[2])
    answerList.append(info[3])
    answerList.append(info[4])
    random.shuffle(answerList)
    ##end answer list
    print(info[0])
    print("A",answerList[0],"\n")
    print("B",answerList[1],"\n")
    print("C",answerList[2],"\n")
    print("D",answerList[3],"\n")
    ##Sets up the answer check lists
    if info[1] == answerList[0]:
        cAns=['A','a']
        iAns=['B','b','c','C','d','D']
    elif info[1] == answerList[1]:
        cAns=['B','b']
        iAns=['A','a','c','C','d','D']
    elif info[1] == answerList[2]:
        cAns=['C','c']
        iAns=['B','b','a','A','d','D']
    elif info[1] == answerList[3]:
        cAns=['D','d']
        iAns=['B','b','c','C','a','A']
    ##end creation of answer check lists
        ##asks the user for input and checks it against the lists, responds appropriatly
    while True:
        userAns=str(input("What is the Answer? "))
        if userAns in cAns:
            print("You have chosen wisely\n")
            Correct_Answers+=1
            break
        elif userAns in iAns:
            print("You have chosen poorly\n")
            Incorrect_Answers+=1
            break
        else:
            print("Not a valid Answer")
    cAns.clear()
    iAns.clear()
        ##end answer check
        ##actual quiz questions
qList = [["Name the Hash", 'SHA',"DES","AES","RSA"],["Which is the correct order?", "Hash then Encrypt","Encrypt then Hash","Hash only","Encryption Only"],["Is MFA more secure? ","Yes","No","Who cares, it sucks","Whats MFA?"],["What attack is key exchange especially vulnerable too? ", "MitM","DDos","Hammers","LOIC"],["Is a PGP key symmetric or asymetric?", "asymetric", "symetric", "who knows?", "both"],["What is the primary operation used in encryption?", "XOR", "OR", "EQUIV","AND"], ["The Basic model for how you can build and use a network and its resoruces is known as _____.", "OSI", "ICP", "ISO", "IEEE"],["The basic job of a ____________ is to enforce and access control policy at the border of a network", "Firewall", "Router", "Switch", "Access Point"],
         ["An __________ is a critical element of a corprate network, allowing access to resoruces from around the world", "WAN", "LAN", "DHCP", "WPA"],["A Secure VPN creates an authenticated and encrpted tunnel across a network", "True", "False","VPN??", "Whats Secure?"],["A _____ is a device that interconnects multiple networks and moves data between them.", "Router", "Hub", "Switch", "Cable"],["Which is a simple device that improves network profmance by only sending a packet to its intended destination", "Switch", "Hub", "TCP/IP", "Router"]]
qList2 = [["What does TCP Stand For", "Transmission Control Protocol", "Total Containtment Procedures", "Too Complicated processe", "Transmission Containtment Practice"],["What does OSI Stand for?","Open Systems Interconnection", "Open Security Model", "OverSaturated Interface","Original System Interaction"], ["How many Layers does OSI have", "7", "9", "6", "8"],["What is the lowest layer called?", "Physical","Datalink","Bit","Fiber"],["What is DNS used for?", "IP resolution", "Website Naming","Communcation","Data Transfer"],["Which is an IPv4 address", "10.0.0.1", "ADF908", "0110", "www.google.com"]]
qList3 = [["What device could you use to speed up a network?", "Switch", "RAM", "A personal Server", "Copper Cabling"],["If you are a hiring manager looking to give a employee a probationary period\n how would you do it using Access Control", "Model of least Privlage", "A capability List", "requring they bring their own device", "Ask for pervious samples of their work"],["What tool can you use to find out where a website is hosted?", "traceroute","ping", "dig", "a reverse dictionary"],["How could you prevent someone from acessing your coprate network?", "With multiple control mechanisms", "By encrypting everything", "Preventing Physcical Acess", "Blacklists"]] 
qList4 = [["Which is not a layer of the OSI model?", "Acess Control", "Data Link", "Session", "Application"],["What is the Physical Layer responsible for?", "Signaling", "Hardware", "Formatting", "Physical addressing"],["Which are the 1st and 7th layers of the OSI model, respectively?", "Physical, Application", "Physical, Presentation", "Data Link, Presentation", "Application, Presentation"],
          ["How does the Transport Layer function?", "Breaking data into packets and properly transmitting", "Breaking data into packets only", "Transmitting packets only", "Receiving packets and putting them back together"],["What does the Data Link Layer do", "Transmit info on the same LAN", "Transmit data over a WAN", "Connect two specific computers via cable", "Connects separate departments"], ["When you write an e-mail program that operates in the Application Layer, which other layers should you be concerned about?","The Application and Presentation Layers","Only the Application Layer","All 7 layers","Down to the Network Layer"],["Which layer includes file formats?","Presentation Layer","Network Layer","Data Link Layer","Physcal layer"],
          ["Which is not an attribute of an organization using a private network for remote sites?","It is inexpensive","It is more reliable","For security purposes","For more control"],["What is one way to keep confidential traffic within a department?","Internal routers","Internal hubs","Border routers", "External Switches"],["Which is a way to hide your IP address?","Using NAT","Using a LAN", "Using a Border router","Using packet filtering"],["What is not relevant to TCP/IP?","It was made for better security","Each computer needs to speak the 'same language'","Each computer needs a separate ID","It operates at the Network and Transport Layers"],
          ["What is ICMP primarily used for?","Monitoring health of a network","Creating routing systems","Smurf attacks","It isn't used anymore because most computers are programmed to ignore ping requests"],["Which is not one of the three main categories of risk?","MitM","DOS","Eavesdropping","Reconnaissance"],["Which is not a type of firewall?","Network Inspection","Packet filtering","Stateful Inspection","Application proxy"]]
qList = qList2 + qList3 + qList4
random.shuffle(qList);
for i in qList:
    questionGen(i)

##end quiz gen
print("Your score is", Correct_Answers/questions, "or", Correct_Answers, "Out of ", questions) ##Prints the score
