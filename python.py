import serial
import csv
import time

# Set the serial port (adjust to match your setup)
ser = serial.Serial('COM3', 9600, timeout=1)

# Open or create a CSV file to store data
with open('soil_moisture_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write header row
    csvwriter.writerow(['Timestamp', 'Soil Moisture Value'])

    try:
        while True:
            # Read line from serial
            line = ser.readline().decode('utf-8').strip()
            
            if "Soil Moisture" in line:
                # Extract the sensor value from the line
                value = line.split(': ')[1]

                # Get the current timestamp
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                # Write the timestamp and sensor value to the CSV
                csvwriter.writerow([timestamp, value])
                print(f"{timestamp}, Soil Moisture: {value}")

            time.sleep(1)

    except KeyboardInterrupt:
        print("Data logging stopped.")
        ser.clo
