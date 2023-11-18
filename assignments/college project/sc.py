
import serial
# Create a serial object
ser = serial.Serial('COM5')
# Open the serial port
ser.open()
# Write data to the serial port
ser.write(b'Hello, Arduino!')
# Read data from the serial port
data = ser.read()
# Close the serial port
ser.close()