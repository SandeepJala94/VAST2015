import xlrd
import numpy as np

from bokeh.plotting import figure

def getAllData():
    fri, sat, sun = build_3_Day_Data()
    #fri = build_3_Day_Data()

    #friNumToDateDict, satNumToDateDict, sunNumToDateDict = buildNumToDateDicts()

    return fri, sat, sun#, friNumToDateDict, satNumToDateDict, sunNumToDateDict


def buildDict(dayData):
    v = []

    for r in range(1, dayData.nrows):
        v.append(dayData.cell_value(r, 0))

    return v


def build_3_Day_Data():
    file_location = "MC1 Data June 2015 V3/park-movement-Fri-FIXED-2.xlsx"
    print("Opening fridayFile")
    fridayFile = xlrd.open_workbook(file_location)
    print("Done opening fridayFile")
    fri = fridayFile.sheet_by_index(0)
    print("Done with fri")
    print()

    file_location = "MC1 Data June 2015 V3/park-movement-Sat.xlsx"
    print("Opening saturdayFile")
    saturdayFile = xlrd.open_workbook(file_location)
    print("Done opening saturdayFile")
    sat = saturdayFile.sheet_by_index(0)
    print("Done with sat")
    print()

    file_location = "MC1 Data June 2015 V3/park-movement-Sun.xlsx"
    print("Opening sundayFile")
    sundayFile = xlrd.open_workbook(file_location)
    print("Done opening sundayFile")
    sun = sundayFile.sheet_by_index(0)
    print("Done with sun")
    print()

    return fri, sat, sun


def buildNumToDateDict():
    locations = ["MC1 Data June 2015 V3/park-movement-Fri-FIXED-2.xlsx", "MC1 Data June 2015 V3/park-movement-Sat.xlsx", "MC1 Data June 2015 V3/park-movement-Sun.xlsx"]
    allDicts = []
    for file_location in location:
        dayFile = xlrd.open_workbook(file_location)
        dayFileDateMode = dayFile.datemode
        numToDateDict = {}

        for r in range(1, dayFile.nrows):
            numToDateDict[dayFile.cell_value(r, 0)] = datetime.datetime(xlrd.xldate_as_tuple(dayFile.cell_value(r, 0), dayFileDateMode))

        allDicts.append(numToDateDict)

    return allDicts[0], allDicts[1], allDicts[2]


def createDict(currentDayData):
    currentDayTimeIDMap = {}
    listOfTimes = []

    for i in range(1, currentDayData.nrows):
        currentTime = currentDayData.cell_value(i, 0)
        currentID = currentDayData.cell_value(i, 1)
        currentAction = currentDayData.cell_value(i, 2)
        currentLocation = (currentDayData.cell_value(i, 3), currentDayData.cell_value(i, 4))

        if currentTime not in currentDayTimeIDMap.keys():
            currentDayTimeIDMap[currentTime] = {currentID:[currentAction, currentLocation]}
            listOfTimes.append(str(currentTime))
        else:
            if currentID not in currentDayTimeIDMap[currentTime].keys():
                currentDayTimeIDMap[currentTime][currentID] = [currentAction, currentLocation]
            else:
                for i in range(0, 100):
                    print("ERROR")
                    i = i-1

    return currentDayTimeIDMap, listOfTimes


def createPark(currentDay, currentDayTimeIDMap, currentDayTimes, currentDayTime):
    p = figure(x_range=(0, 100), y_range=(0, 100), title="Park on "+currentDay+" at time "+str(currentDayTime))

    print("currentDayTime = ", currentDayTime)
    print("currentDayTimeIDMap[currentDayTime] = ", currentDayTimeIDMap[currentDayTime])
    print()

    for currentID in currentDayTimeIDMap[currentDayTime]:
        print("currentDayTime = ", currentDayTime)
        print("x=", currentDayTimeIDMap[currentDayTime][currentID][1][0], " y=",currentDayTimeIDMap[currentDayTime][currentID][1][1])
        p.circle(currentDayTimeIDMap[currentDayTime][currentID][1][0], currentDayTimeIDMap[currentDayTime][currentID][1][1], size=10, line_color="green", fill_color="green", fill_alpha=0.5)
    print()

    return p
