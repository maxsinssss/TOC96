def stateQ0(inputStr):
    print("Q0->",end=" ")
    if(len(inputStr) <= 1):
        print("String rejected")
    elif(inputStr[0] == "1"):
        stateQ1(inputStr[1:])
    elif(inputStr[0] == "0"):
        stateQ0(inputStr[1:])

def stateQ1(inputStr):
    print("Q1->",end=" ")
    if(len(inputStr) <= 1):
        print("String rejected")
    elif(inputStr[0] == "0"):
        stateQ0(inputStr[1:])
    elif(inputStr[0] == "1"):
        stateQ2(inputStr[1:])

def stateQ2(inputStr):
    print("Q2->",end=" ")
    if(len(inputStr) <= 0):
        print("String rejected")
    elif(inputStr[0] == "1"):
        stateQ3(inputStr[1:])
    elif(inputStr[0] == "0"):
        if(len(inputStr) < 2):
            print("String Rejected")
        else:
            stateQ0(inputStr[1:])

def stateQ3(inputStr):
    print("Q3->",end=" ")
    if(len(inputStr) <= 0):
        print("String Accepted")
    elif(inputStr[0] == "1"):
        stateQ3(inputStr[1:])
    elif(inputStr[0] == "0"):
        print("Q3 ->", end=" ")
        stateQ3(inputStr[1:])

inputStr = input("Enter a string of 1 and 0: ")
lenstr = len(inputStr)
print(lenstr)

if lenstr < 3:
    print("Enter a String of Atleast 3 Numbers: ")
elif(inputStr == "111"):
    print("Q0 -> Q1 -> Q2 -> Q3")
    print("String Accepted")
else:
    stateQ0(inputStr)
