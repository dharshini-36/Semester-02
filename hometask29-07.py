#1
try:
    string=input("Enter a string: ") 
    substring=input("Enter a substring: ")
    position=string.index(substring)
    print(f"The position of the substring: {position}")
except ValueError:
    print("Substring was not found")


#2
grades=[]
try:
    average=sum(grades)/len(grades)
    print(average)
except ZeroDivisionError:
    print("List can't be empty")
#or
try:
    grades=input("Enter grades: ")
    grades=[int(grade) for grade  in grades.split()]
    average=sum(grades)/len(grades)
    print(average)
except ZeroDivisionError:
    print("List can't be empty")


#3
try:
    txt="Be your own Sunshine"
    print(txt[20])
except IndexError:
    print("Please enter a valid index")
