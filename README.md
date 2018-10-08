wificar is a small rc car i reperposed as a small side project to demostrate 
the use of micropython for making simple IOT devices

what you will need:
<br> > a esp8266 microcontroller with micropython flashed on it.
<br> > a linux machine to act as the mqtt server

tools you may need :
<br> > https://github.com/wendlers/mpfshell 
<br> > https://mosquitto.org/download/

Note:
the script and code worked out for me in my testing your results may vary please feel free to tweak 
and make adjustments as required

how to use:
<br> > the main.py , boot.py and config.py files need to be copied on the esp8266 board you can use mpfshell for this
<br> > make changes to the mqtt service acording to your network and ip settings 
<br> > start the mqtt service on the linux machine 
<br> > run the controller.py file to control the messages sent 

warning: 
the code is given as is with no implied warranty . use at own risk and please dont use any of
it for production :) .
