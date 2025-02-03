#FutureTime.py
#Name: Alex Hernandez Lopez
#Date: 2/2/25
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("Enter number of hours: ")
  #Ask user for minutes
  moreMins = input("Enter number of minutes: ")
  #Calculate the time after the user-supplied time has passed.
  futureMins = (currentMinute + int(moreMins)) % 60
  extraHour = (currentMinute + int(moreMins)) // 60
  futureTime = (currentHour + int(hours) + extraHour) % 24
  print(futureTime)
  print(futureMins)
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
