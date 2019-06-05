# coding: utf-8
import RPi.GPIO as GPIO
from timeout_decorator import timeout
from rhome.sensor.vendor.dht11 import DHT11
from rhome.sensor.base_sensor import BaseSensor


class HTSensor(BaseSensor):
    name = 'Temperature and Humidity'
    description = ''

    fields = [
        'temperature',
        'humidity',
    ]

    def __init__(self, pin, *args, **kwargs):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
        self.sensor_instance = DHT11(pin=pin)
        super(HTSensor, self).__init__(*args, **kwargs)

    @property
    @timeout(BaseSensor.timeout)
    def temperature(self):
        while True:
            result = self.sensor_instance.read()
            if result.is_valid():
                return result.temperature

    @property
    @timeout(BaseSensor.timeout)
    def humidity(self):
        while True:
            result = self.sensor_instance.read()
            if result.is_valid():
                return result.humidity
