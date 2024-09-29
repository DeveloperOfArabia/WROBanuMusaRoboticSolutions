import serial
import csv
import time

# COM3 changes depending on Arduino used
ser = serial.Serial('COM3', 9600, timeout=1)

with open('sensor_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Timestamp', 'Soil Moisture', 'LDR (Light Intensity)', 'Temperature (C)'])

    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if "Soil Moisture" in line:
                try:
                    values = line.split(", ")
                    soil_moisture = values[0].split(": ")[1]
                    ldr_value = values[1].split(": ")[1]
                    temperature_c = values[2].split(": ")[1]
                    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                    csvwriter.writerow([timestamp, soil_moisture, ldr_value, temperature_c])
                    print(f"{timestamp}, Soil Moisture: {soil_moisture}, LDR: {ldr_value}, Temperature (C): {temperature_c}")

                except IndexError:
                    print("Error in data line:", line)

            time.sleep(1)

    except KeyboardInterrupt:
        print("logging stopped")
        ser.close()
