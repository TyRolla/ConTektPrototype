import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)

accelerometer = adafruit_adxl34x.ADXL345(i2c, address=83)
accelerometer.enable_motion_detection()
accelerometer.enable_tap_detection()
accelerometer.enable_freefall_detection()

# print(dir(accelerometer))

def convertToG(maxScale, x, y, z):
    range = float(maxScale)
    X = (2 * range * float(x)) / (2**16)
    Y = (2 * range * float(y)) / (2**16)
    Z = (2 * range * float(z)) / (2**16)
    return X, Y, Z

def inDanger(x, y, z):
    x = x / 9.80665
    y = y / 9.80665
    z = z / 9.80665
    if abs(x) > 2 or abs(y) > 2 or abs(z) > 2:
        print("Bad Day")

threshold = 8

while True:
    x, y, z = accelerometer.acceleration
    if x >= threshold:
      print("Rotated Left")
    if x <= -threshold:
      print("Rotated Right")
    if y >= threshold:
      print("Rotated Up")
    if y <= -threshold:
      print("Rotated Down")
    if z <= -threshold:
      print("Upside Down")

    #xG, yG, zG = convertToG(24, x, y, z)
    #print(x, y, z)
    print(inDanger(x, y, z) or "")
    #print("Tapped: %s" % accelerometer.events['tap'])
    #print("Free Fall %s" % accelerometer.events['freefall'])
    time.sleep(000.1)
