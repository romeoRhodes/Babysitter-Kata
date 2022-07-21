
import re

# Needs validation for Input
# Checks and Balances for Start Times, End Times, and Bed Time

class BabySitter:
    def __init__( self, start, stop, bedtime ):
        self.start = start
        self.stop = stop
        self.bedtime = bedtime
        self.status = True
        self.validate()
        self.militaryTime()
        self.timeCheck()
        self.hours = self.hoursWorked()
        self.calcPay()

    def validate( self ):
        time = [ self.start, self.stop, self.bedtime]
        for i in time:
            i = re.sub("AM","",i)
            i = re.sub("PM","",i)
            i = re.sub(":","",i)
            if re.search("[a-z]",i):
                print("Invalid Input Found, Use Format ex:'8:00PM' ")
                self.status = False
            else:
                pass

    def militaryTime( self ):
        self.start = timeConvert(self.start)
        self.stop = timeConvert(self.stop)
        self.bedtime = timeConvert(self.bedtime)

    def timeCheck( self ):
        if self.start < 17:
            print("Unable to Process, Arrival Time is Earlier than Allowed")
            self.status = False

        if self.stop > 4:
            print("Unable to Process, Departure Time is Later than Allowed")
            self.status = False

    def hoursWorked(self):
        if self.start > self.stop:
            return self.start - self.stop
        elif self.start < self.stop:
            return self.stop - self.start

    def calcPay(self):
        if self.status == True:
            a = (max(self.start,self.bedtime) - min(self.start,self.bedtime)) * 12
            b = (max(self.bedtime,24) - min(self.bedtime,24)) * 8
            c = (max(self.stop,24) - min(self.stop,24)) * 16 if self.stop > 12 else self.stop * 16
            pay = float(a + b + c)
            print(pay)
        


def timeConvert( time ):
    if time[-2:] == "AM":
        arr = re.split(":", time)
        time = arr[0]
        if int(time) == 12:
            time = int(time)+12
            return time
        elif int(time) < 12 and time > 9:
            return int(time)
        else:
            time = "0" + time
            return int(time)
    elif time[-2:] == "PM" and re.search("[0-9:]",time[:2]):
        arr = re.split(":", time)
        time = arr[0]
        if time == 12:
            return int(time)
        else:
            time = int(time) + 12
            return time
    else:
        print("You Entered an Incorrect Time Format")




emp1 = BabySitter("5:00PM","4:00AM","10:00PM")

emp2 = BabySitter("6:00PM", "2:00AM", "8:00PM")

emp3 = BabySitter("5:00PM", "4:o0AM", "9:00PM") # Wrong Input Example

emp4 = BabySitter("4:00PM", "4:00AM", "7:00PM") # Early Arrival Example 

emp5 = BabySitter("5:00PM", "6:00AM", "9:00PM") # Late Departure Example