def stateQ0(n,countzero,countone):
    print("Q0 ->",end = " ")
    if(len(n) == 0 ):
        if(len(countzero) == len(countone)):
            print("\n ***String Accepted***")
            print("String having equal no. of 1's and 0's")
        else:
            print("\n ***String Rejected***")
    else:
        if(n[0] == "0"):
            countzero.append("0")
            stateQ0(n[1:],countzero,countone)
        elif(n[0] == "1"):
            countone.append("1")
            stateQ1(n[1:],countzero,countone)

def stateQ1(n,countzero,countone):
    print("Q1 ->",end = " ")
    if(len(n) == 0 ):
        if(len(countzero) == len(countone)):
            print("\n ***String Accepted***")
            print("\n String having equal no. of 1's and 0's")
        else:
            print("\n ***String Rejected***")
    else:
        if(n[0] == "0"):
            countzero.append("0")
            stateQ0(n[1:],countzero,countone)
        elif(n[0] == "1"):
            countone.append("1")
            stateQ1(n[1:],countzero,countone)

countzero = []
countone = []
n = input("Enter 0 and 1 sequence: ")
print("Transition State: ")
stateQ0(n,countzero,countone)
            