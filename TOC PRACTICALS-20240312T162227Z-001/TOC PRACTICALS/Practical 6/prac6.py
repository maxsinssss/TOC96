def stateQ0(n):
    print("Q0 ->",end = " ")
    if(len(n) == 0):
        print("\n ***String Accepted***")
    else:
        if(n[0] == '0'):
            print("input 0 " ,end = "")
            stateQ0(n[1:])
        elif(n[0] == '1'):
            print("input 1 " ,end = "")
            stateQ1(n[1:])

def stateQ1(n):
    print("Q1 ->",end = " ")
    if(len(n) == 0):
        print("\n ***String Not Accepted***")
    else:
        if(n[0] == '0'):
            print("input 0 " ,end = "")
            stateQ0(n[1:])
        elif(n[0] == '1'):
            print("input 1 " ,end = "")
            stateQ1(n[1:])

n = int(input("Enter a Decimal Number : "));
n = bin(n).replace("0b","")
stateQ0(n)


