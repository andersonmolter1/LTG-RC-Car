import qwiic_icm20948
import time
import sys

def runExample():
	IMU = qwiic_icm20948.QwiicIcm20948()
	IMU.begin()
	IMU.getAgmt() # read all axis and temp from sensor, note this also updates all instance variables
	return IMU.ayRaw
		time.sleep(0.03)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		sys.exit(0)