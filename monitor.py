import wmi
import datetime
import numpy as np

# ---Settings---

# Poll Temperatures every x seconds. 1 does not work!
RATE  = 3

# The resulting file
# Be sure to open it and clear it so no data is saved inside!
CSVFILE = "data.csv"


# ---Loop---

# Set a played variable for later use
played = False

# Loop until canceled (with CTRL+C)
while True:

    # Each epoch get the current time and store it in a list
    now = datetime.datetime.now()

    # Save the second 
    second = int(now.strftime("%S"))
    print("running... current sec: ", second)

    if not played:

        # Every x seconds
        if second % RATE == 0:


            played = True

            # Start a list with the time
            time_list = [
                int(now.strftime("%Y")), 
                int(now.strftime("%m")), 
                int(now.strftime("%w")), 
                int(now.strftime("%H")), 
                int(now.strftime("%M")), 
                int(now.strftime("%S"))
            ]

            # Open OpenHardwareMonitor
            w = wmi.WMI(namespace="root\OpenHardwareMonitor")
            sensors = w.Sensor()

            index = 1;

            for sensor in sensors:
                # Get only Temperature Sensors
                if sensor.SensorType==u'Temperature':

                    # Depending on your setup you might have diiffernet names and sensors
                    if sensor.Name == 'CPU Package':
                        # CPU Package is the name that OpenHardwareMonitor shows
                        # A name and a corresponding value is added to the list
                        time_list.append('CPU')
                        time_list.append(sensor.Value)
                    if sensor.Name == 'GPU Core':
                        time_list.append('GPU')
                        time_list.append(sensor.Value)
                    if sensor.Name == 'System 1':
                        time_list.append('System 1')
                        time_list.append(sensor.Value)
                    if sensor.Name == 'System 2':
                        time_list.append('System 2')
                        time_list.append(sensor.Value)
                    if sensor.Name == 'Temperature':
                        time_list.append('Drive ' + str(index))
                        time_list.append(sensor.Value)
                        index += 1

            # Convert it to an array
            temps = np.array(time_list)

            # print (temps)

            # Save the file
            with open(CSVFILE,'a+') as f:

                csv_string = ""
                for item in temps:
                    if csv_string == '':
                        csv_string = str(item)
                    else:
                        csv_string += ',' + str(item)

                f.writelines(csv_string + '\n')

    elif second % RATE != 0:   
        played = False

        
