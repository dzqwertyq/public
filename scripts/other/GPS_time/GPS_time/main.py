from serial import Serial, SerialException
import os
from datetime import datetime, timedelta
from time import sleep

#params
serial_baudrate = 4800
sleep_after_error = 10 #sec
test_script = True

class serialReader:
    def __init__(self, baudrate):
        self.baudrate = baudrate

    def open(self):
        for i in range(0, 256):
            port='{}{}'.format(portName, i)
            try:
                self.ser = Serial(port, 4800,timeout=5)
                logWrite('Serial {} connected'.format(port))
                break
            except SerialException as e:
                if i == 0:
                    logWrite('Port search: {0}0-{0}256'.format(portName))
                if i == 256:
                    logWrite('Error: Serial port is not free to connect. {}'.format(e))
                    sleep(10)

    def read_data(self):
        while True:
            try:
                time = parse_datetime(str(self.ser.readline()))
                if time is not None:
                    return time
                #return self.ser.readline()
            except:
                sleep(sleep_after_error)
                logWrite('Error: No serial device or connection lost. Trying to reconnect...')
                self.open()

    def close(self):
        self.ser.close()

def logWrite(logStr="-----------"):
    path = os.path.dirname(os.path.abspath(__file__))
    path = path + 'GPS_time_log.log'
    now = datetime.now()
    now = now.strftime("%m/%d/%Y, %H:%M:%S")
    logStr = "{date}: {string} {separator}".format(date=now, string=logStr, separator='\n')
    file = open(path, 'a')
    file.write(logStr)
    file.close()

def checkOS():
    global portName
    global OSname
    OSname = os.name
    if os.name == 'nt':
        portName = 'COM'
    if os.name == 'posix':
        portName = '/dev/ttyUSB'

def parse_datetime(str=''):
    str = str.split(',')
    if str[0] == "b'$GNRMC":
        res = '{} {}'.format(str[1], str[9])
        return res

def set_time(datetime_object):
    # UTC +3 Minsk/Moscow
    datetime_object = datetime_object + timedelta(hours=3)
    str1 = 'gps    - {}'.format(datetime_object.time())
    str2 ='locale - {}'.format(datetime.now().time())
    logWrite(str1)
    logWrite(str2)
    print(str1)
    print(str2)
    #timeDelta = datetime_object - datetime.now()
    #print(timeDelta.seconds)
    #f timeDelta == '86399':
    #    print('local time = serial time')
    #else:
    #    print(timeDelta.seconds)
    #sleep(sleep_after_error*60)





# Run
# ERROR закрывается подключение к КОМ порту, переписать с открытием подключения
logWrite()
logWrite('Script started')
checkOS()
reader = serialReader(serial_baudrate)
reader.open()
while True:
    line = reader.read_data()
    datetime_object = datetime.strptime(line, '%H%M%S.%f %d%m%y')
    set_time(datetime_object)
    line = reader.read_data()
    datetime_object = datetime.strptime(line, '%H%M%S.%f %d%m%y')
    set_time(datetime_object)
    line = reader.read_data()
    datetime_object = datetime.strptime(line, '%H%M%S.%f %d%m%y')
    set_time(datetime_object)

    sleep(sleep_after_error*360)







