# Create a list of at least 5 states (take inputs from user) with capital, population,area. e.g.
# [[“UP”,”Luckcnow”,128922200,1234],[“HP”,”Shimla”,6812638,182368]]
# a. Display all states and its’ capital.
# b. Average population of all states.
# c. State with maximum covered area.
# d. State with highest population density (Note: population density-
# >>>population/area)
l=[]
l1=[]

n=int(input("Enter the number of states\n"))

for i in range(0,n):
    print("Enter the name of the state")
    l1.append(str(input()))

    print("Enter the name of the capital")
    l1.append(str(input()))

    print("Enter the population")
    l1.append(input())

    print("Enter the area")

    l1.append(input())
    l.append(l1)
    l1=[]

print("State\tCapital")

for i in range(0,n):
    print("%s\t%s"%(l[i][0],l[i][1]))