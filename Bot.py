#CHATBOT_PROJECT
flag=True
flag2=True
print("TmBot: Hi\n")                                                            #Greetings from bot
greet=('hi','hello','hey','namaste','whats up')                                 #Tuple containing types of user response to start conversation
resp=('TmBot: Namaste! Welcome to Tata Motors')                                 #Tuple containing the response for number of input as greeting from user


cars=['1. Tata Punch','2. Tata Nexon','3. Tata Altroz',                         #List having names of cars of Tata Motors
      '4. Tata Tiago','5. Tata Harrier','6. Tata Safari',
      '7. Tata Tigor','8. Tata Nexon EV','9. Tata Tigor EV',
      '10. Tata Tiago NRG']
cars2=['Tata Punch','Tata Nexon','Tata Altroz',                                 #Replica of List cars to check input from user to carry forward further conversation
      'Tata Tiago','Tata Harrier','Tata Safari',
      'Tata Tigor','Tata Nexon EV','Tata Tigor EV',
      'Tata Tiago NRG']


cartype=['1. Hatchback','2. Sedan','3. SUV']                                    #List of category of cars in Tata
cartype2=['Hatchback','Sedan','SUV']                                            #Replica of List cartype to check input from user to carry forward further conversation


Hatchback=['Tata Tiago','Tata Altroz','Tata Tiago NRG']                         #List of all cars under Hatchback category 
Sedan=['Tata Tigor']                                                            #List of all cars under Sedan category
SUV=['Tata Punch','Tata Nexon','Tata Nexon EV',                                 #List of all cars under SUV category 
     'Tata Harrier','Tata Safari']


questions=['1. Car List','2. Car Cost','3. Car Type','4. Upcoming Launch']      #List of facilities chatbot provides


cost=['5.49 lakh','7.30 lakh','5.86 lakh','5.00 lakh','14.39 lakh',             #List of cost of cars synced with List of Cars
      '14.99 lakh','5.68 lakh','13.99 lakh','11.99 lakh','6.57 lakh']


while(flag==True):                                                              #For running loop Infinite Times
  user_response=input("You:")
  print("\n")
  if user_response.lower() in greet:
      print(resp)
      while(flag2==True):
        print("\nTmBot: Choose the service you want to avail")
        for x in questions:
          print(x)
        i=int(input("\nYou:"))
        if i==1:                                                                 #Response for Question 1
          print("\n")
          for y in cars:
           print(y)
          print("\nTmBot: Do you want to continue the service? Y/N")
          confirm_input=str(input("You:"))
          if confirm_input=="Y" or confirm_input=="y":
              continue
          elif confirm_input=="N" or confirm_input=="n":
            print("TmBot: Dhanyawad")
            print("******Conversation Ended******")
            print("\nTmBot: Hi\n")
            break
        elif i==2:                                                               #Response for Question 2
          print("\nTmBot: Which car cost do you want to know??")
          print("\n")
          for y in cars2:
            print(y)
          car_input=str(input("\nYou:"))
          index=cars2.index(car_input)
          print("\nTmBot: Cost of ",cars2[index],'is',cost[index],'rs')
          print("\nTmBot: Do you want to continue the service? Y/N")            #Taking response from user for continuing the conversation of ending it
          confirm_input=str(input("You:"))
          if confirm_input=="Y" or confirm_input=="y":
              continue
          elif confirm_input=="N" or confirm_input=="n":
            print("\nTmBot: Dhanyawad")
            print("******Conversation Ended******")
            print("\nTmBot: Hi\n")
            break
        elif i==3:                                                               #Response for Question 3
            print("\nTmBot: Which Car Type you want to explore?")
            for z in cartype:
              print(z)
            type_input=str(input("\nYou: "))
            index=cartype2.index(type_input)
            if index==0:
              print("\nTmBot: Cars in Hatchback Category are:")
              for j in Hatchback:
                print(j)
            elif index==1:
              print("\nTmBot: Cars in Sedan Category are:")
              for j in Sedan:
                print(j)
            elif index==2:
              print("\nTmBot: Cars in SUV Category are:")
              for j in SUV:
                print(j)
            else:
              print("\nERROR")
              break
            print("\nTmBot: Do you want to continue the service? Y/N")
            confirm_input=str(input())
            if confirm_input=="Y" or confirm_input=="y":
                  continue
            elif confirm_input=="N" or confirm_input=="n":
                print("\nTmBot: Dhanyawad")
                print("******Conversation Ended******")
                print("\nTmBot: Hi\n")
                break
        elif i==4:                                                                #Response for Question 4
            print("\nTmBot: Upcoming Launches from Tata Motors are:")
            print("1. Tata Tiago EV")
            print("2. Tata Altroz EV")
            print("\nTmBot: Do you want to continue the service? Y/N")
            confirm_input=str(input())
            if confirm_input=="Y" or confirm_input=="y":
                  continue
            elif confirm_input=="N" or confirm_input=="n":
                print("\nTmBot: Dhanyawad")
                print("******Conversation Ended******")
                print("\nTmBot: Hi\n")
                break     
 
