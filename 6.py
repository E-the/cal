sub1=float(input("Enter marks of the first subject: "))
sub2=float(input("Enter marks of the second subject: "))
sub3=float(input("Enter marks of the third subject: "))
sub4=float(input("Enter marks of the fourth subject: "))
total=sub1+sub2+sub3+sub4
avg=total/4
percentage=(total/400)*100
if avg>=90 and avg<=100:
    print("Grade: A")
elif avg>=80 and avg<90:
    print("Grade: B")
elif avg>=70 and avg<80:
    print("Grade: C")
elif avg>=60 and avg<70:
    print("Grade: D")
else:
    print("Grade: F")