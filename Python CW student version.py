# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# My student ID - w1953234
# Date - 12/14/2022

# Range function
def credit_range(credit):
    check = False
    for i in range (0,130,+20): #Range of Credits
        if(credit==i):
            check = True
            break
    return check
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
elif pass_credits_int == 100:
    print("\nYour progression outcome :Progress (module trailer)")
elif pass_credits_int == 80 or pass_credits_int == 60:
    print("\nYour progression outcome :Do not Progress – module retriever")
elif pass_credits_int == 40 and 20 <= defer_credits_int <= 80:
    print("\nYour progression outcome :Do not Progress – module retriever ")
elif pass_credits_int == 40 and defer_credits_int == 0:
    print("\nYour progression outcome :Exclude ")
elif pass_credits_int == 20 and 40 <= defer_credits_int <= 100:
    print("\nYour progression outcome :Do not Progress – module retriever ")
elif pass_credits_int == 20 and 0 <= defer_credits_int <= 20:
    print("\nYour progression outcome :Exclude ")
elif pass_credits_int == 0 and 60 <= defer_credits_int <= 120:
    print("\nYour progression outcome :Do not Progress – module retriever ")
elif pass_credits_int == 0 and 0 <= defer_credits_int <= 40:
    print("\nYour progression outcome :Exclude ")
