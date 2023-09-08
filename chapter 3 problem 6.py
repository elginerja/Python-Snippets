month = int(input('Enter the month from 1 thru 12: '))
day = int(input('Enter the day from 1 thru 31: '))
year = int(input('Enter the last two digets of the year: '))

message = '\n' + format(month) + '/'  + format(day) + '/'  + format(year) +  ' IS '

if ((month * day) != year):
    message += "NOT "
    
message += "magic."
print(message)