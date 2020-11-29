import time
import mc6470

###########################    Uncomment below statements in case you get ModuleNotFoundError   #######################
#import sys
#sys.path.insert(0,'/home/pi/testpack/new_env/lib/python3.7/site-packages/');   #Note: replace path in this statement with the installation path of module in your raspberry pi. If you are not sure about the installation then re-run the command "pip3 install python-MC6470"
##################################################

accl = mc6470.Accelerometer()

while(1):
	time.sleep(1)
	(ax, ay, az) = accl.get_data()
	print("acceleration in x-axis: %.2f m/s2"%ax)
	print("acceleration in y-axis: %.2f m/s2"%ay)
	print("acceleration in z-axis: %.2f m/s2"%az)
	print("angular position: %.2f degrees"%accl.get_angle_in_degrees(ax,ay))
	print("")

