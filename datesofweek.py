import datetime

date_1 = datetime.datetime.now()
date_2 = datetime.date(2021, 8, 1)
print("today is", date_2)
print('\n')

week_date = date_2.weekday()
cal = []
#print(week_date)

#print( date_1 )
#print(date_1.month)

for i in range (5):
  #if week_date == 5:  ##if today is not sunday, so try on monady? 
    #print ('\n')  
  #if date_1.month !=  date_1.month:
   # print ('\n')   
  #else:   
  #  print (date_2 + datetime.timedelta(days=i*7), ",", date_2 + datetime.timedelta(days=i*7 + 1), ",", date_2 + datetime.timedelta(days=i*7 + 2), "," ,date_2 + datetime.timedelta(days=i*7 + 3), "," ,date_2 + datetime.timedelta(days=i*7 + 4), "," ,date_2 + datetime.timedelta(days=i*7 + 5))
   
    cal.append(date_2 + datetime.timedelta(days=i*7))
    cal.append(date_2 + datetime.timedelta(days=i*7 + 1))
    cal.append(date_2 + datetime.timedelta(days=i*7 + 2))
    cal.append(date_2 + datetime.timedelta(days=i*7 + 3))
    cal.append(date_2 + datetime.timedelta(days=i*7 + 4))
    cal.append(date_2 + datetime.timedelta(days=i*7 + 5))
    cal.append(date_2 + datetime.timedelta(days=i*7 + 6))
print ("--------------------------------------" ) 
#print(cal)
bad_dates = 0
for date in cal:
    if date.month != int(cal[1].month):
        bad_dates += 1
print ("--------------------------------------" )         
#print(bad_dates) 

for i in range(bad_dates):
       del cal[-1] 
#print(cal)
#string = ""
#string = cal
#print(string)
cal2 = []
for date in cal:
    #print(date)
    a = date.weekday()
    #print(type(a))
    if int(a) == 5:
        cal2.append(date)
        cal2.append('\n')
    if int(a) == 6:
      cal2.append(date)

print(cal2)  

cal3 = ",".join([str(item) for item in cal2])
print(cal3)

thismonth = date.month
print(thismonth)
if thismonth == 8:
  thismonthword = "August"
elif thismonth == 9:
  thismonthword = "September"
elif thismonth == 10:
  thismonthword = "October"
elif thismonth == 11:
  thismonthword = "November"
elif thismonth == 12:
  thismonthword = "December"
elif thismonth == 1:
  thismonthword = "January"
elif thismonth == 2:
  thismonthword = "February"
elif thismonth == 3:
  thismonthword = "March"
elif thismonth == 4:
  thismonthword = "April"
elif thismonth == 5:
  thismonthword = "May"
elif thismonth == 6:
  thismonthword = "June"
else:
  thismonthword = "July"

#print(thismonthword)
headerstring = ",".join([thismonthword,"Sunday", "Saturday", "\n"])
print(headerstring)

f = open("nirdates.csv", "w")
f.write(headerstring)
f.write(",")
f.write(cal3)  
f.close()
  