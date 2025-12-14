import os
from Menu2_Calapit import *

#asking the user first
name = input("What's your name? -> ").lower()

#ask the user if they want to enter the program
ask_1 = input(f"\nHi {name}, do you want to enter the program? (yes/no) \n--> ").lower()

#main loop of whole program
while True:  

    if ask_1 == "yes":
        os.system('cls') #clearing history

        print("-------------------------------------")
        print(f"    Welcome to my program, {name}!")
        print("---------------------------------------")
        print("|             Main Menu               |")
        print("|                                     |")
        print("|       1. Print Statement            |")
        print("|       2. Variables                  |")
        print("|       3. Operators                  |")
        print("|       4. Conditional                |")
        print("|       5. Loops                      |")
        print("|       6. Lists                      |")
        print("|       7. Functions                  |")
        print("|       8. Exit the Program           |")
        print("---------------------------------------")

        # choosing option of main menu
        ask = input("Choose only one number -->  ").lower()
        print("-------------------------------------")

#for exit "8"
        if ask == "8":
            print("Thank you for your time!")
            exit()
#for Print statement "1"
        elif ask == "1":  
            os.system('cls')
            one()

            subto = True
            while subto == True:  #subtopics loop

                ask_print = input("Choose one subtopic (a/b/c) or Type 'main' for main menu --> ").lower()
                if ask_print == "main":
                    subto = False   #exit subtopics loop and return to main menu
                    break



                #for subtopics of 1
                if ask_print == "a":
                    os.system('cls')
                    one_a()  #the def for "a"

                    while True:
                        ask_printa = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                        
                        if ask_printa == "sub":
                            os.system('cls')
                            one()
                            #go back to subtopics loop
                            break
                        elif ask_printa == "main":
                            subto = False   #exit subtopics loop and return to main menu
                            break
                        else:
                            print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_print == "b":
                    os.system('cls')
                    one_b() #the def for "b"

                    while True:
                        ask_printa = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                        
                        if ask_printa == "sub":
                            os.system('cls')
                            one()
                            #go back to subtopics loop
                            break
                        elif ask_printa == "main":
                            subto = False   #exit subtopics loop and return to main menu
                            break
                        else:
                            print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_print == "c":
                    os.system('cls')
                    one_c() #the def for "c"

                    while True:

                        ask_try = input("Do you want to try the input? (yes/no) --> ").lower()
                        print("-----------------------------------------------------")
                        if ask_try == 'yes':
                            print("Input: ")
                            tanong = input("\tWhat's your name? --> ")
                            print(f"\nOutput: \nHi {tanong}")
                            print("-----------------------------------------------------")
                        elif ask_try == 'no':
                            break
                            

                    while True:
                        
                        ask_printa = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                        if ask_printa == "sub":
                            os.system('cls')
                            one()
                            #go back to subtopics loop
                            break
                        elif ask_printa == "main":
                            subto = False   #exit subtopics loop and return to main menu
                            break
                        else:
                            print("Invalid choice, please type 'sub' or 'main'.")
