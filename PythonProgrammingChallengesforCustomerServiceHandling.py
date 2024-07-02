print("\n Ticket System \n")
Start_Over=('Y')
while Start_Over!=('y', 'YES', 'yes', 'Yes'):
    print("\nTicket System")
    issues=["Login","Service","General"]
    name=input("What is your name?: ")
    print(" What is your issue type Login for login issues, type Service for service issues, and type General if you have general questions....")
    queue=1
    ticket=input("Type your issue as mentioned above: ")

    if (ticket=="Login","login"):
        queue=queue=+1
        print(name,"your",ticket,"issue is documented and is #", queue, "in the queue")
        print(" We have identified your login issue, please log off your computer and sign in again")
        follow_up1=input("Are you able to log off your computer? Type #1 if you can log off now to complete your login steps. Type #2 if you plan to log off at a later time: ")
        print(" We have documented your response in our records. Outcome: Customer", name, ticket,"issue was #", queue, " in the queue and is now closed")
    elif (ticket=="Service","service"):
        queue=queue*2
        print(name,"your",ticket,"issue is documented and is #", queue, "in the queue")
        print(" We have identified your service issue, please log off your computer and sign in again")
        follow_up1=input("Are you able to log off your computer? Type #1 if you can log off now to complete your login steps. Type #2 if you plan to log off at a later time: ")
        print(" We have documented your response in our records. Outcome: Customer", name, ticket,"issue was #", queue, " in the queue and is now closed")
    elif (ticket=="General","general"):
        queue=queue*3
        print(name,"your",ticket,"issue is documented and is #", queue, "in the queue")
        print(" We have identified your service issue, please log off your computer and sign in again")
        follow_up1=input("Are you able to log off your computer? Type #1 if you can log off now to complete your login steps. Type #2 if you plan to log off at a later time: ")
        print(" We have documented your response in our records. Outcome: Customer", name, ticket,"issue was #", queue, " in the queue and is now closed")








