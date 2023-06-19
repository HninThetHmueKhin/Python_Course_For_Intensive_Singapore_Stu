from datetime import date

year1 = int(input("Enter the year(yyyy) for the first date: "))
month1 = int(input("Enter the month(mm) for the first date: "))
day1 = int(input("Enter the day(dd) for the first date: "))

year2 = int(input("Enter the year(yyyy) for the second date: "))
month2 = int(input("Enter the month(mm) for the second date: "))
day2 = int(input("Enter the day(dd) for the second date: "))

date1 = date(year1,month1,day1)
date2 = date(year2,month2,day2)

no_of_days = date2 -date1
days = no_of_days.days

print("The number of days between the two dates is: ",days)