#for Variable "2"
        elif ask == "2":
            os.system('cls')
            two() #the def for "2"

            subtot = True
            while subtot == True:  #subtopics loop

                ask_printt = input("Choose one subtopic (a/b/c/d) or Type 'main' for main menu --> ").lower()
                if ask_printt == "main":
                    subto = False   #exit subtopics loop and return to main menu
                    break

                #for subtopics of 2
                if ask_printt == "a":
                    os.system('cls')
                    two_a() #the def for "a"


                    while True:
                        ask_printb = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                        
                        if ask_printb == "sub":
                            os.system('cls')
                            two()
                            #go back to subtopics loop
                            break
                        elif ask_printb == "main":
                            subtot = False   #exit subtopics loop and return to main menu
                            break
                        else:
                            print("Invalid choice, please type 'sub' or 'main'.")
                
                elif ask_printt == "b":
                    os.system('cls')
                    two_b()#the def for "b"

                    while True:
                        ask_printb = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                        
                        if ask_printb == "sub":
                            os.system('cls')
                            two()
                            #go back to subtopics loop
                            break
                        elif ask_printb == "main":
                            subtot = False   #exit subtopics loop and return to main menu
                            break
                        else:
                            print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_printt == "c":
                    os.system('cls')
                    two_c()#the def for "c"


                    while True:

                        ask_try = input("Do you want to try the input? (yes/no) --> ").lower()
                        print("-----------------------------------------------------")
                        if ask_try == 'yes':
                            print("Input: ")
                            anything = eval(input("Input anything : "))
                            print(f"\nOutput: \nThe type of data that you input is", (type(anything)))
                            print("-----------------------------------------------------")
                        elif ask_try == 'no':
                            break

                    while True:
                        ask_printb = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                        
                        if ask_printb == "sub":
                            os.system('cls')
                            two()
                            #go back to subtopics loop
                            break
                        elif ask_printb == "main":
                            subtot = False   #exit subtopics loop and return to main menu
                            break
                        else:
                            print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_printt == "d":
                    os.system('cls')
                    two_d() #the def for "d"


                    while True:
                        ask_printb = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()

                        if ask_printb == "sub":
                                os.system('cls')
                                two()
                                #go back to subtopics loop
                                break
                        elif ask_printb == "main":
                                subtot = False   #exit subtopics loop and return to main menu
                                break
                        else:
                                print("Invalid choice, please type 'sub' or 'main'.")

#for Operators "3"
        elif ask == "3":
            os.system('cls')
            three() #the def for "3"

            subtott = True
            while subtott == True:  #subtopics loop

                ask_printt = input("Choose one subtopic (a/b/c/d) or Type 'main' for main menu --> ").lower()
                if ask_printt == "main":
                    subtott = False   #exit subtopics loop and return to main menu
                    break

                #for subtopics of "3"
                if ask_printt == "a":
                    os.system('cls')
                    three_a()  #the def for "a"

                    while True:
                            ask_printt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printt == "sub":
                                os.system('cls')
                                three()
                                #go back to subtopics loop
                                break
                            elif ask_printt == "main":
                                subtott = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_printt == "b":
                    os.system('cls')
                    three_b()  #the def for "b"

                    while True:
                            ask_printt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printt == "sub":
                                os.system('cls')
                                three()
                                #go back to subtopics loop
                                break
                            elif ask_printt == "main":
                                subtott = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")
                
                elif ask_printt == "c":
                    os.system('cls')
                    three_c()  #the def for "c"
                
                    while True:
                            ask_printt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printt == "sub":
                                os.system('cls')
                                three()
                                #go back to subtopics loop
                                break
                            elif ask_printt == "main":
                                subtott = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_printt == "d":
                    os.system('cls')
                    three_d()  #the def for "d"
                
                    while True:
                            ask_printt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printt == "sub":
                                os.system('cls')
                                three()
                                #go back to subtopics loop
                                break
                            elif ask_printt == "main":
                                subtott = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")


#for Conditional "4"
        elif ask == "4":
            os.system('cls')
            four() #the def for "4"

            subtottt = True
            while subtottt == True:  #subtopics loop

                ask_printtt = input("Choose one subtopic (a/b/c/d) or Type 'main' for main menu --> ").lower()
                if ask_printtt == "main":
                    subtottt = False   #exit subtopics loop and return to main menu
                    break

                #for subtopics of "4"
                if ask_printtt == "a":
                    os.system('cls')
                    four_a()  #the def for "a"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                four()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")

                
                elif ask_printtt == "b":
                    os.system('cls')
                    four_b()  #the def for "b"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                four()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")



                elif ask_printtt == "c":
                    os.system('cls')
                    four_c()  #the def for "c"
                
                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                four()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")


                elif ask_printtt == "d":
                    os.system('cls')
                    four_d()  #the def for "d"
                
                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                four()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")


