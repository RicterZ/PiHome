# coding: utf-8
import time
from timeout_decorator.timeout_decorator import TimeoutError
from rhome.logger import logger


class BaseSensor(object):
    name = None
    description = None
    fields = None

    timeout = 5
    interval = None

    callback = None
    _callback = None

    room = None
    timestamp = None

    def __init__(self, *args, **kwargs):
        if 'callback' in kwargs:
            self.callback = self.wrap_callback
            self._callback = kwargs['callback']

        logger.info('Initialize sensor \'{}\''.format(self.name))

    def __str__(self):
        return '<Sensor: {}>'.format(self.name)

    def get_data(self):
        if self.callback:
            return

        if self.fields is None:
            raise Exception('No fields')

        data = {}
        for field in self.fields:
            logger.debug('Getting data \'{}\' from sensor'.format(field))
            try:
                ret = getattr(self, field)
                data[field] = ret
            except TimeoutError:
                logger.warning('Timed out while getting data \'{}\' from sensor \'{}\''.format(field, self.name))
                data[field] = 'TIMEOUT'

        data['timestamp'] = int(time.time())
        return data

    def wrap_callback(self, channel):
        raise NotImplementedError

    def invoke_callback(self, data=None):
        self._callback(self.room, self, data=data)
