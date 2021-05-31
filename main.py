from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Hp\\Downloads\\covid.ico",
        timeout = 10
    )

def webData(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    #notifyme("Devsi","Lets stop the spread of this virus together")
    while True:
        my_html_data = webData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(my_html_data, 'html.parser')
        # print(soup.prettify())
        mystr = ""

        for tr in soup.find_all('tr'):
            mystr += tr.get_text()  # Converting the Parsed Data to a String
        mystr = mystr[1:]
        myList = (mystr.split("\n\n"))

        states = ['Haryana', 'Delhi', 'Punjab']  # Enter Your State Name Here (Don't Enter More Than 5 States)
        for item in myList[0:31]:
            dataList = (item.split('\n'))
            if dataList[1] in states:
                notify_title = 'Cases of Covid-19 In India'
                notify_text = f" State: {dataList[1]}\n Indian Cases : {dataList[2]}\n Cured : {dataList[3]}\n Deaths : {dataList[4]}"
                notifyme(notify_title, notify_text)
                time.sleep(2)
        time.sleep(3600)  # Loop For 1 Hour (1 hour = 3600 seconds)
