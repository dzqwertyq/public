from serial import Serial, SerialException
import os
from datetime import datetime


#params
port = 'COM4'
baudrate = 4800

ser = Serial('COM1', baudrate)

class SerialReader:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        try:
            self.ser = Serial(port, baudrate)
            logWrite('Serial {} connected'.format(port))
        except SerialException as e:
            logWrite('Error: Serial port is not free to connect. {}'.format(e))

    def read_data(self):
        return self.ser.readline()

    #def close(self):
    #    self.ser.close()

def logWrite(logStr="*****"):
    path = os.path.dirname(os.path.abspath(__file__))
    path = path + 'GPS_time_log.log'
    now = datetime.now()
    now = now.strftime("%m/%d/%Y, %H:%M:%S")
    #str = now +': '+logStr + '\n'
    logStr = "{date}: {string} {separator}".format(date=now, string=logStr ,separator='\n')
    file = open(path, 'a')
    file.write(logStr)
    file.close()

def locateSerial():
    if os.name == 'nt':
        for i in range(0, 256):
            return('{}{}'.format('COM',i))

print(locateSerial())
# Usage
logWrite()
logWrite('Script started')
reader = SerialReader(port, baudrate)
while True:
    data = reader.read_data()
    print(data)

reader.close()