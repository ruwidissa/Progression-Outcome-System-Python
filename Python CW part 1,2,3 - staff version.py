# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# My student ID - w1953234
# Date - 12/13/2022

#   All Variables

progress = 0
progress_module_trailer = 0
do_not_progress_module_retriever = 0
exclude = 0
progress_list = []
trailer_list = []
excluded_list = []
retriever_list = []

f = open("file.txt", "a")
f.truncate(0)
f.close()

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
    total = pass_credits_int + defer_credits_int + fail_credits_int
# Conditions
    if total != 120:
        print("Total incorrect")
    elif pass_credits_int == 120:
        print("\nYour progression outcome :Progress")
        progress_list.append([pass_credits_int, defer_credits_int, fail_credits_int])
        progress += 1
    elif pass_credits_int == 100:
        print("\nYour progression outcome :Progress (module trailer)")
        trailer_list.append([pass_credits_int, defer_credits_int, fail_credits_int])
        progress_module_trailer += 1
    elif pass_credits_int == 80 or pass_credits_int == 60:
        print("\nYour progression outcome :Do not Progress – module retriever")
        retriever_list.append([pass_credits_int, defer_credits_int, fail_credits_int])
        do_not_progress_module_retriever += 1
    elif pass_credits_int == 40 and 20 <= defer_credits_int <= 80:
        print("\nYour progression outcome :Do not Progress – module retriever ")
        retriever_list.append([pass_credits_int, defer_credits_int, fail_credits_int])
        do_not_progress_module_retriever += 1
    elif pass_credits_int == 40 and defer_credits_int == 0:
        print("\nYour progression outcome :Exclude ")
        excluded_list.append([pass_credits_int, defer_credits_int, fail_credits_int])
        exclude += 1
    elif pass_credits_int == 20 and 40 <= defer_credits_int <= 100:
        print("\nYour progression outcome :Do not Progress – module retriever ")
        retriever_list.append([pass_credits_int, defer_credits_int, fail_credits_int])
        do_not_progress_module_retriever += 1
    elif pass_credits_int == 20 and 0 <= defer_credits_int <= 20:
        print("\nYour progression outcome :Exclude ")
        excluded_list.append([pass_credits_int, defer_credits_int, fail_credits_int])
        exclude += 1
    elif pass_credits_int == 0 and 60 <= defer_credits_int <= 120:
        print("\nYour progression outcome :Do not Progress – module retriever ")
        retriever_list.append([pass_credits_int, defer_credits_int, fail_credits_int])
        do_not_progress_module_retriever += 1
    elif pass_credits_int == 0 and 0 <= defer_credits_int <= 40:
        print("\nYour progression outcome :Exclude ")
        excluded_list.append([pass_credits_int, defer_credits_int, fail_credits_int])
        exclude += 1

    total_outcomes = progress + progress_module_trailer + do_not_progress_module_retriever + exclude
# Repetition for another set of inputs
    done = True
    while done:
        print("\nWould you like to enter another set of data?")
        while True:
            try:
                run_again = input("Enter 'y' for yes or 'q' to quit and view results: ")

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
                    break
                # If user input char values like space then this program works
            except:
                print("\t", "*" * 5, "User input is incorrect", "*" * 5, "\n")


# Histogram
def histogram():
    print("\n")
    print("-"*75)
    print("Histogram")
    print("Progress  ", progress, ":", "*" * progress)
    print("Trailer   ", progress_module_trailer, ":", "*" * progress_module_trailer)
    print("Retriever ", do_not_progress_module_retriever, ":", "*" * do_not_progress_module_retriever)
    print("Exclude   ", exclude, ":", "*" * exclude)
    print("-"*75)
    print(total_outcomes, " outcome(s) in total")


histogram()
# Part 2 and Part 3
print("-"*75)
print("Part 2: ")
for x in progress_list:
    string = str(x)
    string = string[1:-1]
    p = "Progress - " + string
    print("Progress - ", string)
    f = open("file.txt", "a")
    f.write("Progress - " + string + '\n')
    f.close()

for x in trailer_list:
    string = str(x)
    string = string[1:-1]
    t = "Progress (module trailer) - " + string
    print("Progress (module trailer) - " + string)
    f = open("file.txt", "a")
    f.write("Progress (module trailer) - " + string + '\n')
    f.close()

for x in excluded_list:
    string = str(x)
    string = string[1:-1]
    e = "Exclude – " + string
    print("Exclude – ", string)
    f = open("file.txt", "a")
    f.write("Exclude – " + string + '\n')
    f.close()

for x in retriever_list:
    string = str(x)
    string = string[1:-1]
    r = "Module retriever - " + string
    print("Module retriever - ", string)
    f = open("file.txt", "a")
    f.write("Module retriever - " + string + '\n')
    f.close()

print("")
print("-" * 75)
print("Part 3")
f = open('file.txt', 'r')
content = f.read()
print(content)
f.close()