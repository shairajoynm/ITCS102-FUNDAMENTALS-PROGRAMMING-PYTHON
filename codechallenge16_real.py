import os
print("----------------------------------------")
print("Student Information System")
print("----------------------------------------")

student_list = {}




while True:

    print("\nChoose what you want to do \n a - Add Information \n b - Review Record \n c - Search \n d - Delete a Record \ne -  Edit or Modify a Record\n")

    choosing = input(" =--> ").lower()

#add
    if choosing == 'a':
        id = eval(input("Student ID number:  "))
        last_name = input("Last name: ").lower()
        first_name = input("First name: ").lower()
        course = input("Program: ")

        student_list[id]= [last_name, first_name, course]
    
        os.system('cls')
        print("\nRecord Saved\n")
        continue

#review       
    elif choosing == 'b':
        for ids, record in student_list.items():
            print(f"Student ID: {ids} in student record {record}")
        continue

#search
    elif choosing == 'c':
        os.system('cls')
        ask = eval(input("Student ID: "))
        print(f"Record shows {student_list[ask]}")
        print("\nRecord Found\n")

#delete
    elif choosing == 'd':
        os.system('cls')
        ask_2 = eval(input("Student ID to delete: "))
        if ask_2 in student_list:
            del student_list[ask_2]

        print("Record Deleted")

#modify or edit

    elif choosing == 'e':
        ask_3 = input("Student ID:  ")
        for a in student_list[ask_3]:
                print(f"{a}")
        
        lname = input("Input Student Last Name: ")
        fname = input("Input Student First Name: ")
        course = input("Input Student Course: ")

        student_list[ask_3][0] = lname
        student_list[ask_3][1] = fname
        student_list[ask_3][2] = course


            