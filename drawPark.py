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



def createPark(currentDay, currentDayTimeIDMap, currentDayTimes, currentDayTime):
    p = figure(x_range=(0, 100), y_range=(0, 100), title="Park on "+currentDay+" at time "+str(currentDayTime))

    print("currentDayTime = ", currentDayTime)
    print("currentDayTimeIDMap[currentDayTime] = ", currentDayTimeIDMap[currentDayTime])
    print()

    for currentID in currentDayTimeIDMap[currentDayTime]:
        print("currentDayTime = ", currentDayTime)
        print("x=", currentDayTimeIDMap[currentDayTime][currentID][1][0], " y=",currentDayTimeIDMap[currentDayTime][currentID][1][1])
        p.circle(currentDayTimeIDMap[currentDayTime][currentID][1][0], currentDayTimeIDMap[currentDayTime][currentID][1][1], size=10, line_color="green", fill_color="green", fill_alpha=0.5)



    #Selections and Sliders
    day__select = Select(title = "Day",
                         value = "Friday",
                         width=200,
                         options = ["Friday", "Saturday", "Sunday"] )

    time_select = Select(title = "Time",
                         value = currentDayTimes[0],
                         width = 200,
                         options = currentDayTimes)

    scan_next_hour_button = Button(label="Scan Next Second", button_type="success")
    scan_prev_hour_button = Button(label="Scan Prev Second", button_type="success")




#Functionality og Selectors, Sliders, and Buttons
def updateDay():
    pass

def updateTime():
    pass

def goToNextSecond():
    pass

def goToPrevSecond():
    pass

#execute functionality
#day__select.on_change('value', updateDay)
#time_select.on_change('value', updateTime)
#scan_next_hour_button(goToNextSecond)
#scan_prev_hour_button(goToPrevSecond)


inputs = column(widgetbox(day__select, time_select, scan_prev_hour_button, scan_next_hour_button, sizing_mode="scale_both"))
layout = row(inputs, p)
curdoc().add_root(layout)
curdoc().title = "Park Map"
