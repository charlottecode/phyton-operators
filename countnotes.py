amount=int(input("enter the amount"))

note1=amount//500
print("500",note1)

note2=amount%500//100
print("100",note2)

note3=amount%500%100//50
print("50",note3)
