import random
import datetime
import csv

currhour = datetime.datetime.now()
#now_H = currhour.hour #commented out for testing purposes
#now_H stores the current hour
#now_M = currhour.minute #commented out for testing purposes
#now_M stores the current minute, currently not used
#now_M = random.randint(0,59) #testing purposes
#now_H = random.randint(0,24) #testing purposes
i = 0

def hourMult(hr,mi):
        #Takes time and determines multiplier
        if (hr >= 0 and hr <= 6):
                return (30,'A',7)
        elif (hr > 6 and hr <= 8):
                return (200,'B',2)
        elif (hr > 8 and hr <= 16):
                return (275,'C',8)
        elif (hr > 16 and hr <= 22):
                return (350,'D',6)
        elif (hr > 22 and hr < 24):
                return (100,'E',1)
        else:
                return (215,'F',1)

def timeCheck(multtC):
        #Takes input of multiplier (multtC) and spits out lower/uper values
        #r1 is number randomly generated based upon multtC --> lower value
        #r2 = r1 + multtC --> upper value
        #multtC is input from output of hourMult(hr,mi)
        #Returns r1,r2 in a tuple
        r1 = random.randint(0,(1000-multtC[0]))
        r2 = r1 + multtC[0]
        return (r1,r2)

def lightsOn(inTuple,lO):
        #Compares input from timeCheck tuple and determines whether lights off or on
        #using r1, r2 from timeCheck(multtC), determines if the 
        #1 == Lights On
        #0 == Lights Off
        if (lO >= inTuple[0] and lO <= inTuple[1]):
                return ("Lights On",1)
                #print currhour.hour, currhour.minute
        else:
                return ("Lights Off",0)
                #print currhour.hour, currhour.minute

#def likelihoodOn()
        
def csvwriter(fileN,text):
        with open(fileN, 'ab') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=';')
                filewriter.writerow([text])


def testingResults():
        #Spits out numerical string of results for feedback
        now_H = random.randint(0,24)
        now_M = random.randint(0,59)
        mult = hourMult(now_H, now_M)
        multPerc = mult[0]*.001
        tc = timeCheck(mult)
        lights = lightsOn(tc,mult[0])
        #r1;r2;mult;mult%;multHours;Hour;Minute;Lights On?
        return str(tc[0])+";"+str(tc[1])+";"+str(mult[0])+";"+str(multPerc)+";"+str(mult[2])+";"+str(now_H)+";"+str(now_M)+";"+str(lights[1])
        
def manyIterations():
        mIi = 0
        while (mIi != 10):
                testString = str(testingResults())
                csvwriter('teststat.csv',testString)
                print mIi
                mIi = mIi + 1


manyIterations()
