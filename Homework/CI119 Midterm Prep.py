import random ##imports the liabrary that allows use of random functions
import sys
print("Copywrite MRB 3/23/2018")
Correct_Answers = 0
Incorrect_Answers = 0
questions = 0
reAsk = [];
done = False;
def questionGen(info): ##A function for the creation of multiple choice questions with 4 possible option
    global Correct_Answers ##calls the program-wide variable
    global Incorrect_Answers
    global questions
    global reAsk
    try: color = sys.stdout.shell
    except AttributeError: raise RuntimeError("Use IDLE 3.5+")
    questions += 1
    ##begin answer list creation and randomization
    answerList=[]
    answerList.append(info[1])
    answerList.append(info[2])
    answerList.append(info[3])
    answerList.append(info[4])
    random.shuffle(answerList)
    ##end answer list
    print(str(questions)+". " + info[0])
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
            shell.write("You have chosen wisely", "STRING")
            print('\n');
            Correct_Answers += 1
            break
        elif userAns in iAns:
            shell.write("You have chosen poorly\n",'COMMENT')
            print('\n');
            Incorrect_Answers += 1
            if not(info in reAsk):
                reAsk.append(info);
            break
        else:
            print("Not a valid Answer")
    cAns.clear()
    iAns.clear()
        ##end answer check
        ##actual quiz questions
Quiz_1 = [["Name the Hash", 'SHA',"DES", "AES", "RSA"], ["Which is the correct order?", "Hash then Encrypt", "Encrypt then Hash", "Hash only", "Encryption Only"], ["Is MFA more secure? ", "Yes", "No", "Who cares, it sucks", "What’s MFA?"], ["What attack is key exchange especially vulnerable too? ", "MitM", "DDos", "Hammers", "LOIC"], ["Is a PGP key symmetric or asymmetric?", "asymmetric", "symmetric", "who knows?", "both"], ["What is the primary operation used in encryption?", "XOR", "OR", "EQUIV", "AND"], ["The Basic model for how you can build and use a network and its resources is known as _____.", "OSI", "ICP", "ISO", "IEEE"], ["The basic job of a ____________ is to enforce and access control policy at the border of a network", "Firewall", "Router", "Switch", "Access Point"],
         ["A __________ is a critical element of a corporate network, allowing access to resources from around the world", "WAN", "LAN", "DHCP", "WPA"], ["A Secure VPN creates an authenticated and encrypted tunnel across a network", "True", "False", "VPN??", "What’s Secure?"], ["A _____ is a device that interconnects multiple networks and moves data between them.", "Router", "Hub", "Switch", "Cable"], ["Which is a simple device that improves network performance by only sending a packet to its intended destination", "Switch", "Hub", "TCP/IP", "Router"], ["What is the concept of ROT13", "Each letter corresponds to the letter 13 letters after it in the alphabet", "multiply the ASCII Hex by 13", "Rotate the enigma rotor 13 times", "Run the text through DES 13 times"]]
