#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *
import requests
import json
from datetime import datetime
 
root =Tk()
root.geometry("600x600") #size of the window
root.resizable(0,0) #fixed window size
#title
root.title("Weather Application - by Aditya Pandey")
root.configure(background='light blue')

city_value = StringVar()


def showWeather():
    api_key = "paste your api key here"
    city_name = city_value.get()
    complete_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + '&appid='+api_key
    response = requests.get(complete_url)
    
#-----------shows the response in python from json readable
    x = response.json()
    
    
    tfield.delete("1.0", "end")
    
    
    if x["cod"] == 200:
        kelvin = 273
        
        
#-----------Functions that fetch and display:

        current_temperature = int(x['main']['temp']-kelvin)
        feels_like = int(x['main']['feels_like']-kelvin)
        current_humidity = x['main']["humidity"]
        wind_speed = x['wind']['speed']*3.6
        current_pressure = x['main']["pressure"]
        cloudy = x['clouds']['all']
        timezone = x['timezone']
        weather_description = x["weather"][0]["description"]
#-----------These values will be the output

        weather = f"\nWeather in:{city_name}\nTemperature (Celsius): {current_temperature}°\nFeels like in (Celsius): {feels_like}°\nPressure: {current_pressure} hPa\nHumidity: {current_humidity}%\nCloud: {cloudy}%\nInfo: {weather_description}" 
    else: 
        weather = f"\n\tWeather for '{city_name}' not found! \n\t Please enter valid City name!"
    
    tfield.insert(INSERT, weather)


#GUI:
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#OUTPUT VISIBLE BY: 
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()


# In[ ]:




