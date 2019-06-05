# coding: utf-8
import time
import requests

from rhome.logger import logger


class Monitor(object):
    rooms = []
    interval = 60
    result = {}

    def __init__(self, rooms=None, interval=60):
        if rooms is not None:
            self.rooms = rooms

        if isinstance(interval, (int,)):
            self.interval = interval

    def add_rome(self, room):
        self.rooms.append(room)

    def callback(self, room, sensor, data):
        logger.info('Callback function called by sensor \'{}\' of room \'{}\''.format(sensor.name, room.name))

        if room.name not in self.result:
            self.result[room.name] = {}

        self.result[room.name].update({sensor.name: data})

    def report(self, data):
        logger.debug('Report data ...')

        for k, v in data.iteritems():
            if k not in self.result:
                # different room
                self.result[k] = v
            else:
                # same room
                self.result[k].update(v)

        import pprint
        pprint.pprint(self.result)

        # clean
        self.result = {}

    def run(self):
        while True:
            result = {}
            for room in self.rooms:
                logger.info('Getting room \'{}\' data'.format(room.name))
                result[room.name] = room.get_data()

            self.report(result)
            logger.info('Sleep {}s'.format(self.interval))
            time.sleep(self.interval)
