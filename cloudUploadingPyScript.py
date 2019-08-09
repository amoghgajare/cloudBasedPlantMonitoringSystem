from time import sleep
import serial
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
#I interafaced STM32F1 on COM8 port at 115200 baud rate
ser = serial.Serial('COM8', 115200)
ser.flushInput()
scope=['https://www.googleapis.com/auth/drive']
#credentials is the json file you download from Google API page
credentials=ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
client=gspread.authorize(credentials)
#In place of Sensor_Data, put name of a already existent google sheet in your drive
sheet=client.open('Sensor_Data').sheet1
n=10
errorNo=0

for a in range(0,n+1):
    try:
        sheet.update_cell(a+2,1,datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        ser.flushInput()
        ser_bytes = ser.readline()
        buff=ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        buff1=buff.split(",")
        L=buff1[0][1:len(buff1[0])]    #Light Intensity
        T=buff1[1][1:len(buff1[1])]    #Temperature
        S=buff1[2][1:len(buff1[2])]    #Soil Humidity
        sheet.update_cell(a+2,2,str(T))
        sheet.update_cell(a+2,3,str(S))
        sheet.update_cell(a+2,4,str(L))
    except:
        ser.flushInput()
    sleep(0.5)

