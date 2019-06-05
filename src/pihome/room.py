# coding: utf-8
from pihome.logger import logger


class Room(object):
    name = None
    interval = None
    sensors = []

    def __init__(self, name, sensors=None):
        self.name = name
        if isinstance(sensors, (list,)):
            self.sensors = sensors

    def add_sensor(self, sensor):
        logger.info('Sensor \'{}\' added'.format(sensor.name))
        sensor.room = self
        self.sensors.append(sensor)

    def get_data(self):
        ret = {}
        for sensor in self.sensors:

            # forge callback
            import random
            if random.randint(1, 10) % 3 == 0:
                if sensor.callback is not None:
                    sensor.callback(channel=17)
            # forge end

            if not sensor.callback:
                logger.info('Getting data from sensor \'{}\''.format(sensor.name))
                ret[sensor.name] = sensor.get_data()

        return ret
