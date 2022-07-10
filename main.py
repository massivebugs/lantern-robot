import os
import subprocess
import time

def heartbeat(seconds: int = 5) -> None:
    """ Flashes the onboard PWR LED for a few seconds """

    if (os.geteuid() != 0):
        print('You need root permissions to run heartbeat()!') 
        return

    subprocess.check_output("echo heartbeat | tee /sys/class/leds/led1/trigger > /dev/null", shell=True)
    time.sleep(seconds)
    subprocess.run("echo default-on | tee /sys/class/leds/led1/trigger > /dev/null", shell=True)

if __name__ == "__main__":
    heartbeat()