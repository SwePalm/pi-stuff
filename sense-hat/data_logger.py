from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from csv import writer

sense = SenseHat()

def get_sense_data():
    sense_data = []
    sense_data.append(round(sense.get_temperature(), 1))
    sense_data.append(round(sense.get_humidity(), 1))
    sense_data.append(datetime.now())
    return(sense_data)

timestamp = datetime.now()
delay = 3

with open('datalogger.csv', 'w', newline='') as f:
    my_writer = writer(f)
    my_writer.writerow(['temp', 'hum', 'datetime'])
    

    while True:
        data = get_sense_data()
        dt = data[-1] - timestamp
        if dt.seconds > delay:
            my_writer.writerow(data)
            print(data)
            timestamp = datetime.now()
    

    