Networks_1 = [["What does TCP Stand For", "Transmission Control Protocol", "Total Containment Procedures", "Too Complicated process", "Transmission Containment Practice"], ["What does OSI Stand for?", "Open Systems Interconnection", "Open Security Model", "OverSaturated Interface", "Original System Interaction"], ["How many Layers does OSI have", "7", "9", "6", "8"], ["What is the lowest layer called?", "Physical", "Datalink", "Bit", "Fiber"], ["What is DNS used for?", "IP resolution", "Website Naming", "Communication", "Data Transfer"], ["Which is an IPv4 address", "10.0.0.1", "ADF908", "0110", "www.google.com"]]
Chap_10 = [["What device could you use to speed up a network?", "Switch", "RAM", "A personal Server", "Copper Cabling"], ["If you are a hiring manager looking to give an employee a probationary period\n how would you do it using Access Control", "Model of least Privilege", "A capability List", "requiring they bring their own device", "Ask for pervious samples of their work"], ["What tool can you use to find out where a website is hosted?", "traceroute", "ping", "dig", "a reverse dictionary"], ["How could you prevent someone from accessing your corporate network?", "With multiple control mechanisms", "By encrypting everything", "Preventing Physical Access", "Blacklists"]]
OSI_1= [["Which is not a layer of the OSI model?", "Access Control", "Data Link", "Session", "Application"], ["What is the Physical Layer responsible for?", "Signaling", "Hardware", "Formatting", "Physical addressing"], ["Which are the 1st and 7th layers of the OSI model, respectively?", "Physical, Application", "Physical, Presentation", "Data Link, Presentation", "Application, Presentation"],
          ["How does the Transport Layer function?", "Breaking data into packets and properly transmitting", "Breaking data into packets only", "Transmitting packets only", "Receiving packets and putting them back together"], ["What does the Data Link Layer do", "Transmit info on the same LAN", "Transmit data over a WAN", "Connect two specific computers via cable", "Connects separate departments"], ["When you write an e-mail program that operates in the Application Layer, which other layers should you be concerned about?", "The Application and Presentation Layers", "Only the Application Layer", "All 7 layers", "Down to the Network Layer"], ["Which layer includes file formats?", "Presentation Layer", "Network Layer", "Data Link Layer", "Physical layer"],
          ["Which is not an attribute of an organization using a private network for remote sites?", "It is inexpensive", "It is more reliable", "For security purposes", "For more control"], ["What is one way to keep confidential traffic within a department?", "Internal routers", "Internal hubs", "Border routers", "External Switches"], ["Which is a way to hide your IP address?", "Using NAT", "Using a LAN", "Using a Border router", "Using packet filtering"], ["What is not relevant to TCP/IP?", "It was made for better security", "Each computer needs to speak the 'same language'", "Each computer needs a separate ID", "It operates at the Network and Transport Layers"],
          ["What is ICMP primarily used for?", "Monitoring health of a network", "Creating routing systems", "Smurf attacks", "It isn't used anymore because most computers are programmed to ignore ping requests"], ["Which is not one of the three main categories of risk?", "MitM", "DOS", "Eavesdropping", "Reconnaissance"], ["Which is not a type of firewall?", "Network Inspection", "Packet filtering", "Stateful Inspection", "Application proxy"]]
