# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# My student ID - w1953234
# Date - 12/14/2022


progress = 0
progress_module_trailer = 0
do_not_progress_module_retriever = 0
exclude = 0
mydict = {}

# Range function
def credit_range(credit):
    check = False
    for i in range (0,130,+20): #Range of Credits
        if (credit==i):
            check = True
            break
    return check

done_two = True
while done_two:
    # Input one - pass credits
    while True:
        try:
            pass_credits_int = int(input("Please Enter Your Credits At Pass : "))
            if (credit_range(pass_credits_int) == True):
                break
            else:
                print("\t", "*" * 5, "Pass credits are out of Range", "*" * 5, "\n")
                continue
        except:
            print("\t", "*" * 5, "Integer Required", "*" * 5, "\n")

    # Input two - defer credits
    while True:
        try:
            defer_credits_int = int(input("Please Enter Your Credits At Defer: "))
            if (credit_range(defer_credits_int) == True):
                break
            else:
                print("\t", "*" * 5, "Defer credits are out of Range", "*" * 5, "\n")
                continue
        except:
            print("\t", "*" * 5, "Integer Required", "*" * 5, "\n")
    # Input three - fail credits
    while True:
        try:
            fail_credits_int = int(input("Please Enter Your Credits At Fail : "))
            if (credit_range(fail_credits_int) == True):
                break
            else:
                print("\t", "*" * 5, "Fail credits are out of Range", "*" * 5, "\n")
                continue
        except:
            print("\t", "*" * 5, "Integer Required", "*" * 5, "\n")
    student_id = input("Enter your student ID ")

    total = pass_credits_int + defer_credits_int + fail_credits_int
# Conditions
    if total != 120:
        print("Total incorrect")
    elif pass_credits_int == 120:
        print("\nYour progression outcome :Progress")
        mydict[student_id] = ": Progress - ", ",", pass_credits_int, ",", defer_credits_int, ",", fail_credits_int
    elif pass_credits_int == 100:
        print("\nYour progression outcome :Progress (module trailer)")
        mydict[student_id] = ": Progress (module trailer) - ", ",", pass_credits_int, ",", defer_credits_int, ",", fail_credits_int
    elif pass_credits_int == 80 or pass_credits_int == 60:
        print("\nYour progression outcome :Do not Progress – module retriever")
        mydict[student_id] = ": Module retriever - ", ",", pass_credits_int, ",", defer_credits_int, ",", fail_credits_int
    elif pass_credits_int == 40 and 20 <= defer_credits_int <= 80:
        print("\nYour progression outcome :Do not Progress – module retriever ")
        mydict[student_id] = ": Module retriever - ", ",", pass_credits_int, ",", defer_credits_int, ",", fail_credits_int
    elif pass_credits_int == 40 and defer_credits_int == 0:
        print("\nYour progression outcome :Exclude ")
        mydict[student_id] = ": Exclude - ", ",", pass_credits_int, ",", defer_credits_int, ",", fail_credits_int
    elif pass_credits_int == 20 and 40 <= defer_credits_int <= 100:
        print("\nYour progression outcome :Do not Progress – module retriever ")
        mydict[student_id] = ": Module retriever - ", ",", pass_credits_int, ",", defer_credits_int, ",", fail_credits_int
    elif pass_credits_int == 20 and 0 <= defer_credits_int <= 20:
        print("\nYour progression outcome :Exclude ")
        mydict[student_id] = ": Exclude - ", ",", pass_credits_int, ",", defer_credits_int, ",", fail_credits_int
    elif pass_credits_int == 0 and 60 <= defer_credits_int <= 120:
        print("\nYour progression outcome :Do not Progress – module retriever ")
        mydict[student_id] = ": Module retriever - ", ",", pass_credits_int, ",", defer_credits_int, ",", fail_credits_int
    elif pass_credits_int == 0 and 0 <= defer_credits_int <= 40:
        print("\nYour progression outcome :Exclude ")
        mydict[student_id] = ": Exclude - ", ",", pass_credits_int, ",", defer_credits_int, ",", fail_credits_int

# Repetition for another set of inputs
    done = True
    while done:
        print("\nWould you like to enter another set of data?")
        while True:
            try:
                run_again = input("Enter 'y' for yes or 'q' to quit and view results: ")
                print("")

            # Set done to False if the 'q' string value found. It won't continue the while loop further and it runs the rest of programe(Histogram) and End
                if run_again.lower() == "q":
                    done = False
                    done_two = False
                    break
             # If the user input a letter out of "y" and "q", display the incorrect message and continue the while loop
                elif run_again.lower() != "y":
                    print("\t", "*" * 5, "User input is incorrect", "*" * 5, "\n")

            # If the user input "y", break the loop and user can input another record
                else:
                    print("\n")
                    print("-" * 75)
                    done = False
                    done_two = True
                    break
                # If user input char values like space then this program works
            except:
                print("\t", "*" * 5, "User input is incorrect", "*" * 5, "\n")
for k, v in mydict.items():
    print(k, *v)