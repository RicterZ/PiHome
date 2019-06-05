# coding: utf-8
from rhome.room import Room
from rhome.sensor import ht, aloud_sound
from rhome.monitor import Monitor

monitor = Monitor(interval=1)

room = Room(name='bedroom')
room.add_sensor(ht.HTSensor(pin=14))
room.add_sensor(aloud_sound.AloudSoundSensor(pin=13, callback=monitor.callback))

monitor.add_rome(room)
monitor.run()
