#!/usr/bin/env python3

import pandas as pd
import matplotlib.pylab as chart
from collections import Counter


#Ask user for data filename
fn=input("What is the name of the viewing data file you'd like to analyze? (Please use name.csv format) \n")

#Read file
data=pd.read_csv(fn)

###########################

#Function for total time watched for one show
def watchtime(file):
    
    #Convert "Start time" to date time

    file["Start Time"] = pd.to_datetime(file['Start Time'], utc=True)

    file = file.set_index("Start Time")

    #Convert datetime to US/Eastern time

    file.index = file.index.tz_convert("US/Eastern")

    file = file.reset_index() 

    #Convert Duration to timedelta

    file["Duration"]= pd.to_timedelta(file["Duration"])

    #Ask user for the show they'd like to use

    sn=input("What is the full name of the show you'd like to analyze?\n")

    #Find the show name in the csv file

    show = file[file["Title"].str.contains(sn,regex=False)]

    #Get rid of short view times which were added to the data from watching previews

    show=show[(show["Duration"]>"0 days 00:01:00")]

    #Get final sum of total time watched

    totaltime=show["Duration"].sum()

    print("You have watched "+sn+" for a total of "+str(totaltime)+ " (hours, minutes, seconds).\n\n")
    
###########################

#Function for number of tv episodes/movies watched by device type
def device_type(file):
    
    #Find number of episodes/movies watched by device type
    shows=dict(Counter(file["Device Type"]))
    
    #Plot data
    keys = shows.keys()
    values = shows.values()
    chart.bar(keys,values)
    chart.xlabel("Device Type")
    chart.ylabel("# of episodes/movies watched")
    chart.show()
    
###########################
    
#Function for number of tv episodes/movies watched by profile name
def profiles(file):
    
    #Find number of episodes/movies watched by profile
    shows=dict(Counter(file["Profile Name"]))
    
    #Plot data
    keys = shows.keys()
    values = shows.values()
    chart.bar(keys,values)
    chart.xlabel("Profile Name")
    chart.ylabel("# of episodes/movies watched")
    chart.show()
    
###########################
    
#User selection loop
end=1
while (end!=0):
    
    output=int(input("Would you like to find the total time you've watched a single show (1), the number of tv episodes/movies watched by device type (2), or the number of tv episodes/movies watched by profile (3)\n"))
    
    if output==1:
        watchtime(data)
    if output==2:
        device_type(data)
    if output==3:
        profiles(data)
    
    #Loop exit
    end=int(input("Would you like to perform another analyis (1 for yes, 0 for no)\n"))

        
    





