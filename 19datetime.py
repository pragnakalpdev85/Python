import datetime

#get date and time 
datetime1 = datetime.datetime.now()
print(datetime1)

#printing out the day, month, year, hour from datetime object
print("day :",datetime1.day)
print("month :",datetime1.month)
print("year :",datetime1.year)
print("hour :",datetime1.hour)
print("minutes :",datetime1.minute)
print("second :",datetime1.second)

#creating date object
datetime2 = datetime.datetime(2000,2,21)
print(datetime2)

#strftime's different format codes
print("weekday in short: ",datetime1.strftime("%a")) #short weekday
print("Full weekday: ",datetime1.strftime("%A")) #full weekday
print("month in short: ",datetime1.strftime("%b")) #short month 
print("full month: ",datetime1.strftime("%B")) #full month 
print("weekday as number: ",datetime1.strftime("%w")) #weekday as a number between 0-6
print("day: ",datetime1.strftime("%d")) #day 
print("year in short form: ",datetime1.strftime("%y")) #year in short version
print("year in long form: ",datetime1.strftime("%Y")) #full year
print("Hour in 0-23 format: ",datetime1.strftime("%H")) #hour in 0-23 format
print("Hour in 0-12 format: ",datetime1.strftime("%l")) #hour in 0-12 format
print(datetime1.strftime("%p")) #am/pm
