##########################################################
### IoT Timer Using Random Numbers and Lifecycle Stats ###
### Justin Weiler - Started 3/8/2020                   ###
##########################################################

import random
import datetime
import csv

currhour = datetime.datetime.now()
#now_H = currhour.hour #Stores the current hour
#now_M = currhour.minute #Stores the current minute, currently not used

i = 0

def csvWriter(fileN,text):
        #Writes lines of return to .csv for testing and stats purposes
        #Used for testing and for logging
        with open(fileN, 'ab') as csvfile: #Appends lines using 'ab' flags
                filewriter = csv.writer(csvfile, delimiter=';')
                filewriter.writerow([text])

def logFileNaming(baseFileName):
        #Gives log file appropriate naming based upon date
        #Assumes baseFileName has filetype suffix (.csv) already
        return str(currhour.year) + "_" + str(currhour.month) + "_" + str(currhour.day) + "-" + str(baseFileName)

def hourMult(hr,mi):
        #Takes time and determines multiplier
        #returns tuple with mult, ID, #hours
        #Updated to find accurate multipliers for realistic hourly activity
        if (hr == 24 or (hr >= 0 and hr <= 6)): #00:00 - 05:59
                return (30,'A',7,0,6)
        elif (hr > 6 and hr <= 8): #06:00 - 07:59
                return (200,'B',2,6,8)
        elif (hr > 8 and hr <= 16): #08:00 - 15:59
                return (275,'C',8,8,16)
        elif (hr > 16 and hr <= 22): #16:00 - 21:59
                return (350,'D',6,16,22)
        elif (hr > 22 and hr < 24): #22:00 - 23:59
                return (100,'E',1,22,24)
        else:
                return (215,'F',1,25,25) #Catches edge case, replace with error catching/exception handling

def timeCheck(multtC):
        #Takes input of multiplier (multtC) and spits out lower/uper values
        r1 = random.randint(0,(1000-multtC[0])) #Generates random starting value <= (1000 - multtC) --> r1 is lower value
        r2 = r1 + multtC[0] #Calculates r2 to determine --> r2 is higher value
        return (r1,r2) #Returns r1,r2 in a tuple

def lightsOn(inTuple,lO):
        #Compares input from timeCheck tuple and determines whether lights off or on
        #using r1, r2 from timeCheck(multtC)
        if (lO >= inTuple[0] and lO <= inTuple[1]): #Determines whether lO is within r1, r2 range
                return ("Lights On",1) #If so, lights on
        else:
                return ("Lights Off",0) #If not, lights off

def lightsOps():
        #Will take the data from the other modules and operate the lights
        opsMult = hourMult(currhour.hour, currhour.minute) #Gets applicable mult to current hour:minute
        opsMultPerc = opsMult[0]*.001 #Stores mult as a % for statistic analysis purposes
        opsTC = timeCheck(opsMult) #Calls timeCheck(mult) to get randomly generated (r1, r2) values returned as tuple
        opsLights = lightsOn(opsTC,opsMult[0]) #Determines if the lights are to be on or off
        #r1;r2;mult;mult%;multHours;multBeginHour;multEndHour;Hour;Minute;LightsOn? --> Log Format
        opsLogs = str(opsTC[0])+";"+str(opsTC[1])+";"+str(opsMult[0])+";"+str(opsMultPerc)+";"+str(opsMult[2])+";"+str(opsMult[3])+";"+str(opsMult[4])+";"+str(currhour.hour)+";"+str(currhour.minute)+";"+str(opsLights[1])
        csvWriter('RandomPyLogs.csv',opsLogs)
        return opsLights[1] #Yes or No for lights being on

##############################
##### TESTING AREA BELOW #####
##############################

#def likelihoodOn()
#An idea for a method which will tell how often Lights On happens compared to
#how likely that should happen.

def testingResults():
        #Used for testing purposes only
        #Spits out numerical string of results for feedback
        #r1;r2;mult;mult%;multHours;multBeginHour;multEndHour;Hour;Minute;LightsOn?
        now_H_test = random.randint(0,24) #Randomly generates hour for testing
        now_M_test = random.randint(0,59) #Randomly generates minute for testing
        mult = hourMult(now_H_test, now_M_test) #Calls hourMult(hr,mi) to get applicable mult
        multPerc = mult[0]*.001 #Stores mult as a % for statistic analysis purposes
        tc = timeCheck(mult) #Calls timeCheck(mult) to get randomly generated (r1, r2) values returned as tuple
        lights = lightsOn(tc,mult[0]) #Determines if the lights are on in each scenario
        return str(tc[0])+";"+str(tc[1])+";"+str(mult[0])+";"+str(multPerc)+";"+str(mult[2])+";"+str(mult[3])+";"+str(mult[4])+";"+str(now_H_test)+";"+str(now_M_test)+";"+str(lights[1])
        
def manyIterations():
        #Used for testing purposes only
        #Generates test run data for statistical analysis
        mIi = 0 #Initializes counter at 0
        iterNum = 1400000 #Number of results to be gained through testing
        while (mIi != iterNum):
                testString = str(testingResults()) #Stores testingResults() return as a string for print to teststat.csv
                csvWriter('teststat.csv',testString) #Write testString to teststat.csv
                print mIi #Counter for on-screen real time status
                mIi = mIi + 1 #Increments counter for while loop

##############################
#####  END TESTING AREA  #####
##############################

manyIterations() #Used for testing purposes only
