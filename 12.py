import math

class3=int(input("number of students in class3:"))
class4=int(input("number of students in class4:"))
class5=int(input("number of students in class5:"))

totaldesk1=math.ceil(class3/2)
totaldesk2=math.ceil(class4/2)
totaldesk3=math.ceil(class5/2)

totaldesk=int(totaldesk1+totaldesk2+totaldesk3)

print(f"class 3 need {totaldesk1} desk")
print(f"class 4 need {totaldesk2} desk")
print(f"class 5 need {totaldesk3} desk")