ISS_1 = [["What does CIA stand for in Information Security?", "Confidentiality, Integrity, Availability", "Central Intelligence Agency", "Celestial Intervention Agency", "Confidence, Intelligence, Adversity"], ["Which of these is NOT a security domain", "System", "LAN to WAN", "User", "Workstation"], ["Which is a user domain threat", "Violation of Security policies", "Viruses", "Unauthorized Access", "MiTm"], ["Which of these is a Workstation threat?", "BYOD", "User Apathy", "Server Vulnerabilities", "Insecure communications"], ["Which of these is a LAN threat", "Unauthorized Access", "BYOD", "Probing", "Infected Emails"], ["Which of these is a LAN to WAN Threat", "Firewall Vulnerabilities", "Insecure Communications", "Viruses", "Violation of security policies"], ["Which of these is a WAN threat?", "MiTM", "BYOD", "User Apathy", "Server Vulnerabilities"]]
Crypto_1 = [["What does OTP stand for", "One time Pad", "On the Program", "One Time Purchase", "Over the plan"], ["Who did the Verona Project Target?", "The Soviets", "The USA", "The Germans", "The Italians"], ["How did the US generate OTPs?", "Cosmic Radio Noise", "a random number generator", "by throwing darts", "manufacturing differences between computers"], ["Which of these is a Block Cipher", "AES", "ROT13", "XOR", "SHA"], ["What is SSL used for", "Certificate Validation", "Socket Testing", "DNS", "Surfing the Internet"]]
RBAC_1 = [["What does DAC stand for in a network security context?", "Discretionary Access Control", "Digital Analog Converter", "Direct Access Control", "Dictionary Attack Computing"], ["What RBAC method is characterized by allowing Users to share their permissions", "DAC", "MAC", "RBAC", "ACM"], ["What does A[s, o] mean in terms of an ACM?", "Access of Subject on Object", "The Action of an Object on a Subject", "An array of subjects and objects", "a function of S and O"], ["How would an attack first try to crack a stolen password hash?", "With a rainbow table", "By guessing", "with a reverse Hash generator", "With a password cracker"]]
Chap1_def = [["What is Cyberspace?", "Users, Pages, etc. in the online domain", "Computers in Space", "The Internet", "Computers on a network"], ["What is a threat?", "Anything that could damage a system", "A bomb", "Implied Malice", "A Virus"], ["What is Malware?", "Code that causes a specific undesired action to occur", "A program meant to damage a system", "Preinstalled programs on a computer", "Badly written programs"], ["What is a Virus?", "A program to cause damage to a system", "A computer Sickness", "Bloatware", "Something that slows down your computer"], ["What is a thin client", "A computer with no Hard drive", "A tablet", "A computer with no network connectivity", "Something with little data"], ["What is the LAN to WAN Domain?", "The Domain where Local IT infrastructure connects to the outside world", "The area where the Data link layer functions", "The Domain where Users send Data", "The border of the network"], ["What is the port for HTTP?", "80", "22", "53", "11211"], ["What is the port for DNS?", "53", "23", "69", "52"], ["What is a port in networking?", "A logical connection place", "A physical connection place", "An ordered group for session connections", "A place where files are moved in a computer"], ["What is a proxy server?", "A server where traffic can be screened", "A server to mask IP", "A tactic used by hackers to fool a system", "A traffic direction server"], ["What does an Intrusion Detection System do?", "Monitors a network for malicious activity", "Prevents unauthorized intrusion", "Scans inbound traffic for attacks", "Actively scan for malicious activity"], ["How does an IP-Stateful Firewall work?", "By comparing IPs with authorized traffic", "By IP blacklists", "By examining an IP vs. the packet content", "By only allowing outside communication in specific circumstances"], ["Where is the weakest point in the network?", "Users", "The network edge", "The workstations", "Communications on a WAN"]]
Chap1_sen = [["How could you mitigate the risk of data being stolen from a network?", "Institute WPA Encryption", "Hide the network", "Use code in communications", "Instiute WEP encryption"], ["How can you actively reduce the risk of a network intrusion going undetected?", "Using Intrusion Prevention Systems", "firewalls", "Using Intrusion Detection systems", "By periodically resetting the network"], ["How can you prevent port-scanning reconnaissance?", "By disabling PING", "By disabling IMAP", "By hiding your network servers", "With a Stateful Inspection Firewall"], ["How can you reduce the risk of unauthorized access to your network?", "By securing the network and requiring authentication", "By using only physical communication", "By using Connection filtering", "By hiding the network"], ["How can you reduce the risk of a disgruntled employee sabotaging your systems? (Choose the most correct one)", "Track usage and raise flags when abnormal usage occurs, grant users access to only what they need to do their jobs", "Track all employees and fire disgruntled ones as quickly as possible", "Lock down IT systems during a certain timeframe", "protect workstations against physical tampering"]]
Class_Review = [["What is Kerchoff's Principle?", "That a cryptosystem should be secure even if all details (except the key) are known", "That a cyber-system should be secret", "That a system should be secure even if the key is known", "That a cyber-System should be widely used to be effective"], ["Where does modern cryptography have its roots?", "WWII", "WWI", "The Cold War", "The Roman Empire"], ["How do you attack a Substitution Cipher?", "Frequency Analysis", "Distributed Computing", "By factoring a key", "With a dictionary attack"], ["What was ARPANet?", "The precursor to the internet", "A WWII Spy ring", "A Communication system", "another word for the internet"], ["What is a worm?", "Self-replicating malware", "Undetected Malware", "Intrusion Software", "A kind of virus"], ["What is a Zero-Day?", "A vulnerability present at Launch", "The first day of a Machine", "the start of the programming Epoch", "A hacked Exploit"], ["What does it mean to 'Fingerprint' code?", "To identify the idiosyncrasies of a programmer in their code", "To identify a virus or other program", "The memory location of a piece of software", "Using computers to identify a hacker based on their actions"]]
Chap9 = [["What does nonrepudiation do?", "Prevents someone from denying a previous statement or action", "Protects against constant use of the same key", "Confirms identity", "Denies access to rejected parties"], ["What is a substitution cipher?", "It replaces the characters with different characters", "It rearranges the characters", "It uses a mathematical formula", "It is a random encryption"], ["What is a simple substitution cipher?", "Caesar cipher", "DES", "Enigma", "BlowFish"], ["For asymmetric encryption, who's key do you use for encryption?", "Receiver's public key", "Receiver's private key", "Sender's private key", "Sender's public key"], ["Does symmetric encryption provide authentication?", "No", "Yes", "Sometimes", "Depends"], ["Which weakness of substitution do algorithms minimize?", "Frequency analysis", "Authentication", "Denial of Service", "Dictionary attacks"], ["what is a key directory?", "Trusted repository of all public keys", "Individual password storage", "List of broken encryptions", "List of authorized users"]]
Chap4 = [["What is Risk Management?", "The Process of identifying, assessing, prioritizing, and addressing risks", "The mitigation of risks", "The process of responding to risks", "The prioritization and addressing of risks"], ["The effect of a risk can be:", "A positive or negative effect", "a negative effect", "a positive effect", "no effect"], ["Which of these is not part of the risk management process", "Risk taking", "Risk Identification", "Risk Planning", "Risk control"], ["What is a risk register", "A list of risks", "A measure of the effect of a risk", "Paperwork companies must file for loans", "A list of the costs of a risk"], ["Is Risk analysis Quantitative or Qualitative", "Both", "Neither", "Quantitative", "Qualitative"], ["Which of these is the measure of a medium impact risk", "Major", "Minor", "Average", "Critical"], ["Is a disaster recovery plan part of a Business continuity plan?", "Yes", "No", "Only In safety critical industries", "They are the same thing"], ["How should you assume disasters occur?", "Murphy's Law", "In singletons", "All at once", "randomly"], ["What is the advantage of a hotsite in the event of a disaster", "It allows for fast recovery", "it's inexpensive", "It prevents virus infections", "it allows for easy forensics if the network crashes"], ["Which DRP Exercise is also called a Tabletop exercise?", "A structured walkthrough", "A Simulation Test", "A checklist test", "An Assessment test"], ["Which US law requires publicly traded companies to report information to the US government?", "Sarbanes-Oxley Act", "Gramm-Leach-Bliley Act", "Payment Card Industry Security Standard", "USA Patriot Act"], ["Which of these is NOT an authentication method", "CAPATCHA", "Kerberos", "Tokens", "Challenge Response Handshakes"]]
misc = [["Which of these is NOT a method of social engineering in network security", "Malicious USBs", "Phishing", "Intimidation", "Appeal for Help"], ["Which criteria do organizations NOT take into effect when assessing the classification of an object", "Threat", "Sensitivity", "Value", "Criticality"], ["What is the difference between an ACL and an ACM", "ACLs associate permissions with Users, ACM's associate permissions with files", "ACL's associate permissions with files, ACM's associate permissions with users", "ACL's are part of DAC while ACMS are part of MAC", "ACLs are part of MAC while ACMs are part of DAC"], ["What domains are access controls implemented in", "WAN to LAN and Workstation", "User and workstation", "Workstation and WAN", "LAN and WAN"], ["Are companies legally required to report data breaches", "Yes", "No", "Only in California", "Only if the breach steals unencrypted data"], ["What is the attack used to mask an illegitimate website with a legitimate IP", "DNS Poisoning", "DNS Amplification", "Social Engineering", "TCP sequence guessing"], ["What is the attack used to send large amounts of traffic at a target from a small source", "DNS Amplification", "DDoSing", "Botnets", "Proxy redirect"], ["What is Wireshark used for?", "Packet sniffing", "Building network infrastructure", "connection diagnosing", "Building routing systems"], ["What is the biggest data breach to date", "Yahoo", "Equifax", "OPM", "Facebook"], ["What kind of malware locks a computer and demands money to unlock it", "Ransomware", "Spyware", "Bloatware", "freeware"]]
Mobile_Security = [["What is the largest attack vector in mobile security?", "Androidlotoor", "Rootkits", "EternalBlue", "Infected APKs"], ["What is a vulnerability associated with bring your own device?", "Malware Transmission", "electronic snooping", "lost productivity", "Data theft"]]
midTerm = [["Which of the following is used for netflow monitoring?", "TCPDump", "ping", "traceroute", "pyshark"], ["Domain infomation gropper is used to troubleshoot___.", "Domain Name Server", "Authentication Server", "Content Centric server", "Web server"], ["The IP packet consists of which of the following", "All", "Payload", "TCP Header", "IP Header"], ["Hub is a network device at which Level?", "Physical", "Datalink", "Transport", "Network"], ["Private Key in PKI is used to ", "decrypt message", "encrypt message", "cipher text", "All"], ["Domain Name Server proves ___ to a browser program", "URL", "MAC", "IP", "None of these"], ["While going up from the physical to application layer, a packet goes throught", "De-encapsulation", "Encapsulation", "Esclation", "None of the above"], ["The more secure form of HTTP uses which of the following protocols?" "SSL", "RSA", "DES", "El-Gamal"], ["Internet is more developed form of ", "Circuit Switched Network", "Packet Switched Network", "Internet Contorl Message Protocol", "None of these"], ["The following are examples of a Single Sign On", "Kerberos", "SESAME", "RADIUS", "All of these"], ["Access Control Mechanism is implemented primarily in ", "Authorization Table", "Capabilities", "Access Control Lists", "All of These"], ["Which do you trust more when the most when the senders ID is vauge?", "Hash", "Encryption", "TLS", "Antivirus"], ["Which do you trust more when the identty of the sender is not vauge?", "Encryption", "Hash", "TLS", "Antivirus"], ["Which of the following are the pillars of infomation assurance", "All of these", "Integrty", "Authentication", "Non-Repudiation"], ["The root certificate belongs to ", "Signing Authority", "Sender", "receiver", "all of these"], ["Public and private keys are part of a symmetric crypto system", "True", "False", "Dont pick this one", "Or this one"], ["Which of these is an example of a block cipher", "AES", "XOR", "Ciphertext AutoKey", "HC256"], ["Access Control's functions is to control active ___ have access to a ___\n with some specific access operation.", "1-object, 2-subject", "1-subject, 2-object", "1-directory, 2-user", "None of these"], ["In DAC, users can be given the ability of passing on their ____ to others users", "Privileges", "roles", "indentity", "Administration"], ["Magnetic Stripes on access cars that they give ou in hotels as door keys are an example of ___", "Passive Tokens", "Active Tokens", "One times passive passwords", "RSA"], ["Biometric readers preform", "Biometirc matching", "Pattern recongnition", "feature extraction", "Authentication"], ["In packet switiching, _____ are routed through the network noes", "Packets", "Frames", "Data", "genes"], ["A packet typically contains__" "All of these", "MAC", "IP", "Port number"], ["Which protocol is used in ping?", "ICMP", "TCP", "URL", "FTP"], ["Data Frames are used at which layer?", "Datalink", "Physical", "Transport", "session"], ["Peer to Peer networks are", "All of these", "Complex", "Easy to set up", "reliable"]]
preMidterm = Quiz_1+Networks_1+Chap_10+OSI_1+Crypto_1+RBAC_1+Chap1_def+Chap1_sen+Class_Review+Chap9 + Chap4+misc;
postMidterm = Mobile_Security
question = preMidterm + postMidterm + midTerm
random.shuffle(question);
qList=[]
Qnum=int(input("How many questions do you want? (enter 0 for all of them)"))
if Qnum == 0:
    qList = question
    print("Using All", len(qList), "Questions");
elif Qnum > len(question):
         print("Your number is greater then the number of avalible questions, using all avalible.")
         qList = question
else:
    print("Generating Quiz")
    q = [];
    while len(q) < Qnum:
         n = random.randint(0, len(question)-1)
         if n in q:
             continue
         else:
             q.append(n)
    for i in q:
        qList.append(question[i])
for i in qList:
    questionGen(i)
##end quiz gen
print("Your score is",int((Correct_Answers/questions)*100), "Percent") ##Prints the score
while not(done) and len(reAsk) != 0:
    redo = input("Do you want to redo the questions you missed?[Y/N] ")
    if redo == 'y' or redo == 'Y':
        print("Reasking questions")
        random.shuffle(reAsk)
        Correct_Answers = 0
        Incorrect_Answers = 0
        for i in reAsk:
            questionGen(i)
        print(" you got ", Correct_Answers, "out of ", len(reAsk), "of thoes right");
        done = True
    elif redo == 'n' or redo == 'N':
        print("Ok, exiting program")
        done = True
    else:
        print("Please input Y or N")
        done = False
