# coding: utf-8
import RPi.GPIO as GPIO
from rhome.sensor.base_sensor import BaseSensor
from rhome.logger import logger


class AloudSoundSensor(BaseSensor):
    name = 'Aloud Sound Forge'
    description = ''

    fields = []

    def __init__(self, pin, *args, **kwargs):
        super(AloudSoundSensor, self).__init__(*args, **kwargs)

    def wrap_callback(self, channel):
        # process data
        data = {'message': 'I heard it'}
        self.invoke_callback(data)
