import serial
import csv
import time

# COM3 changes depending on the Arduino
ser = serial.Serial('COM3', 9600, timeout=1)

with open('soil_moisture_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(['Timestamp', 'Soil Moisture Value'])

    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            
            if "Soil Moisture" in line:
                value = line.split(': ')[1]
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S
                csvwriter.writerow([timestamp, value])
                print(f"{timestamp}, Soil Moisture: {value}")

            time.sleep(1)

    except KeyboardInterrupt:
        print("Data logging stopped.")
        ser.clo
