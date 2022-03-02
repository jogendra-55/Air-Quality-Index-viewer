from tkinter import *
from tkinter.ttk import Style
from PIL import ImageTk,Image
import requests
import json
root=Tk()
root.title('Air Quality Index APP')
root.geometry('400x110')
def ziplookup():
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip.get()+
                                   "&distance=25&API_KEY=9ED06886-0E1D-4665-922B-9D8737EBD897")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_clr = "#00e400"
        elif category == "Moderate":
            weather_clr = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_clr = "#ff7e00"
        elif category == "Unhealthy":
            weather_clr = "#ff0000"
        elif category == "Very Unhealthy":
            weather_clr = "#8f3f97"
        if category == "Hazardous":
            weather_clr = "#7e0023"

        root.configure(background=weather_clr)
        mylabel = Label(root, text=city + "  Air Quality " + str(quality) + "  " + category, font=('Helvetica,20'),background=weather_clr)
        mylabel.grid(row=3,column=1,columnspan=3)
    except Exception as e:
        api = "Error..."
        lbl=Label(root,text='Not a Zipcode')
        lbl.configure(bg='gray')
        lbl.grid(row=2,column=0)
        root.configure(background='black')

zip=Entry(root)
zip.grid(row=0,column=0,stick=W+E+N+S )
zp_bn=Button(root,text='Lookup Zip',command=ziplookup )
zp_bn.grid(row=0,column=1,stick=W+E+N+S)
root.mainloop()


