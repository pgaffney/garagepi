## GaragePi - The Raspberry Pi Garage Door Opener

A wifi Raspberry Pi connected to a 2-channel relay connected to my actual garage door
remote allows me to open and close my garage door with just a browser on my smartphone.

## GaragePi Setup

GaragePi is built using the WebIOPi framework by Eric @ trouch.com. It is setup with this file structure below:

    pi@raspberrypi ~ $ tree garagepi
    garagepi
    ├── config
    ├── html
    │   └── index.html
    └── python
        └── garagepi.py

WebIOPi by default is setup with a login and password. But I only plan on using this when I'm on my local wifi
network so I opted to remove the password protection completely. You do this by removing /etc/webiopi/passwd or
empty it, then restart the webiopi server.

    sudo rm /etc/webiopi/passwd

Run this command below to load up webiopi with the new config file:

    sudo webiopi -d -c /home/pi/garagepi/config

Then load this up in your browser... again, change the IP to the IP of your Pi:

    http://192.168.1.60:8000

If that worked, then you can make GaragePi run at startup.

    sudo update-rc.d webiopi defaults

    # As a side note, you can start/stop the background service by doing:
    $ sudo /etc/init.d/webiopi start
    $ sudo /etc/init.d/webiopi stop

Then replace the default config file at /etc/webiopi/config with a symlink to the config file at /home/pi/garagepi/config.

    sudo rm /etc/webiopi/config
    sudo ln -s /home/pi/garagepi/config /etc/webiopi/config

Reboot and test it out.

    sudo reboot


## Save to Homescreen on Your Smartphone

I recommend you then save this page on the home screen of your smartphone, or at least bookmark it. Instructions
for [Android](http://mobile-pixels.com/pin-webapp-website-android-homescreen/) / [iOS](http://www.gottabemobile.com/2013/11/23/save-website-shortcut-ios-7-home-screen/).
