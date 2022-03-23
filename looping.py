# list1 = [["M12",1],["Mrm",2],
# ["carry",2],["ziktor",1],["abhi",0]]
# dict1 = dict(list1)

# for item in dict1: 
#     print(dict1)

    
list1 = [ ["Harry",1 ], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]
dict1 = dict(list1)

# for item in dict1:
    # print(item)
for item, lollypop in dict1.items():
    print(item, "and lolly is ", lollypop)
# items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

# for item in items:
#     if str(item).isnumeric() and item>=6:
#         print(item)


# l =["m12",int,float,8,90,0,9,46,56,77,68,87,97,45]
# for a in l:
#     if (str(a).isnumeric() and a>6):
#         print(a)



# l = []
# while(1):
#     a = int(input("Enter number : "))
#     try:
#         if a not in l and len(str(a)) == 1:
#             l.append(a)
#         else:
#             raise Exception
#     except:
#         print("Duplicates are not allowed and number should have 2 digits")
#         break        