import functions as funcs

from bokeh.io import curdoc
from bokeh.layouts import widgetbox, row, column, layout
from bokeh.models import ColumnDataSource, Select, Button, Slider
from bokeh.palettes import Spectral6
from bokeh.io import output_notebook, show
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool
from bokeh.models import BoxZoomTool
from bokeh.models import WheelZoomTool
from bokeh.models import PanTool

fridayData, saturdayData, sundayData = funcs.getAllData()

fridayTimeIDMap, fridayTimes = funcs.createDict(fridayData)
saturdayTimeIDMap, saturdayTimes = funcs.createDict(saturdayData)
sundayTimeIDMap, sundayTimes = funcs.createDict(sundayData)


#for key in fridayTimeIDMap.keys():
#    print(key, " : ")
#    for ids in fridayTimeIDMap[key]:
#        print(ids, " : ", fridayTimeIDMap[key][ids])
#    print()


days = ["Friday", "Saturday", "Sunday"]
allDaysData = [fridayData, saturdayData, sundayData]
allDaysTimeIDMap = [fridayTimeIDMap, saturdayTimeIDMap, sundayTimeIDMap]
allDaysTimes = [fridayTimes, saturdayTimes, sundayTimes]


currentIndexForDays = 0
dayPassedToCreatePark = days[currentIndexForDays]
dayTimeIDMapPassedToCreatePark = allDaysTimeIDMap[currentIndexForDays]
dayTimesPassedToCreatePark = allDaysTimes[currentIndexForDays]


currentSecondIndex = 0
secondPassedToCreatePark = float(dayTimesPassedToCreatePark[currentSecondIndex])


parkMap = funcs.createPark(dayPassedToCreatePark, dayTimeIDMapPassedToCreatePark,
    dayTimesPassedToCreatePark, secondPassedToCreatePark)





#Selections and Sliders
day__select = Select(title = "Day",
                     value = "Friday",
                     width=200,
                     options = days)

time_select = Select(title = "Time",
                     value = dayTimesPassedToCreatePark[0],
                     width = 200,
                     options = dayTimesPassedToCreatePark)

scan_next_second_button = Button(label="Scan Next Second", button_type="success")
scan_prev_hour_button = Button(label="Scan Prev Second", button_type="success")




#Functionality og Selectors, Sliders, and Buttons
def updateDay():
    pass

def updateTime():
    pass

def goToNextSecond():
    currentSecondIndex = getCurrentSecondIndex()
    if currentSecondIndex < len(dayTimesPassedToCreatePark)-1:
        currentSecondIndex = currentSecondIndex+1
        setCurrentSecondIndex(currentSecondIndex)
        secondPassedToCreatePark = float(dayTimesPassedToCreatePark[currentSecondIndex])
        newParkMap = funcs.createPark(dayPassedToCreatePark, dayTimeIDMapPassedToCreatePark,
            dayTimesPassedToCreatePark, secondPassedToCreatePark)
        layout.children[1] = newParkMap
    else:
        print("GO TO THE NEXT DAY")


def goToNextSecondV2():
    print("type(time_select.options) = ", type(time_select.options))
    print("time_select.options[0] = ", time_select.options[0])
    print("time_select.value = ", time_select.value)
    print("Index of time_select.value in time_select.options is : ", time_select.options.indexOf(time_select.value))


    #else:
    #    newParkMap = createParkForNextDay()

    #layout.children[1] = newParkMap

def getCurrentSecondIndex():
    return currentSecondIndex

def setCurrentSecondIndex(newSecondIndex):
    currentSecondIndex = newSecondIndex

def createParkForNextDay():
    #currentSecondIndex = getCurrentSecondIndex()
    if currentIndexForDays is not len(days)-1: #IF THE CURRENT DAY IS NOT THE LAST DAY,
                                               #GO TO THE NEXT DY
        currentIndexForDays = currentIndexForDays + 1
    else:#IF THE CURRENT DAY IS THE LAST ONE, MOVE BACK TO THE FIRST DAY
        currentIndexForDays = 0

    dayPassedToCreatePark = days[currentIndexForDays]
    dayTimeIDMapPassedToCreatePark = allDaysTimeIDMap[currentIndexForDays]
    dayTimesPassedToCreatePark = allDaysTimes[currentIndexForDays]

    currentSecondIndex = 0
    secondPassedToCreatePark = float(dayTimesPassedToCreatePark[currentSecondIndex])

    newParkMap = createPark(dayPassedToCreatePark, dayTimeIDMapPassedToCreatePark,
                    dayTimesPassedToCreatePark, secondPassedToCreatePark)

    #day__select.value = dayPassedToCreatePark
    #time_select.value = dayTimesPassedToCreatePark[0]
    #time_select.options = dayTimesPassedToCreatePark

    return newParkMap

def goToPrevSecond():
    pass





#execute functionality
#day__select.on_change('value', updateDay)
#time_select.on_change('value', updateTime)
scan_next_second_button.on_click(goToNextSecondV2)
#scan_prev_hour_button.on_click(goToPrevSecond)





inputs = column(widgetbox(day__select, time_select, scan_prev_hour_button, scan_next_second_button, sizing_mode="scale_both"))
layout = row(inputs, parkMap)
curdoc().add_root(layout)
curdoc().title = "Park Map"
