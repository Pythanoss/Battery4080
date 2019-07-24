from psutil import sensors_battery
from ctypes import windll
import time



def main():
    while(1):
        battery = sensors_battery()

        while(battery.power_plugged==False):
            battery = sensors_battery()
            if battery.percent <= 40 and battery.power_plugged==False:
                battery = sensors_battery()
                time.sleep(60)
                windll.user32.MessageBoxW(0, "Battery Reached 40. Please Connect the charger.", "Battery Alert", 1)

            time.sleep(60)


        while(battery.power_plugged):
            battery = sensors_battery()
            if battery.percent >= 80 and battery.power_plugged==True:
                windll.user32.MessageBoxW(0, "Battery Charged to 80. Please Disconnect the charger", "Battery Alert", 1)
                battery = sensors_battery()
                time.sleep(60)

            time.sleep(60)

        time.sleep(60)







if __name__ == '__main__':
    print("Battery4080 Started.")
    main()