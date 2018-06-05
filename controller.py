import curses
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect(host="localhost")
 
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(2, 20, "Up")
        mqttc.publish("wificar","up")

    elif key == curses.KEY_DOWN: 
        stdscr.addstr(6,20, "Down")
        mqttc.publish("wificar","down")

    elif key == curses.KEY_LEFT: 
        stdscr.addstr(4, 10, "Left")
        mqttc.publish("wificar","left")

    elif key == curses.KEY_RIGHT: 
        stdscr.addstr(4, 30, "Right")
        mqttc.publish("wificar","right")

mqttc.dissconnect()
