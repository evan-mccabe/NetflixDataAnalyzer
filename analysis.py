#!/usr/bin/env python3

import pandas as pd

#Ask user for data filename
fn=input("What is the name of the viewing data file youd like to analyze? (Please use name.csv format) \n")

#Read file
data=pd.read_csv(fn)

#Convert "Start time" to date time

data["Start Time"] = pd.to_datetime(data['Start Time'], utc=True)

data = data.set_index("Start Time")

#Convert datetime to US/Eastern time

data.index = data.index.tz_convert("US/Eastern")

data = data.reset_index() 

#Convert Duration to timedelta

data["Duration"]= pd.to_timedelta(data["Duration"])

#Ask user for the show they'd like to use

sn=input("What is the full name of the show you'd like to analyze?\n")

#Find the show name in the csv file

show = data[data["Title"].str.contains(sn,regex=False)]

#Get rid of short view times which were added to the data from watching previews

show=show[(show["Duration"]>"0 days 00:01:00")]

#Get final sum of total time watched

totaltime=show["Duration"].sum()

print("You have watched "+sn+" for a total of "+str(totaltime)+ " (hours, minutes, seconds)")

