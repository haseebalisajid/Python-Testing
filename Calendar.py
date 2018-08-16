import calendar
def per_month():
    year=int(input("Enter Year:"))
    month=int(input("Enter Month(integer):"))
    return calendar.month(year,month)
def Whole_calendar():
    year=int(input("Enter Year:"))
    return calendar.calendar(year,2,1,10)
q=input("Do you want to see year or a month Calendar(Y/M):")
if q=="m":
    print(per_month())
elif q=="y":
    print(Whole_calendar())
else:
    print("Good bye")

