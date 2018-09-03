'''
Design a program that asks the user to enter a number of seconds, and works as
follows:
  -  There are 60 seconds in a minutes. If the number of seconds entered by the
     user is greater than or equal to 60, the program should display the number
     of minutes in that many seconds.
  -  There are 3,600 seconds in an hour. If the number of seconds entered by
     the user is greater than or equal to 3,600, the program should display the
     number of hours in that many seconds.
  -  There are 86,400 seconds in a day. If the number of seconds entered by the
     user is greater than or equal to 86,400, the program should display the
     number of days in that many seconds.
'''
# Prompt
sec = int(input("Enter a number of seconds: "))

# Time Variables
min = sec / 60
hours = sec / 3600
days = sec / 86400

# Decision Structure
if 60 <= sec < 3600:
    print(min, "minute(s)")
elif 3600 <= sec < 86400:
    print(hours, "hour(s)")
elif sec >= 86400:
    print(days, "day(s)")