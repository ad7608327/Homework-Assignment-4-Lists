myUniqueList = []
def Alist1 (A,B,C,D,E):
  myUniqueList.append(A)
  myUniqueList.append(B)
  myUniqueList.append(C)
  myUniqueList.append(D)
  myUniqueList.append(E)
  return A,B,C,D,E
A0=input("Enter Element [0] > ")
A1=input("Enter Element [1] > ")
A2=input("Enter Element [2] > ")
A3=input("Enter Element [3] > ")
A4=input("Enter Element [4] > ")
Alist1(A0,A1,A2,A3,A4)
print(f"This is Content of the list {myUniqueList}")
print("<=========================================>")
myLeftovers = []
zz=input("Do you Want to Add More Elements? > ")
if zz == "yes" or zz == "Yes" or zz == "YES":
    B0=input("Enter Element [0] > ")
    B1=input("Enter Element [1] > ")
    B2=input("Enter Element [2] > ")
    B3=input("Enter Element [3] > ")
    B4=input("Enter Element [4] > ")
    if A0 == B0 or A1 == B1 or A2 == B2 or A3 == B3 or A4 == B4 :
        print("Erorr")
        print("<=========================================>")
        AA = input("Do you Want to Move New Elements to myLeftovers ? > ")
        if AA == "yes" or AA == "Yes" or AA == "YES":
            myLeftovers = []
            def Alist1 (A,B,C,D,E):
              myLeftovers.append(A)
              myLeftovers.append(B)
              myLeftovers.append(C)
              myLeftovers.append(D)
              myLeftovers.append(E)
              print(myLeftovers)
              print("<=========================================>")
              print("Thanks For Playing With My Script :)\n")
              exit()
        elif AA == "no" or AA == "No" or AA == "NO":
            print("<=========================================>")
            print("Thanks For Playing With My Script :)\n")
            exit()
    print(myUniqueList)


elif zz =="no" or "No" or "NO":
    print("<=========================================>")
    print("Thanks For Playing With My Script :)\n")
    exit()