#for Loops "5"
        elif ask == "5":
            os.system('cls')
            five() #the def for "5"

            subtottt = True
            while subtottt == True:  #subtopics loop

                ask_printtt = input("Choose one subtopic (a/b/c/d) or Type 'main' for main menu --> ").lower()
                if ask_printtt == "main":
                    subtottt = False   #exit subtopics loop and return to main menu
                    break


            #for subtopics of "5"
                if ask_printtt == "a":
                    os.system('cls')
                    five_a()  #the def for "a"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                five()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_printtt == "b":
                    os.system('cls')
                    five_b()  #the def for "b"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                five()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")


                elif ask_printtt == "c":
                    os.system('cls')
                    five_c()  #the def for "c"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                five()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")
                
                elif ask_printtt == "d":
                    os.system('cls')
                    five_d()  #the def for "d"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                five()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")
                
#for Lists "6"
        elif ask == "5":
            os.system('cls')
            six() #the def for "6"

            subtottt = True
            while subtottt == True:  #subtopics loop

                ask_printtt = input("Choose one subtopic (a/b/c/d) or Type 'main' for main menu --> ").lower()
                if ask_printtt == "main":
                    subtottt = False   #exit subtopics loop and return to main menu
                    break


            #for subtopics of "6"
                if ask_printtt == "a":
                    os.system('cls')
                    six_a()  #the def for "a"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_printtt == "b":
                    os.system('cls')
                    six_b()  #the def for "b"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")


                elif ask_printtt == "c":
                    os.system('cls')
                    six_c()  #the def for "c"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")
                
                elif ask_printtt == "d":
                    os.system('cls')
                    six_d()  #the def for "d"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")
                

#for Lists "6"
        elif ask == "5":
            os.system('cls')
            six() #the def for "6"

            subtottt = True
            while subtottt == True:  #subtopics loop

                ask_printtt = input("Choose one subtopic (a/b/c/d) or Type 'main' for main menu --> ").lower()
                if ask_printtt == "main":
                    subtottt = False   #exit subtopics loop and return to main menu
                    break


            #for subtopics of "6"
                if ask_printtt == "a":
                    os.system('cls')
                    six_a()  #the def for "a"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_printtt == "b":
                    os.system('cls')
                    six_b()  #the def for "b"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")


                elif ask_printtt == "c":
                    os.system('cls')
                    six_c()  #the def for "c"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")
                
                elif ask_printtt == "d":
                    os.system('cls')
                    six_d()  #the def for "d"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")
                
#for Lists "6"
        elif ask == "6":
            os.system('cls')
            six() #the def for "6"

            subtottt = True
            while subtottt == True:  #subtopics loop

                ask_printtt = input("Choose one subtopic (a/b/c/d) or Type 'main' for main menu --> ").lower()
                if ask_printtt == "main":
                    subtottt = False   #exit subtopics loop and return to main menu
                    break


            #for subtopics of "6"
                if ask_printtt == "a":
                    os.system('cls')
                    six_a()  #the def for "a"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_printtt == "b":
                    os.system('cls')
                    six_b()  #the def for "b"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")


                elif ask_printtt == "c":
                    os.system('cls')
                    six_c()  #the def for "c"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")
                
                elif ask_printtt == "d":
                    os.system('cls')
                    six_d()  #the def for "d"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                six()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")
                

#for Function "7"
        elif ask == "7":
            os.system('cls')
            seven() #the def for "7"

            subtottt = True
            while subtottt == True:  #subtopics loop

                ask_printtt = input("Choose one subtopic (a/b) or Type 'main' for main menu --> ").lower()
                if ask_printtt == "main":
                    subtottt = False   #exit subtopics loop and return to main menu
                    break


            #for subtopics of "7"
                if ask_printtt == "a":
                    os.system('cls')
                    seven_a()  #the def for "a"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                seven()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")

                elif ask_printtt == "b":
                    os.system('cls')
                    seven_b()  #the def for "b"

                    while True:
                            ask_printtt = input("Type 'sub' to go back to subtopics or 'main' for main menu --> ").lower()
                            
                            if ask_printtt == "sub":
                                os.system('cls')
                                seven()
                                #go back to subtopics loop
                                break
                            elif ask_printtt == "main":
                                subtottt = False   #exit subtopics loop and return to main menu
                                break
                            else:
                                print("Invalid choice, please type 'sub' or 'main'.")


    #for the "no" in entering program
    elif ask_1 == 'no':
        print("Alright, come back again next time!")
        exit()

    else:
        print("Invalid Choice. Please Try Again")
        exit()

                


