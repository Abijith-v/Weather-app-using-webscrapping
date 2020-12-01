#web scrapping xD

import requests #used for webscrapping
from bs4 import BeautifulSoup
from tkinter import Label #tkinter for GUI
from tkinter import Tk
from PIL import ImageTk,Image

#declare url to store the url of weather
url="https://weather.com/en-IN/weather/today/l/0259f5cb8f7564c47113a67cc9f7eac0645d7ceeff8df54764959788b5038b15"

#creating GUI, using master
master=Tk()	#creates window ,master can be named anything we want
master.title("Weather")	#sets title for the window
master.config(bg="black")	#sets bg colour
#master.wm_attributes("-transparentcolor", "black")

#set up an image inside the window

img=Image.open("C:/Users/AV/Desktop/python projects/Weather app/weathericon.png")
img=img.resize((150,150))
img=ImageTk.PhotoImage(img) #convert img to tkinter readable form, now "img" can be used.


#declare a function thatll take the info from the url

def getWeather():
	page=requests.get(url)	#get the website
	soup=BeautifulSoup(page.content,"html.parser")
	loc=soup.find("h1",class_="CurrentConditions--location--1Ayv3").text	#class naem of the field from the html file using inspect
	temp=soup.find("span",class_="CurrentConditions--tempValue--3KcTQ").text
	pred=soup.find("div",class_="CurrentConditions--phraseValue--2xXSr").text
	comment=soup.find("div",class_="CurrentConditions--precipValue--RBVJT").text
	
	#imageurl=soup.find("svg",class_="CurrentConditions--wxIcon--2cDUg Icon--icon--2AbGu Icon--fullTheme--3jU2v")

	location.config(text=loc)	#set the text into the labels
	temprature.config(text=temp+"C")
	weatherPrediction.config(text=pred)
	extraComment.config(text=comment)

	temprature.after(60000,getWeather) # recurse the function after every 1 min(60000)
	master.update()
	print(loc,temp,pred,comment)
#declaring labels

location=Label(master,font=("Amatic SC bold",30),bg="black",fg="white")	#set fontface and size for location, and set colour as white
location.grid(row=0,sticky="N",padx=100) #place it inside the window using grid, row is 0, sticky puts it to NORTH, x padding is set to 100

temprature=Label(master,font=("Amatic SC bold",40),bg="black",fg="white")
temprature.grid(row=1,sticky="W",padx=50)

Label(master,image=img,bg="black").grid(row=1,sticky="E")

weatherPrediction=Label(master,font=("Amatic SC bold",20),bg="black",fg="white")
weatherPrediction.grid(row=1,sticky="W",padx=150)

extraComment=Label(master,font=("Amatic SC bold",15),bg="black",fg="white")
extraComment.grid(row=3,sticky="W",padx=100,pady=30)



getWeather()

master.mainloop()
